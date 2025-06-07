import streamlit as st
from textblob import TextBlob

st.title("Emotion Detection from Text")

text = st.text_input("Enter your sentence:")

if st.button("Detect Emotion"):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    # Keyword-based check
    angry_words = ["angry", "furious", "mad", "annoyed", "irritated"]
    rude_words = ["stupid", "idiot", "shut up", "nonsense", "dumb"]
    excited_words = ["excited", "amazing", "awesome", "thrilled", "yay", "can't wait"]
    bored_words = ["bored", "boring", "dull", "nothing to do", "meh"]

    # Emotion Detection
    if any(word in text_lower for word in rude_words):
        emotion = "Rude 😠"
    elif any(word in text_lower for word in angry_words):
        emotion = "Angry 😡"
    elif any(word in text_lower for word in excited_words):
        emotion = "Excited 😄"
    elif any(word in text_lower for word in bored_words):
        emotion = "Bored 😴"
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

    st.write("Emotion:", emotion)
