# 🎙️ AI Voice Studio - Premium Text-to-Speech Converter

A modern, high-quality Web Application built with Python and Streamlit that converts text into natural-sounding speech using Google Text-to-Speech (gTTS).

![Project Banner](https://img.shields.io/badge/UI-Glassmorphism-a855f7?style=for-the-badge) ![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## ✨ Features

*   **Premium Interface:** Stunning dark mode UI featuring glassmorphism, sleek gradients, and smooth micro-animations.
*   **Global Reach:** Support for 15+ international languages and regional accents (English US/UK/AU/IN, Spanish, French, Japanese, Mandarin, etc.).
*   **Real-time Analytics:** Instant character and word counting as you type.
*   **Speech Control:** Adjustable speech speed (Normal / Slow).
*   **Direct Playback:** Listen to the generated audio directly within your browser.
*   **Instant Export:** Download the generated speech as high-quality MP3 files with a single click.
*   **Responsive Architecture:** Fully mobile-friendly and adapts seamlessly to any screen size.

## 📁 Project Structure

```text
text_to_speech_app/
│
├── app.py              # Main Streamlit application logic and UI code
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🚀 Quick Start & Deployment

### Local Development

1. **Clone the repository or navigate to the project folder:**
   ```bash
   cd text_to_speech_app
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   The application will automatically open at `http://localhost:8501`.

### ☁️ Cloud Deployment (Streamlit Community Cloud)

Deploying this app is extremely easy and free using Streamlit Community Cloud:

1. Push this project folder to a public or private **GitHub repository**.
2. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click on **"New app"**.
4. Select your GitHub repository, branch, and specify `app.py` as the Main file path.
5. Click **"Deploy"**.
6. Within minutes, your app will be live and accessible via a public URL!

## 🛠️ Technology Stack

*   **Frontend:** Streamlit, Vanilla CSS3 (Custom Injections)
*   **Backend:** Python 3
*   **Core Library:** `gTTS` (Google Text-to-Speech API)
