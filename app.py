import streamlit as st
import time
import plotly.graph_objects as go

from src.predict import predict_job
from src.preprocess import clean_text

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("🛡️ JobShield AI")
st.subheader("AI-Powered Fake Job Detection System")

st.markdown("---")

# =========================================
# INPUT
# =========================================

job_text = st.text_area(
    "Paste Job Description",
    height=300,
    placeholder="Paste complete job description here..."
)

# =========================================
# ANALYZE BUTTON
# =========================================

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

        st.markdown("---")

        # =========================================
        # RESULT SECTION
        # =========================================

        st.subheader("Detection Result")

        if is_fake:

            st.error("⚠️ Fake Job Detected")

        else:

            st.success("✅ Legitimate Job Posting")

        # =========================================
        # METRICS
        # =========================================

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

        # =========================================
        # PROGRESS BAR
        # =========================================

        st.write("### Scam Risk Level")

        st.progress(int(fake_score) / 100)

        # =========================================
        # GAUGE CHART
        # =========================================

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

        fig.update_layout(
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =========================================
        # FINAL MESSAGE
        # =========================================

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