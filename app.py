import streamlit as st
from elevenlabs import generate, play, save

def get_audio(text, lang='es', speed=1.0):
    # Definir el tono y la velocidad de la voz según el texto
    voice = "en_us_male"  # Cambia esto al ID de la voz que prefieras
    audio = generate(
        text=text,
        voice=voice,
        model="eleven_monolingual_v1",  # Modelo de voz
        speed=speed,
        language=lang
    )

    # Guardar el archivo de audio en memoria
    audio_file = BytesIO(audio)
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
        st.warning("Por favor, intr
