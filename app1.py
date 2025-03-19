import streamlit as st
import re

st.set_page_config(page_title="PASSWORD STRENGTH CHECKER BY ARSH ALI AZAM", page_icon="🪪", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/8c/7a/05/8c7a05d38cb7213b00c01b64a16d35df.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)


# st.header("🔐")
st.markdown("""
    <h2 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
               -webkit-background-clip: text;
               color: transparent;
               font-weight: bold;">
        Password🔑 strength checker!
    </h2>
    """, unsafe_allow_html=True)

st.markdown("""<p style='color: white;'>### Welcome to the ultimate password strength checker👋
            Use this simple tool to check the strength of your password and get suggestion on how to make it stronger.🔐
            We will give you helpful tips to create a **Strong Password** 🔐 style.</p>""", unsafe_allow_html=True)


# st.title("🔐Password strength checker")
# st.markdown(""" 
#             ### Welcome to the ultimate password strength checker👋
#             Use this simple tool to check the strength of your password and get suggestion on how to make it stronger.🔐
#             We will give you helpful tips to create a **Strong Password** 🔐""")

password = st.text_input("**🪷Enter your password**", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("✖️**Password should be at least 8 character long**.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌**Password should contain both upper and lower case characters**.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("⭕**Password Should contain at least one digit.**")

    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("🔴**Password Should contain at least one Special character(!@#$%&*)**") 

    if score == 4:
        feedback.append("💪**Your Password is Strong!**")               
    elif score == 3:
        feedback.append("❗**Your Password is Medium Strength. It could be stronger.**")
    else:
        feedback.append("🚫**Your Password is weak. Please make it stronger.**")

    if feedback:
        st.markdown("## 🟡Improvment Suggestion")
        for tip in feedback:
            st.write(tip)
else:
      st.info("**Please enter your password to get Started.**")












