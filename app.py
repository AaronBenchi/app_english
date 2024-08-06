import streamlit as st
from elevenlabs import ElevenLabs
from io import BytesIO

# Configura tu API key
client = ElevenLabs(api_key="d8da938a8be28b4cc192033aa31d40c2")

def get_audio(text, lang='es', speed=1.0):
    # Configura los parámetros del audio
    voice_params = {
        'text': text,
        'lang': lang,
        'speed': speed
    }

    # Llama a la API para generar el audio
    response = client.text_to_speech(**voice_params)
    
    # Guarda el archivo de audio en memoria
    audio_file = BytesIO(response.content)
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
