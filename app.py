import streamlit as st
import requests
from io import BytesIO

# Configura tu API key
API_KEY = "d8da938a8be28b4cc192033aa31d40c2"
API_URL = "https://api.elevenlabs.io/v1/text-to-speech"

def get_audio(text, voice='Bella', speed=1.0):
    # Configura los parámetros del audio
    headers = {
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY
    }
    payload = {
        "text": text,
        "voice": voice,
        "model_id": "eleven_multilingual_v1",
        "stability": 0.75,
        "similarity_boost": 0.75
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    response.raise_for_status()  # Verificar errores

    # Guarda el archivo de audio en memoria
    audio_file = BytesIO(response.content)
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
        try:
            audio_file = get_audio(text, voice, speed)
            st.audio(audio_file, format="audio/mp3")
        except requests.exceptions.RequestException as e:
            st.error(f"Error al generar el audio: {e}")
    else:
        st.warning("Por favor, introduce un texto.")
