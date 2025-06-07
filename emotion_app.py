import streamlit as st
from textblob import TextBlob
import base64

# ---- Function to set background from URL ----
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{image_url}');
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---- Set Custom Background ----
set_background("https://images.unsplash.com/photo-1531746790731-6c087fecd65a?auto=format&fit=crop&w=1350&q=80")

# ---- Title ----
st.markdown("<h1 style='text-align: center; color: white;'>Emotion Detection from Text</h1>", unsafe_allow_html=True)

# ---- Input ----
st.markdown("<h4 style='color:white;'>Enter your sentence:</h4>", unsafe_allow_html=True)
text = st.text_input("")

# ---- Detect Button ----
if st.button("Detect Emotion"):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    lower_text = text.lower()

    if any(word in lower_text for word in ["yay", "party", "picnic", "awesome", "excited"]):
        emotion = "Excited 😁"
    elif any(word in lower_text for word in ["angry", "hate", "annoyed", "frustrated"]):
        emotion = "Angry 😠"
    elif any(word in lower_text for word in ["boring", "not fun", "dull"]):
        emotion = "Bored 😒"
    elif polarity > 0.5:
        emotion = "Very Happy 😊"
    elif polarity > 0:
        emotion = "Happy 🙂"
    elif polarity == 0:
        emotion = "Neutral 😐"
    elif polarity > -0.5:
        emotion = "Sad 😟"
    else:
        emotion = "Very Sad 😢"

    st.markdown(f"<h3 style='color:white;'>Emotion: {emotion}</h3>", unsafe_allow_html=True)

