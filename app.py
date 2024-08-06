import streamlit as st
from elevenlabs import ElevenLabs
from io import BytesIO

# Configura tu API key
api_key = "d8da938a8be28b4cc192033aa31d40c2"
client = ElevenLabs(api_key=api_key)

def get_audio(text, voice='Rachel', speed=1.0):
    # Genera el audio usando la API de ElevenLabs
    response = client.generate(
        text=text,
        voice=voice,
        speed=speed
    )
    
    # Guarda el archivo de audio en memoria
    audio_file = BytesIO(response.content)
    audio_file.seek(0)

    return audio_file

st.title("Texto a Voz con Streamlit")

# Entrada de texto
text = st.text_area("Introduce el texto que quieres convertir a voz:", "")

# Parámetros de configuración
voice = st.selectbox("Voz", ["Rachel", "Domi", "Bella", "Antoni", "Elli", "Josh", "Arnold"])
speed = st.slider("Velocidad (0.5 - 2.0)", 0.5, 2.0, 1.0, 0.1)

if st.button("Generar Audio"):
    if text:
        audio_file = get_audio(text, voice, speed)
        st.audio(audio_file, format="audio/mp3")
    else:
        st.warning("Por favor, introduce un texto.")
