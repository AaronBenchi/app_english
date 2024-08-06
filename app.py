# streamlit run apps.py
import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu

# Configuración de la página
st.set_page_config(page_title="Mi Aplicación", page_icon="🚀", layout="wide")

# Función para cargar la animación
def cargar_animacion(ruta_animacion):
    with open(ruta_animacion) as f:
        return json.load(f)

# Página de inicio con animación
def pagina_inicio():
    ruta_animacion = "animation/Animation - 1706587782829.json"
    animacion = cargar_animacion(ruta_animacion)
    st_lottie(animacion, speed=1, loop=True, quality="high")

# Crear un menú con diferentes pestañas
def crear_menu():
    with st.sidebar:
        selected = option_menu("App Navigation", ["Inicio", 
                                                  "App 1: Memorizar Inglés", 
                                                  "App 2: Eliminar Fondo", 
                                                  "App 3"], 
                               icons=['house', 
                                      'book', 
                                      'image', 
                                      'app'], 
                               menu_icon="cast", default_index=0)
    return selected

# Lógica principal
if __name__ == "__main__":
    selected = crear_menu()
    
    if selected == "Inicio":
        pagina_inicio()
    elif selected == "App 1: Memorizar Inglés":
        st.title("App 1: Memorizar Inglés")
        
        import pandas as pd
        import random
        import requests

        # Función para cargar datos desde Google Sheets
        def cargar_datos_google_sheets(sheet_id, sheet_name):
            url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
            return pd.read_csv(url)

        # Leer CSS
        with open("mi_estilo.css", "r") as f:
            css = f.read()

        # Renderizar los estilos CSS utilizando markdown
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

        # Función para obtener una palabra aleatoria
        def obtener_palabra_aleatoria():
            return df.sample(n=1)

        # Función para obtener la siguiente palabra en orden
        def obtener_palabra_secuencial(index):
            return df.iloc[[index % len(df)]]

        # Barra lateral
        st.sidebar.success("Escoge tu tarjeta")

        # Lista de tarjetas disponibles
        tarjetas = {
            "Tarjeta 1": "1O9vblqik8g99ZuQ3tugubDW6VyWnzk1pwMTjsXOla6I"
            # Puedes añadir más tarjetas aquí
        }

        # Seleccionar tarjeta
        tarjeta_seleccionada = st.sidebar.selectbox("Elige una tarjeta", list(tarjetas.keys()))

        if tarjeta_seleccionada:
            sheet_id = tarjetas[tarjeta_seleccionada]
            df = cargar_datos
