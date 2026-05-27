import streamlit as st
import base64
import os

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="About JobShield AI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================
# FUNCTION TO LOAD IMAGE
# =========================================

def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# =========================================
# LOAD BACKGROUND IMAGE
# =========================================

bg_image = get_base64("assets/background.png")

# =========================================
# BACKGROUND CSS
# =========================================

background_css = ""

if bg_image:
    background_css = f"""
    background-image: url("data:image/png;base64,{bg_image}");
    """

# =========================================
# CUSTOM CSS
# =========================================

st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif;
    color: white;
}}

/* MAIN APP */

.stApp {{
    {background_css}
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-color: #050816;
}}

/* REMOVE STREAMLIT DEFAULTS */

header {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

#MainMenu {{
    visibility: hidden;
}}

/* MAIN OVERLAY */

.main-overlay {{
    background: rgba(5, 8, 22, 0.82);
    padding: 40px;
    border-radius: 25px;
    margin-top: 20px;
}}

/* HERO SECTION */

.hero {{
    text-align: center;
    padding-top: 30px;
    padding-bottom: 30px;
}}

.hero-title {{
    font-size: 60px;
    font-weight: 700;
    color: white;
}}

.hero-subtitle {{
    font-size: 22px;
    color: #CBD5E1;
    margin-top: 10px;
}}

/* GLASS CARD */

.glass-card {{
    background: rgba(17, 24, 39, 0.75);
    backdrop-filter: blur(14px);
    border-radius: 24px;
    padding: 40px;
    margin-top: 30px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 30px rgba(124, 58, 237, 0.35);
}}

/* SECTION TITLE */

.section-title {{
    color: #A855F7;
    font-size: 32px;
    font-weight: bold;
    margin-top: 35px;
    margin-bottom: 20px;
}}

/* DESCRIPTION */

.description {{
    color: #E2E8F0;
    font-size: 18px;
    line-height: 1.9;
}}

/* FEATURE BOX */

.feature-box {{
    background: rgba(30, 41, 59, 0.82);
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.3s ease;
}}

.feature-box:hover {{
    transform: translateY(-5px);
    box-shadow: 0 0 20px rgba(168, 85, 247, 0.4);
}}

/* FEATURE TITLE */

.feature-box h3 {{
    color: white;
    margin-bottom: 10px;
}}

/* FOOTER */

.footer {{
    text-align: center;
    color: #CBD5E1;
    margin-top: 50px;
    padding-bottom: 20px;
    font-size: 15px;
}}

/* MOBILE RESPONSIVE */

@media screen and (max-width: 768px) {{

    .hero-title {{
        font-size: 40px;
    }}

    .hero-subtitle {{
        font-size: 18px;
    }}

    .description {{
        font-size: 16px;
    }}

    .glass-card {{
        padding: 20px;
    }}

    .main-overlay {{
        padding: 20px;
    }}
}}

</style>
""", unsafe_allow_html=True)

# =========================================
# MAIN CONTENT
# =========================================

st.markdown('<div class="main-overlay">', unsafe_allow_html=True)

# HERO SECTION

st.markdown("""
<div class="hero-title">
    🛡️ About JobShield AI
</div>

<div class="hero-subtitle">
    Protecting Careers with Artificial Intelligence
</div>
""", unsafe_allow_html=True)

# GLASS CARD START

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# ABOUT DESCRIPTION

st.markdown("""
<div class="description">

Job hunting should feel exciting — not dangerous.

Every day, thousands of people apply for online jobs hoping to build successful careers and secure their future. However, hidden among legitimate opportunities are fraudulent job postings designed to scam users, steal personal information, and exploit job seekers.

<br><br>

<b>JobShield AI</b> was created to fight back.

<br><br>

JobShield AI is an advanced AI-powered fake job detection platform that uses Machine Learning and Natural Language Processing (NLP) to analyze job postings and identify suspicious patterns in real time.

<br><br>

The platform intelligently scans:

<ul>
<li>Job descriptions</li>
<li>Company information</li>
<li>Hiring language</li>
<li>Recruitment patterns</li>
<li>Suspicious wording</li>
</ul>

to determine whether a job opportunity appears legitimate or potentially fraudulent.

<br>

Inspired by modern AI platforms and cybersecurity systems, JobShield AI combines intelligent machine learning with a futuristic startup-style user experience.

</div>
""", unsafe_allow_html=True)

# FEATURES SECTION

st.markdown("""
<div class="section-title">
🚀 Core Features
</div>
""", unsafe_allow_html=True)

features = [

    (
        "🤖 AI-Powered Detection",
        "Uses Machine Learning and NLP models trained on real-world recruitment datasets to identify fraudulent job postings."
    ),

    (
        "📊 Smart Confidence Score",
        "Provides an intelligent AI confidence gauge to estimate scam probability and trust levels."
    ),

    (
        "⚡ Real-Time Analysis",
        "Instantly scans and analyzes pasted job descriptions with fast AI-driven predictions."
    ),

    (
        "🌌 Futuristic User Interface",
        "Designed with cinematic dark themes, neon glow effects, glassmorphism cards, and modern startup aesthetics."
    )
]

for title, desc in features:

    st.markdown(f"""
    <div class="feature-box">
        <h3>{title}</h3>
        <p class="description">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# TECHNOLOGIES SECTION

st.markdown("""
<div class="section-title">
🧠 Technologies Used
</div>

<div class="description">

• Python<br>
• Streamlit<br>
• Machine Learning<br>
• Natural Language Processing (NLP)<br>
• Scikit-learn<br>
• TF-IDF Vectorization<br>
• Plotly<br>
• GitHub<br>

</div>
""", unsafe_allow_html=True)

# FUTURE SECTION

st.markdown("""
<div class="section-title">
🔮 Future Vision
</div>

<div class="description">

JobShield AI is designed to evolve into a complete AI recruitment safety ecosystem capable of:

<ul>
<li>Detecting fake companies</li>
<li>Resume-job compatibility analysis</li>
<li>AI chatbot assistance</li>
<li>Cybersecurity threat visualization</li>
<li>User scan history</li>
<li>Live analytics dashboards</li>
<li>Advanced fraud detection systems</li>
</ul>

The mission is simple:

<br><br>

<b>Make online job searching safer for everyone.</b>

</div>
""", unsafe_allow_html=True)

# CLOSE GLASS CARD

st.markdown("</div>", unsafe_allow_html=True)

# FOOTER

st.markdown("""
<div class="footer">
Built with AI • NLP • Cybersecurity • Machine Learning
</div>
""", unsafe_allow_html=True)

# CLOSE MAIN OVERLAY

st.markdown("</div>", unsafe_allow_html=True)