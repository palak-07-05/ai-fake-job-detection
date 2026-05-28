import streamlit as st
import base64
import os

# PAGE CONFIG
st.set_page_config(
    page_title="About JobShield AI",
    layout="wide"
)

# LOAD IMAGE FUNCTION
def get_base64(file_path):
    if not os.path.exists(file_path):
        return None

    with open(file_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    return encoded


# LOAD BACKGROUND IMAGE
bg_image = get_base64("assets/background.png")

# BACKGROUND STYLE
if bg_image:
    background_style = f"""
    background-image:
    linear-gradient(
        rgba(5, 8, 22, 0.85),
        rgba(5, 8, 22, 0.92)
    ),
    url("data:image/png;base64,{bg_image}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    """
else:
    background_style = """
    background:
    linear-gradient(
        135deg,
        #050816,
        #0f172a,
        #111827
    );
    """


# CUSTOM CSS
st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif;
    color: white;
}}

.stApp {{
    {background_style}
    color: white;
}}

#MainMenu, footer, header {{
    visibility: hidden;
}}

.main-container {{
    padding: 2rem 4rem;
}}

.hero {{
    text-align: center;
    padding-top: 40px;
}}

.hero-title {{
    font-size: 60px;
    font-weight: 700;
    background: linear-gradient(90deg, #ffffff, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.hero-subtitle {{
    font-size: 20px;
    color: #CBD5E1;
}}

.glass-card {{
    background: rgba(15, 23, 42, 0.72);
    backdrop-filter: blur(16px);
    border-radius: 28px;
    padding: 45px;
    margin-top: 30px;
    border: 1px solid rgba(255,255,255,0.08);
}}

.section-title {{
    font-size: 30px;
    font-weight: 700;
    color: #C084FC;
    margin-top: 35px;
    margin-bottom: 18px;
}}

.description {{
    color: #CBD5E1;
    font-size: 17px;
    line-height: 1.9;
}}

.feature-box {{
    background: rgba(30, 41, 59, 0.82);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.06);
    transition: 0.3s ease;
}}

.feature-box:hover {{
    transform: translateY(-4px);
}}

.feature-box h3 {{
    color: white;
}}

.feature-box p {{
    color: #CBD5E1;
    margin: 0;
}}

.footer {{
    text-align: center;
    margin-top: 50px;
    color: #94A3B8;
    font-size: 14px;
}}

@media screen and (max-width: 768px) {{
    .hero-title {{ font-size: 42px; }}
    .main-container {{ padding: 1rem; }}
}}

</style>
""", unsafe_allow_html=True)


# MAIN CONTAINER
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <div class="hero-title"> JobShield AI</div>
    <div class="hero-subtitle">AI-Powered Fake Job Detection Platform</div>
</div>
""", unsafe_allow_html=True)

# GLASS CARD
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# ABOUT (IMPROVED)
st.markdown("""
<div class="section-title">About JobShield AI</div>

<div class="description">
JobShield AI is a machine learning-based web application designed to detect fake job postings and help users avoid online recruitment scams.

It analyzes job descriptions using Natural Language Processing (NLP) and identifies suspicious patterns such as unrealistic salary claims, misleading job roles, and fraudulent hiring behavior.

The system is built to assist students, freshers, and job seekers in making safer and more informed career decisions.
</div>
""", unsafe_allow_html=True)

# FEATURES DATA (IMPROVED)
features = [
    ("🤖 AI-Based Detection", "Classifies job postings as real or fake using trained ML models."),
    ("📊 Fraud Probability Score", "Displays confidence level of prediction for better transparency."),
    ("⚡ Real-Time Analysis", "Instantly processes job descriptions and generates results."),
    ("🛡️ Scam Prevention", "Helps users avoid fraudulent and misleading job offers.")
]

# FEATURES TITLE
st.markdown("""
<div class="section-title">
Core Features
</div>
""", unsafe_allow_html=True)

# HORIZONTAL FEATURES
cols = st.columns(len(features), gap="small")

for col, (title, desc) in zip(cols, features):
    with col:
        st.markdown(f"""
        <div class="feature-box" style="padding:16px; min-height:140px;">
            <h3 style="font-size:16px; margin-bottom:8px;">{title}</h3>
            <p style="font-size:13px; line-height:1.5;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# TECHNOLOGIES + FUTURE
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="section-title">Technologies Used</div>

    <div class="description">
    • Python (Core Development)<br>
    • Streamlit (Web Framework)<br>
    • Machine Learning (Classification Models)<br>
    • NLP (Text Processing)<br>
    • Scikit-learn (Model Training)<br>
    • TF-IDF Vectorization (Feature Extraction)<br>
    • Pandas (Data Handling)<br>
    • SQLite (Database)<br>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="section-title">Future Vision</div>

    <div class="description">
    JobShield AI is being developed into a complete job safety and recruitment intelligence system.

    <ul>
    <li>Resume-job compatibility matching</li>
    <li>Fake company detection module</li>
    <li>AI chatbot for job verification</li>
    <li>Advanced fraud analytics dashboard</li>
    <li>Cloud-based deployment</li>
    <li>User authentication system</li>
    </ul>

    
    </div>
    """, unsafe_allow_html=True)

# CLOSE CARD
st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
Built using AI, NLP & Machine Learning
</div>
""", unsafe_allow_html=True)

# CLOSE MAIN
st.markdown("</div>", unsafe_allow_html=True)