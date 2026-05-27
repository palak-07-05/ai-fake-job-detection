import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import fetch_all

# =========================================
# PAGE TITLE
# =========================================

st.title("📊 JobShield AI Dashboard")

st.markdown(
    "Monitor fake job detection statistics and recent activity."
)

# =========================================
# FETCH DATABASE RECORDS
# =========================================

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

# =========================================
# METRICS
# =========================================

st.subheader("Overview")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Total Jobs Checked",
        total
    )

with col2:

    st.metric(
        "Fake Jobs Detected",
        fake_count
    )

with col3:

    st.metric(
        "Legitimate Jobs",
        real_count
    )

st.markdown("---")

# =========================================
# PIE CHART
# =========================================

st.subheader("Detection Distribution")

if total > 0:

    labels = [
        "Fake Jobs",
        "Legitimate Jobs"
    ]

    sizes = [
        fake_count,
        real_count
    ]

    fig, ax = plt.subplots(
        figsize=(5, 5)
    )

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

else:

    st.info(
        "No prediction data available yet."
    )

st.markdown("---")

# =========================================
# RECENT PREDICTIONS
# =========================================

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

    df = df[::-1]

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning(
        "Prediction history is empty."
    )

st.markdown("---")

# =========================================
# AI INSIGHTS
# =========================================

st.subheader("AI Insights")

if total == 0:

    st.info(
        "Analyze some job descriptions to generate insights."
    )

elif fake_count > real_count:

    st.error(
        "⚠️ High number of suspicious job postings detected."
    )

elif real_count > fake_count:

    st.success(
        "✅ Most analyzed jobs appear legitimate."
    )

else:

    st.info(
        "📌 Equal number of fake and real jobs detected."
    )

st.markdown("---")

# =========================================
# SYSTEM STATUS
# =========================================

st.subheader("System Status")

st.success(
    "🟢 AI Detection System Active"
)