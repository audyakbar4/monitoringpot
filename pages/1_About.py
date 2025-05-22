import streamlit as st
from check_auth import require_login
require_login()

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======= CSS Styling =======
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://w.wallhaven.cc/full/4g/wallhaven-4ge28l.jpg');
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

# === ABOUT SECTION ===
st.markdown("""
<div class="fade-in centered">
    <h1>About Moodpot</h1>
    <p><strong>Moodpot</strong> adalah proyek inovatif yang dirancang untuk menggabungkan teknologi <em>embedded systems</em>, interaksi manusia-komputer, dan edukasi lingkungan dalam satu wadah yang menyenangkan dan fungsional.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Visi Kami")
st.markdown("""
<div class="fade-in" style="padding-bottom: 2rem;">
    <p>
    Membangun jembatan antara <strong>emosi digital</strong> dan <strong>perawatan tanaman</strong> melalui antarmuka ekspresif yang mudah diakses dan dapat dikembangkan lebih lanjut oleh siapa saja.
    </p>
</div>
""", unsafe_allow_html=True)

# === TIM KAMI ===
st.markdown("### Tim Pengembang")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="fade-in feature-card" style="margin-bottom: 2rem;">
        <h4>Embedded System Engineer</h4>
        <p>Bertanggung jawab atas pengolahan sinyal dari sensor kelembapan, pengendalian ekspresi LED matrix, dan stabilitas sistem Arduino.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="fade-in feature-card" style="margin-bottom: 2rem;">
        <h4>Software Developer</h4>
        <p>Membangun UI interaktif menggunakan Streamlit, autentikasi pengguna, dan sistem monitoring berbasis UART secara real-time.</p>
    </div>
    """, unsafe_allow_html=True)

# === LATAR BELAKANG TEKNOLOGI ===
st.markdown("### Teknologi di Balik Moodpot")
st.markdown("""
- **Sensor Kelembapan**: Untuk mendeteksi kondisi tanah secara akurat.
- **LED Matrix**: Menampilkan ekspresi senang/sedih sesuai kondisi tanaman.
- **Arduino Uno & PCB Shield**: Sistem mikroprosesor yang solid dan rapi tanpa kabel jumper.
- **UART Monitoring**: Menampilkan data langsung ke antarmuka desktop.
- **Streamlit**: Web framework berbasis Python untuk antarmuka interaktif dan modern.

> Semua elemen ini bersatu untuk menciptakan pengalaman interaktif yang menyenangkan dan edukatif.
""")

# === NILAI PROYEK ===
st.markdown("### Nilai Kami")
st.markdown("""
- **Edukasi**: Mengajarkan pentingnya perhatian terhadap tanaman secara menyenangkan.
- **Sustainability**: Mengedepankan kesadaran lingkungan melalui teknologi.
- **Interaktif**: Mengubah perawatan tanaman menjadi pengalaman emosional.
- **Terbuka untuk Pengembangan**: Siap dikembangkan untuk IoT, mobile apps, dan alert otomatis.
""")

# === PENUTUP ===
st.markdown("---")
st.success("Moodpot dibuat untuk masa depan yang lebih hijau dan terhubung.")
