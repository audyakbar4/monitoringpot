import streamlit as st
from auth import auth_menu
from streamlit_lottie import st_lottie
import requests

# ======= Page config =======
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# ======= CSS Styling =======
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://w.wallhaven.cc/full/76/wallhaven-76wydo.jpg');
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

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======= Session State Defaults =======
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ======= Authentication =======
if not st.session_state.logged_in:
    auth_menu()
else:
    # Header with Logout
    col1, col2 = st.columns([9, 1])
    with col2:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

    # === Hero Section ===
    st.markdown(
        """
        <div class='fade-in centered'>
            <h1 style='color:#00c7ff;'>Moodpot: Smart Emotion Plant</h1>
            <p style='font-size:18px;'>Inovasi pot tanaman interaktif dengan ekspresi wajah yang berubah sesuai kelembapan tanah.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # === Project Description ===
    st.markdown("## Deskripsi Proyek")
    st.markdown("""
    **Moodpot** adalah alat cerdas berbentuk pot tanaman yang menampilkan ekspresi wajah (senang/sedih) menggunakan **LED Matrix** berdasarkan **kadar kelembapan tanah**. Proyek ini dirancang untuk memberikan **umpan balik emosional** terhadap kondisi tanaman, menjadikan perawatan tanaman lebih **interaktif dan edukatif**.

    Komponen utama:
    - **Sensor Kelembapan Tanah**: Mengukur tingkat kelembapan secara real-time.
    - **LED Matrix 8x8**: Menampilkan ekspresi wajah tanaman.
    - **Arduino Uno**: Otak dari sistem.
    - **PCB Shield**: Menghilangkan kebutuhan kabel jumper.
    - **Monitoring UART**: Data dikirim ke komputer untuk pemantauan lebih lanjut.
    """)

    # === Features Section ===
    st.markdown("---")
    st.header("Fitur Utama Moodpot")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="fade-in feature-card">
            <h3>Interaksi Emosional</h3>
            <p>Wajah senang atau sedih muncul tergantung kondisi tanaman. Tanaman terlihat lebih "hidup".</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="fade-in feature-card">
            <h3>Monitoring Serial</h3>
            <p>Data dikirim via UART untuk analisis kelembapan secara digital dan logging.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="fade-in feature-card">
            <h3>Desain Tanpa Kabel</h3>
            <p>PCB shield khusus mengeliminasi kabel jumper, menjadikan sistem lebih rapi dan andal.</p>
        </div>
        """, unsafe_allow_html=True)

    # === Lottie Monitoring Preview ===
    st.markdown("---")
    st.subheader("Realtime Monitoring System")
    st.markdown("Moodpot dapat dikembangkan lebih lanjut untuk visualisasi kelembapan dalam bentuk grafik dan alert otomatis. Berikut gambaran monitoring sistemnya:")

    # === Future Development ===
    st.markdown("---")
    st.markdown("## Potensi Pengembangan")
    st.markdown("""
    - **Integrasi IoT** dengan WiFi untuk pemantauan via internet.
    - **Aplikasi Mobile** untuk alert dan kontrol ekspresi wajah.
    - **Notifikasi Otomatis** saat kelembapan turun di bawah ambang batas.
    - **Sensor Tambahan** seperti suhu atau cahaya untuk kecerdasan yang lebih tinggi.
    """)

    # === Footer ===
    st.markdown("---")
    st.info("Aplikasi ini dirancang oleh tim dengan semangat edukasi, teknologi, dan keberlanjutan . Dibuat menggunakan  Streamlit.")
