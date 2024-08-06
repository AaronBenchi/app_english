import streamlit as st
from gtts import gTTS
from io import BytesIO

def get_audio(text, lang='es', speed=1.0):
    # Crear el objeto de texto a voz
    tts = gTTS(text=text, lang=lang, slow=(speed < 1.0))
    
    # Guardar el archivo de audio en memoria
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    return audio_file

st.title("Texto a Voz con Streamlit")

# Entrada de texto
text = st.text_area("Introduce el texto que quieres convertir a voz:", "")

# Parámetros de configuración
lang = st.selectbox("Idioma", ["es", "en"])
speed = st.slider("Velocidad (0.5 - 2.0)", 0.5, 2.0, 1.0, 0.1)

if st.button("Generar Audio"):
    if text:
        audio_file = get_audio(text, lang, speed)
        st.audio(audio_file, format="audio/mp3")
    else:
        st.warning("Por favor, introduce un texto.")
