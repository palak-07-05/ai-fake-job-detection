import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import fetch_all

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Dashboard | JobShield AI",
    page_icon="📊",
    layout="wide"
)

# =========================================
# PAGE TITLE
# =========================================

st.title("📊 JobShield AI Dashboard")

st.markdown("""
Track fake job detection statistics, AI insights,
and recent recruitment scam analysis activity.
""")

st.markdown("---")

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
# OVERVIEW METRICS
# =========================================

st.subheader("📌 Overview")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="Total Jobs Checked",
        value=total
    )

with col2:

    st.metric(
        label="Fake Jobs Detected",
        value=fake_count
    )

with col3:

    st.metric(
        label="Legitimate Jobs",
        value=real_count
    )

st.markdown("---")

# =========================================
# CHART SECTION
# =========================================

st.subheader("📈 Detection Distribution")

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
        figsize=(6, 6)
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
# RECENT PREDICTIONS TABLE
# =========================================

st.subheader("🧾 Recent Predictions")

if total > 0:

    df = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Job Description",
            "Result"
        ]
    )

    # latest first
    df = df[::-1]

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

else:

    st.warning(
        "Prediction history is empty."
    )

st.markdown("---")

# =========================================
# AI INSIGHTS
# =========================================

st.subheader("🧠 AI Insights")

if total == 0:

    st.info(
        "Analyze job descriptions to generate AI insights."
    )

elif fake_count > real_count:

    st.error(
        "⚠️ A high number of suspicious job postings were detected. Users should verify recruiters and company details carefully."
    )

elif real_count > fake_count:

    st.success(
        "✅ Most analyzed job postings appear legitimate based on AI analysis."
    )

else:

    st.info(
        "📌 Equal number of fake and real job postings detected."
    )

st.markdown("---")

# =========================================
# SYSTEM STATUS
# =========================================

st.subheader("⚙️ System Status")

st.success(
    "🟢 AI Detection System Active"
)

st.caption(
    "Machine Learning • NLP • Real-Time Fraud Detection"
)