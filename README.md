# 🌍 Multilingual Sentiment Analyzer

This is a Streamlit-based web application that allows users to analyze the sentiment of a message — whether entered as text or uploaded as an audio file — in **English or Spanish**. The app uses a pre-trained Hugging Face transformer model to classify sentiment as **Positive**, **Neutral**, or **Negative**.

---

## 🚀 Features

- 🌐 Supports English and Spanish input.
- 📝 Analyze sentiment from written **text**.
- 🎙️ Analyze sentiment from **voice recordings** (MP3 or WAV).
- 🧠 Sentiment prediction powered by Hugging Face Transformers.
- 📊 Color-coded sentiment result: 
  - Green (Positive)
  - Yellow (Neutral)
  - Red (Negative)
- 🔊 Automatic transcription of uploaded audio using Google Speech Recognition.

---

## 📦 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Transformers (Hugging Face)](https://huggingface.co/transformers/)
- [Torch](https://pytorch.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pydub](https://github.com/jiaaro/pydub)
- [langdetect](https://pypi.org/project/langdetect/)

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/multilingual-sentiment-analyzer.git
cd multilingual-sentiment-analyzer
pip install -r requirements.txt
streamlit run main.py
