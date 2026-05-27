import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt

from src.predict import predict_job
from src.preprocess import clean_text
from database import (
    init_db,
    insert_prediction,
    fetch_all
)

# =========================================
# DATABASE INIT
# =========================================

init_db()

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================
# SIDEBAR MENU
# =========================================

menu = st.sidebar.selectbox(
    "Menu",
    ["Predict", "Dashboard", "History"]
)

# =========================================
# PREDICT PAGE
# =========================================

if menu == "Predict":

    st.title("🛡️ JobShield AI")
    st.subheader("AI-Powered Fake Job Detection System")

    st.markdown("---")

    # INPUT
    job_text = st.text_area(
        "Paste Job Description",
        height=300,
        placeholder="Paste complete job description here..."
    )

    # ANALYZE BUTTON
    if st.button("Analyze Job"):

        # Empty input
        if not job_text.strip():

            st.warning("Please enter a job description.")

        else:

            with st.spinner("Analyzing Job Description..."):

                time.sleep(1)

                # Clean text
                cleaned_text = clean_text(job_text)

                # Prediction
                result = predict_job(cleaned_text)

                # Scores
                fake_score = result["fake_score"]
                real_score = result["real_score"]

                # Prediction
                is_fake = result["prediction"] == 1

                # Save to database
                final_result = (
                    "FAKE JOB"
                    if is_fake
                    else "REAL JOB"
                )

                insert_prediction(
                    job_text,
                    final_result
                )

            st.markdown("---")

            # RESULT SECTION
            st.subheader("Detection Result")

            if is_fake:

                st.error("⚠️ Fake Job Detected")

            else:

                st.success("✅ Legitimate Job Posting")

            # METRICS
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Fake Probability",
                    f"{fake_score:.2f}%"
                )

            with col2:
                st.metric(
                    "Real Probability",
                    f"{real_score:.2f}%"
                )

            # PROGRESS BAR
            st.write("### Scam Risk Level")

            st.progress(int(fake_score) / 100)

            # GAUGE CHART
            fig = go.Figure(go.Indicator(

                mode="gauge+number",

                value=fake_score,

                title={'text': "Fraud Risk Score"},

                gauge={

                    'axis': {'range': [0, 100]},

                    'bar': {'color': "red"},

                    'steps': [

                        {'range': [0, 30], 'color': "green"},
                        {'range': [30, 70], 'color': "orange"},
                        {'range': [70, 100], 'color': "red"}

                    ],
                }
            ))

            fig.update_layout(height=400)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # FINAL MESSAGE
            st.markdown("---")

            if fake_score >= 70:

                st.error(
                    "This posting contains multiple suspicious patterns commonly found in fraudulent jobs."
                )

            elif fake_score >= 40:

                st.warning(
                    "This posting shows some suspicious characteristics. Verify company details carefully."
                )

            else:

                st.success(
                    "This posting appears relatively safe based on AI analysis."
                )

# =========================================
# DASHBOARD PAGE
# =========================================

elif menu == "Dashboard":

    st.title("📊 JobShield AI Dashboard")

    rows = fetch_all()

    total = len(rows)

    fake_count = sum(
        1 for row in rows
        if "FAKE" in row[2]
    )

    real_count = sum(
        1 for row in rows
        if "REAL" in row[2]
    )

    # METRICS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Jobs Checked",
            total
        )

    with col2:
        st.metric(
            "Fake Jobs",
            fake_count
        )

    with col3:
        st.metric(
            "Real Jobs",
            real_count
        )

    st.markdown("---")

    # PIE CHART
    st.subheader("Fake vs Real Jobs")

    if total > 0:

        labels = ["Fake Jobs", "Real Jobs"]

        sizes = [fake_count, real_count]

        fig, ax = plt.subplots()

        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.axis("equal")

        st.pyplot(fig)

    else:

        st.info("No predictions available yet.")

    st.markdown("---")

    # TABLE
    st.subheader("Recent Predictions")

    if total > 0:

        df = pd.DataFrame(
            rows,
            columns=[
                "ID",
                "Job Description",
                "Result"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.warning("No history available.")

# =========================================
# HISTORY PAGE
# =========================================

elif menu == "History":

    st.title("📜 Prediction History")

    rows = fetch_all()

    if len(rows) > 0:

        for row in rows:

            st.markdown("---")

            st.write(f"### Record #{row[0]}")

            st.write("#### Job Description")
            st.write(row[1])

            st.write("#### Result")
            st.write(row[2])

    else:

        st.warning("No prediction history found.")