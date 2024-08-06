import streamlit as st
from elevenlabs import generate
from io import BytesIO

def get_audio(text, voice='Bella', speed=1.0):
    # Generar el audio con elevenlabs
    audio = generate(
        text=text,
        voice=voice,
        model='eleven_multilingual_v1',
        stability=0.75,
        similarity_boost=0.75
    )

    # Guardar el archivo de audio en memoria
    audio_file = BytesIO(audio)
    audio_file.seek(0)
    return audio_file

st.title("Texto a Voz con Streamlit")

# Entrada de texto
text = st.text_area("Introduce el texto que quieres convertir a voz:", "")

# Parámetros de configuración
voice = st.selectbox("Voz", ["Bella", "Domi", "Larry", "Rachel"])
speed = st.slider("Velocidad (0.5 - 2.0)", 0.5, 2.0, 1.0, 0.1)

if st.button("Generar Audio"):
    if text:
        audio_file = get_audio(text, voice, speed)
        st.audio(audio_file, format="audio/mp3")
    else:
        st.warning("Por favor, introduce un texto.")
