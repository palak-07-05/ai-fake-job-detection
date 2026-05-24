import streamlit as st
import pickle
import time
import plotly.graph_objects as go
from database import add_user, login_user

# PAGE CONFIG

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide"
)

# SESSION

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# CUSTOM CSS

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #050816;
    color: white;
}

.stApp {
    background: linear-gradient(to bottom right, #050816, #0F172A);
}

/* LOGIN CARD */

.login-card {
    background: rgba(17, 24, 39, 0.8);
    padding: 40px;
    border-radius: 24px;
    margin-top: 60px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 30px rgba(124,58,237,0.35);
}

/* HERO */

.hero {
    text-align: center;
    padding-top: 30px;
    padding-bottom: 20px;
}

.hero-title {
    font-size: 70px;
    font-weight: bold;
    color: white;
}

.hero-subtitle {
    color: #94A3B8;
    font-size: 22px;
}

/* INPUT */

.stTextInput input {
    background-color: #111827;
    color: white;
    border-radius: 15px;
    border: 2px solid #7C3AED;
}

/* BUTTON */

.stButton button {
    background: linear-gradient(90deg, #7C3AED, #3B82F6);
    color: white;
    border-radius: 15px;
    height: 55px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

/* MAIN CARD */

.glass-card {
    background: rgba(17, 24, 39, 0.75);
    border-radius: 24px;
    padding: 35px;
    margin-top: 30px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 30px rgba(124,58,237,0.3);
}

.fake-text {
    color: #EF4444;
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}

.real-text {
    color: #10B981;
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}

.footer {
    text-align: center;
    color: #94A3B8;
    margin-top: 60px;
    padding-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# LOGIN / SIGNUP PAGE

if not st.session_state.logged_in:

    st.markdown("""
    <div class="hero">
        <div class="hero-title">🛡️ JobShield AI</div>
        <div class="hero-subtitle">
            AI-Powered Fake Job Detection Platform
        </div>
    </div>
    """, unsafe_allow_html=True)

    menu = ["Login", "Create Account"]

    choice = st.selectbox("Select Option", menu)

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # LOGIN

    if choice == "Login":

        if st.button("Login"):

            result = login_user(username, password)

            if result:

                st.success("Login Successful")

                st.session_state.logged_in = True
                st.rerun()

            else:

                st.error("Invalid Username or Password")

    # SIGNUP

    else:

        if st.button("Create Account"):

            add_user(username, password)

            st.success("Account Created Successfully")

            st.info("Go to Login Menu to Login")

    st.markdown('</div>', unsafe_allow_html=True)

# MAIN WEBSITE

else:

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    # LOGOUT

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    # HERO

    st.markdown("""
    <div class="hero">
        <div class="hero-title">🛡️ JobShield AI</div>
        <div class="hero-subtitle">
            AI-Powered Fake Job Detection Platform
        </div>
    </div>
    """, unsafe_allow_html=True)

    # INPUT

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    job_text = st.text_area(
        "Paste Job Description",
        height=250
    )

    analyze = st.button("Analyze with AI")

    st.markdown('</div>', unsafe_allow_html=True)

    # PREDICTION

    if analyze:

        if job_text.strip() == "":

            st.warning("Please enter a job description.")

        else:

            with st.spinner("Analyzing with AI..."):

                time.sleep(2)

                vector = vectorizer.transform([job_text])

                prediction = model.predict(vector)[0]

                probability = model.predict_proba(vector)[0]

                fake_score = probability[1] * 100
                real_score = probability[0] * 100

            st.markdown('<div class="glass-card">', unsafe_allow_html=True)

            if prediction == 1:

                st.markdown(
                    '<div class="fake-text">⚠️ Fake Job Detected</div>',
                    unsafe_allow_html=True
                )

                score = fake_score

            else:

                st.markdown(
                    '<div class="real-text">✅ Real Job Posting</div>',
                    unsafe_allow_html=True
                )

                score = real_score

            # AI GAUGE

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "AI Confidence Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#7C3AED"},
                    'bgcolor': "#111827",
                }
            ))

            fig.update_layout(
                paper_bgcolor="#111827",
                font={'color': "white"}
            )

            st.plotly_chart(fig, use_container_width=True)

            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
    Built with AI • NLP • Machine Learning
    </div>
    """, unsafe_allow_html=True)