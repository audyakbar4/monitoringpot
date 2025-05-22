import streamlit as st
from check_auth import require_login
require_login()

# Load styling
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======= CSS Styling =======
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://w.wallhaven.cc/full/n6/wallhaven-n62ly6.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==== Header ====
st.markdown("""
<div class="fade-in centered">
    <h1>📬 Contact Us</h1>
    <p>Have a question, feedback, or collaboration idea?</p>
    <p>Let us know! We’d love to hear from you and grow together 🌱</p>
</div>
""", unsafe_allow_html=True)

# ==== Contact Info Box ====
st.markdown("""
<div class="feature-card fade-in" style="max-width: 600px; margin: 2rem auto;">
    <h3>💡 Project Inquiries</h3>
    <p>Email: <a href="mailto:moodpot.dev@gmail.com">moodpot.dev@gmail.com</a></p>
    <p>Instagram: <a href="https://instagram.com/moodpot.lab" target="_blank">@moodpot.lab</a></p>
    <p>Location: Surabaya, Indonesia 🌏</p>
</div>
""", unsafe_allow_html=True)

# ==== Contact Form ====
st.markdown("### ✍️ Send us a message")
with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("👤 Your Name")
    email = st.text_input("📧 Your Email")
    subject = st.text_input("📝 Subject")
    message = st.text_area("💬 Your Message")

    submitted = st.form_submit_button("📨 Send Message")

    if submitted:
        if not name or not email or not message:
            st.error("Please complete all required fields.")
        else:
            # Simulasi kirim (bisa integrasi ke Google Sheet, Email API, dsb)
            st.success(f"Thank you, {name}! Your message has been sent. We'll get back to you soon.")
