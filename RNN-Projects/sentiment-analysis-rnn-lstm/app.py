import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.main {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
}

h1 {
    text-align: center;
    color: #38bdf8;
}

textarea {
    border-radius: 10px !important;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 10px;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #6366f1, #38bdf8);
    transform: scale(1.03);
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------- LOAD MODEL -------------------
model = load_model("model.h5")
word_index = imdb.get_word_index()

# ------------------- TEXT ENCODING -------------------
def encode_text(text):
    words = text.lower().split()
    encoded = []
    for word in words:
        if word in word_index:
            encoded.append(word_index[word] + 3)
        else:
            encoded.append(2)
    return encoded

# ------------------- UI -------------------
st.markdown("<h1>🎬 AI Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.write("Analyze your movie reviews with Deep Learning 🤖")

user_input = st.text_area("✍️ Write your review here...", height=150)

if st.button("🚀 Analyze Sentiment"):
    if user_input.strip() != "":
        with st.spinner("Analyzing your review... 🔍"):
            encoded = encode_text(user_input)
            padded = pad_sequences([encoded], maxlen=200)

            prediction = model.predict(padded)[0][0]

        if prediction > 0.5:
            st.markdown(
                f'<div class="result-box" style="background-color:#064e3b;">😊 Positive Review<br>Confidence: {prediction:.2f}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="result-box" style="background-color:#7f1d1d;">😡 Negative Review<br>Confidence: {prediction:.2f}</div>',
                unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter a review first!")

# ------------------- FOOTER -------------------
st.markdown("""
<hr>
<p style='text-align: center; color: gray;'>
Made with ❤️ using LSTM & Streamlit
</p>
""", unsafe_allow_html=True)