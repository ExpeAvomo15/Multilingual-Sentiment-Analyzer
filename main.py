import streamlit as st
import torch
from transformers import pipeline
import speech_recognition as sr
import tempfile
import os
from pydub import AudioSegment
from langdetect import detect

# Configuración inicial
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
st.title("🌍 Multilingual Sentiment Analyzer")
st.markdown("This app analyzes sentiment from text or voice in both English and Spanish.")

# Cargar modelo estable y público desde Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Idioma de interfaz
lang_option = st.selectbox("Choose your language / Elige tu idioma", ["English", "Español"])

# Entrada de texto
txt_input = st.text_area("Enter text to analyze / Escribe texto para analizar")

if st.button("Analyze Text"):
    if txt_input:
        try:
            detected_lang = detect(txt_input)
            result = sentiment_pipeline(txt_input)[0]
            label = result['label']
            score = result['score']

            color = "white"
            mood = "😐 Neutral"
            if "1" in label or "2" in label:
                color = "red"
                mood = "😠 Negative" if lang_option == "English" else "😠 Negativo"
            elif "3" in label:
                color = "yellow"
                mood = "😐 Neutral"
            elif "4" in label or "5" in label:
                color = "green"
                mood = "😊 Positive" if lang_option == "English" else "😊 Positivo"

            st.markdown(f"**Detected language**: {detected_lang.upper()}")
            st.markdown(f"**Sentiment**: <span style='color:{color}'>{mood} ({label}, {score:.2f})</span>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter some text.")

# Cargar archivo de audio
uploaded_audio = st.file_uploader("Upload an audio file (WAV or MP3)", type=["wav", "mp3"])

if st.button("Analyze Audio"):
    if uploaded_audio:
        try:
            audio_ext = os.path.splitext(uploaded_audio.name)[1].lower()
            with tempfile.NamedTemporaryFile(delete=False, suffix=audio_ext) as temp_input:
                temp_input.write(uploaded_audio.read())
                temp_input.flush()

                audio_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                if audio_ext == ".mp3":
                    sound = AudioSegment.from_mp3(temp_input.name)
                elif audio_ext == ".wav":
                    sound = AudioSegment.from_wav(temp_input.name)
                else:
                    st.error("❌ Unsupported audio format.")
                    raise ValueError("Unsupported format")

                sound.export(audio_wav.name, format="wav")

                recognizer = sr.Recognizer()
                with sr.AudioFile(audio_wav.name) as source:
                    audio = recognizer.record(source)
                    input_text = recognizer.recognize_google(audio)

            if input_text:
                st.markdown(f"**Transcription**: `{input_text}`")
                detected_lang = detect(input_text)
                result = sentiment_pipeline(input_text)[0]
                label = result['label']
                score = result['score']

                color = "white"
                mood = "😐 Neutral"
                if "1" in label or "2" in label:
                    color = "red"
                    mood = "😠 Negative" if lang_option == "English" else "😠 Negativo"
                elif "3" in label:
                    color = "yellow"
                    mood = "😐 Neutral"
                elif "4" in label or "5" in label:
                    color = "green"
                    mood = "😊 Positive" if lang_option == "English" else "😊 Positivo"

                st.markdown(f"**Detected language**: {detected_lang.upper()}")
                st.markdown(f"**Sentiment**: <span style='color:{color}'>{mood} ({label}, {score:.2f})</span>", unsafe_allow_html=True)
            else:
                st.warning("⚠️ Could not extract text from audio.")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please upload an audio file.")
