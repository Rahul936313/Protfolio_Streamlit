# app.py
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
from streamlit_lottie import st_lottie
import json
import requests

st.set_page_config(page_title="Rahul Singh Portfolio", page_icon="💻", layout="wide")

# 🎉 Animation effect (falling emojis)
#rain(emoji="💻", font_size=30, falling_speed=5, animation_length="infinite")

# Load Lottie Animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_4kx2q32n.json")

# Header with animation
colored_header(
    label="Rahul Singh",
    description="B.Tech CSE (AI & Data Science)",
    color_name="blue-70"
)

st.write("Passionate about Machine Learning, Web Development, and System Design.")

# Profile Image + Animation
col1, col2 = st.columns([1, 2])
with col1:
    st.image("assets/profile.jpg", width=200)
with col2:
    st_lottie(lottie_coding, height=250, key="coding")

# Resume
with open("Resume.docx", "rb") as docx_file:
    st.download_button("📄 Download Resume", docx_file, "Resume.docx")

st.divider()

# About Me
st.header("✨ About Me")
st.write("""
I am a B.Tech student specializing in AI & Data Science.  
I enjoy building end-to-end projects that combine machine learning with web deployment.  
Currently improving my software engineering skills and contributing to open-source projects.
""")

# Education
st.header("🎓 Education")
st.write("""
**B.Tech in Computer Science & Engineering (AI & Data Science)**  
Poornima University, Jaipur | 2024 – 2028
""")

# Skills
st.header("🛠️ Skills")
skills = ["Python", "C", "SQL", "HTML", "CSS", "Streamlit", "FastAPI", "Git", "MySQL", "Machine Learning"]
st.write(", ".join(skills))

# Projects
st.header("🚀 Projects")
st.markdown("""
- **Restaurant Billing System** → [GitHub](https://github.com/YOUR_GITHUB/Restaurant-billing-system-)  
- **Fake News Detector** → [GitHub](https://github.com/YOUR_GITHUB/fake-news-detector)  
- **Password Manager** → [GitHub](https://github.com/YOUR_GITHUB/Passward_manager)  
- **Portfolio Website** → [GitHub](https://github.com/YOUR_GITHUB/Protfolio-using-html-and-css.)
""")

# Certifications
st.header("🏆 Certifications and Badges")
st.markdown("""
- Microsoft Achievements → [Badges](https://learn.microsoft.com/en-us/users/rahulsingh-3798/transcript)
""")

st.markdown("""
- Google Skill Boost Achievements → [Badges](https://www.cloudskillsboost.google/public_profiles/ecac4ddb-bbd7-485b-a189-e642c2cf3128)
""")

# Hackathons
st.header("💡 Hackathons & Achievements")
st.write("""
- Smart India Hackathon 2025 — Participant  
- Solved 15+ problems on coding platforms  
- Active GitHub contributor
""")

# Contact
st.header("📬 Contact")
st.write("""
📧 **Email:** rsnr936313@gmail.com  
📱 **Phone:** +91-9460309339  
🌐 [GitHub](https://github.com/Rahul936313) | [LinkedIn](https://www.linkedin.com/in/rahul-singh-41303a323/)
""")

st.divider()
st.caption("✨ Made with ❤️ by Rahul Singh")
