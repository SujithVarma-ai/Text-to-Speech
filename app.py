import streamlit as st
from gtts import gTTS
import io
import time

# Configure the Streamlit page
st.set_page_config(
    page_title="AI Voice Synthesis",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Supported languages dictionary
LANGUAGES = {
    "English (US)": "en",
    "English (UK)": "en-uk",
    "English (Australia)": "en-au",
    "English (India)": "en-in",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Hindi": "hi",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Mandarin)": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar"
}

def inject_custom_css():
    """Injects custom CSS for a light theme with glassmorphism and modern styling."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        
        /* Global typography and background */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #1e293b;
        }
        
        /* Soft light background for the app */
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            color: #0f172a;
        }

        /* Hide the default top padding */
        .block-container {
            padding-top: 2rem;
            max-width: 800px;
        }

        /* Light Glassmorphism panel */
        .glass-panel {
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 1);
            padding: 2.5rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            margin-bottom: 1.5rem;
            animation: fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Typography styling */
        .gradient-title {
            background: linear-gradient(135deg, #4f46e5 0%, #0ea5e9 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            text-align: center;
            letter-spacing: -1px;
        }
        
        .subtitle {
            color: #64748b;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 400;
            margin-bottom: 2.5rem;
            letter-spacing: 0.5px;
        }

        /* Text Area styling */
        .stTextArea textarea {
            background-color: rgba(255, 255, 255, 0.9) !important;
            color: #0f172a !important;
            border: 1px solid rgba(203, 213, 225, 0.8) !important;
            border-radius: 16px !important;
            padding: 1.2rem !important;
            font-size: 1.1rem !important;
            line-height: 1.6 !important;
            transition: all 0.3s ease !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.02) !important;
        }
        .stTextArea textarea:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15), inset 0 2px 4px rgba(0,0,0,0.02) !important;
        }

        /* Stats text */
        .stats-text {
            display: flex;
            justify-content: flex-end;
            gap: 15px;
            color: #64748b;
            font-size: 0.85rem;
            margin-top: -15px;
            margin-bottom: 20px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stat-value {
            color: #334155;
        }

        /* Generate Button */
        .stButton button {
            background: linear-gradient(135deg, #4f46e5 0%, #0ea5e9 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 100px !important;
            padding: 0.8rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            letter-spacing: 0.5px !important;
            width: 100% !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 8px 20px rgba(79, 70, 229, 0.25) !important;
        }
        .stButton button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 12px 25px rgba(79, 70, 229, 0.35) !important;
        }
        .stButton button:active {
            transform: translateY(1px) !important;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: rgba(248, 250, 252, 0.95) !important;
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(226, 232, 240, 0.8);
        }
        [data-testid="stSidebar"] .css-17lntkn {
            color: #0f172a;
        }
        
        /* Selectbox styling in sidebar */
        .stSelectbox > div > div {
            background-color: white !important;
            color: #0f172a !important;
            border-radius: 8px !important;
            border: 1px solid rgba(203, 213, 225, 0.8) !important;
        }

        /* Audio element */
        audio {
            width: 100%;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            border-radius: 100px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            background: #ffffff;
        }
        
        /* Custom divider */
        hr {
            border-color: rgba(203, 213, 225, 0.5);
            margin: 2rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

def generate_audio(text, lang, speed):
    """Generates audio from text using gTTS and returns a BytesIO object."""
    try:
        tts = gTTS(text=text, lang=lang, slow=speed)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer
    except Exception as e:
        st.error(f"Error generating audio: {e}")
        return None

def main():
    inject_custom_css()

    # --- Sidebar Navigation & Settings ---
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        selected_lang_name = st.selectbox("🌐 Select Language", list(LANGUAGES.keys()))
        selected_lang_code = LANGUAGES[selected_lang_name]
        
        st.markdown("<br>", unsafe_allow_html=True)
        speed_option = st.radio("⏱️ Speech Speed", ["Normal", "Slow"])
        is_slow = speed_option == "Slow"
        
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.markdown(
            "This premium text-to-speech converter leverages **gTTS** to deliver "
            "natural-sounding voices. Built with Python and Streamlit."
        )
        st.markdown("<div style='margin-top: auto; padding-top: 20px; font-size: 0.8rem; color: #94a3b8;'>© 2026 AI Voice Studio</div>", unsafe_allow_html=True)

    # --- Main Content Area ---
    st.markdown("<div class='gradient-title'>AI Voice Studio</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Transform your text into lifelike speech in seconds</div>", unsafe_allow_html=True)

    # Wrap main interaction in a glassmorphism panel
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    # Input Area
    text_input = st.text_area("", placeholder="Type or paste your text here...", height=180, label_visibility="collapsed")
    
    # Character & Word Count
    words = len(text_input.split())
    chars = len(text_input)
    st.markdown(f"""
        <div class='stats-text'>
            <span>Words: <span class='stat-value'>{words}</span></span>
            <span>Chars: <span class='stat-value'>{chars}</span></span>
        </div>
    """, unsafe_allow_html=True)

    # Actions
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_btn = st.button("✨ Generate Audio")

    st.markdown("</div>", unsafe_allow_html=True) # End glass-panel

    # Handle Generation
    if generate_btn:
        if not text_input.strip():
            st.warning("⚠️ Please enter some text to generate audio.")
        else:
            with st.spinner("🎙️ Synthesizing voice..."):
                # Simulate a slight delay for smoother UI experience if generation is too fast
                time.sleep(0.5) 
                
                audio_buffer = generate_audio(text_input, selected_lang_code, is_slow)
                
                if audio_buffer:
                    st.success("✅ Audio generated successfully!")
                    
                    st.markdown("<div class='glass-panel' style='padding: 1.5rem;'>", unsafe_allow_html=True)
                    st.markdown("<h4 style='margin-bottom: 0; color: #0f172a;'>Playback</h4>", unsafe_allow_html=True)
                    
                    # Playback
                    st.audio(audio_buffer, format="audio/mp3")
                    
                    # Download
                    st.download_button(
                        label="⬇️ Download MP3",
                        data=audio_buffer,
                        file_name=f"ai_voice_{int(time.time())}.mp3",
                        mime="audio/mp3",
                        use_container_width=True
                    )
                    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
