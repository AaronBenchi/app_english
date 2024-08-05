# streamlit run apps.py

import streamlit as st
from streamlit_option_menu import option_menu

# Crear un menú con diferentes pestañas
with st.sidebar:
    selected = option_menu("App Navigation", ["App 1: Memorizar Inglés", 
                                              "App 2: Eliminar Fondo", 
                                              "App 3"], 
                           icons=['house', 
                                  'gear', 
                                  'kanban'], 
                                  
                           menu_icon="cast", default_index=0)

# Mostrar el contenido de cada pestaña
####
# APP 1
####
if selected == "App 1: Memorizar Inglés":
    st.title("App 1: Memorizar Inglés")
    st.write("App 1: Memorizar Inglés")
    
    # streamlit run app.py
    import os
    import streamlit as st
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

    ##### DECLARAR FUNCIONES #####
    # Función para obtener una palabra aleatoria
    def obtener_palabra_aleatoria():
        return df.sample(n=1)

    # Función para obtener una palabra aleatoria con prioridad en la frecuencia
    def obtener_palabra_prioridad():
        frecuencia_prioritaria = random.randint(1, 3)
        palabras_con_prioridad = df[df['frecuencia'] == frecuencia_prioritaria]
        
        # Verificar si hay al menos una fila en el DataFrame
        if not palabras_con_prioridad.empty:
            return palabras_con_prioridad.sample(n=1)
        else:
            # Si no hay filas, devolver None o algún valor predeterminado
            return None

    ##### Barra lateral #####
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
        df = cargar_datos_google_sheets(sheet_id, "Sheet1")
    ##### Barra lateral #####

    # INICIO WEB
    if tarjeta_seleccionada:
        # Configuración de la página
        st.title("Let's learn English Aaron")
        st.markdown("---")

        # Iteraciones máximas del usuario
        max_iteraciones = 15

        # Variable para contar las iteraciones
        iteraciones = st.session_state.get('iteraciones', 0)

        # Actualizar la información de la iteración y las palabras
        if iteraciones < max_iteraciones:
            palabra_inicial = obtener_palabra_prioridad()
            
            # Verificar si se obtuvo una palabra válida
            if palabra_inicial is not None:
                palabra_spelling = palabra_inicial['speling'].values[0]
                palabra_EN = palabra_inicial['palabra_EN'].values[0]
                palabra_ES = palabra_inicial['palabra_ES'].values[0]

                c1, c2, c3 = st.columns([7, 7, 2])
                # marcador número de palabras
                with c1:
                    # HTML para el marcador circular con la fracción
                    marcador_html = f"""<div class="marcador-circular">{iteraciones + 1}/{max_iteraciones}</div>"""
                    # Escribir el marcador circular en el contenedor
                    st.markdown(marcador_html, unsafe_allow_html=True)
                # Palabra en inglés
                with c2:
                    st.write(f'<img src="https://icons.veryicon.com/png/Flag/Not%20a%20Patriot/USA%20Flag.png" width="20"> <span style="font-size: 16px; font-weight: bold;">{palabra_EN}</span>', unsafe_allow_html=True)
                # Pronunciación
                with c3:
                    st.write(f'<img src="https://definicion.de/wp-content/uploads/2011/06/pronunciacion-1.png" width="20"> {palabra_spelling}', unsafe_allow_html=True, align="right")

                # AUDIO
                # Llamada a la función para obtener la palabra inicial y su índice de fila
                indice_fila_palabra_inicial = df[df['palabra_EN'] == palabra_EN].index[0]
                ruta_audio = f"https://github.com/AaronBenchi/app_english/blob/main/tarjeta1/audio_{indice_fila_palabra_inicial}.wav?raw=true"
                st.audio(ruta_audio, format="audio/wav", start_time=0, sample_rate=None)

                # Barra de progreso
                progreso = st.progress(iteraciones / max_iteraciones)

                # Botón para mostrar la traducción y la pregunta sobre la dificultad
                with st.expander("Mostrar"):
                    st.write(f'# {palabra_EN}')
                    st.write(f'# {palabra_ES}')

                    c1, c2 = st.columns([7, 7])
                    with c1:
                        st.markdown(f"#### Meaning: {palabra_inicial['Significado'].values[0]}")
                    with c2:
                        st.image(palabra_inicial['link_imagen'].values[0], caption='Foto', width=100)

                    st.write('¿Qué tan difícil fue para ti esta palabra?')

                st.markdown("---")
                # Actualizar frecuencia en función de la dificultad
                if iteraciones < max_iteraciones:
                    # Botones de dificultad
                    st.markdown('<p style="text-align:center;">DIFICULTAD</p>', unsafe_allow_html=True)

                    col1, col2, col3 = st.columns([7, 7, 2])

                    with col1:
                        facil_btn = st.button('Fácil')
                    with col2:
                        regular_btn = st.button('Regular')
                    with col3:
                        dificil_btn = st.button('Difícil')

                    if facil_btn:
                        df.loc[df['palabra_EN'] == palabra_EN, 'frecuencia'] = 1
                    elif regular_btn:
                        df.loc[df['palabra_EN'] == palabra_EN, 'frecuencia'] = 2
                    elif dificil_btn:
                        df.loc[df['palabra_EN'] == palabra_EN, 'frecuencia'] = 3

                    iteraciones += 1
                    st.session_state['iteraciones'] = iteraciones
                    progreso.progress(iteraciones / max_iteraciones)
        else:
            st.write("Finalizado con éxito")

####
# APP 2
####
elif selected == "App 2: Eliminar Fondo":
    st.title("App 2: Eliminar Fondo")
    st.write("App 2: Eliminar Fondo")
    
    # APP 2
    import streamlit as st
    from rembg import remove
    from PIL import Image
    import io
    import time
    
    st.title("Eliminador de Fondos de Imágenes")
    
    uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption="Imagen original", use_column_width=True)
    
        if st.button("Eliminar fondo"):
            progress_bar = st.progress(0)
            status_text = st.empty()
    
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
                status_text.text(f"Progreso: {i + 1}%")
    
            with st.spinner("Eliminando fondo..."):
                result_image = remove(image)
                st.success("Fondo eliminado")
    
            with col2:
                st.image(result_image, caption="Imagen sin fondo", use_column_width=True)
                
                buffer = io.BytesIO()
                result_image.save(buffer, format="PNG")
                buffer.seek(0)
        
                st.download_button(
                    label="Descargar imagen sin fondo",
                    data=buffer,
                    file_name="imagen_sin_fondo.png",
                    mime="image/png"
                )

####
# APP 3
####
elif selected == "App 3":
    st.title("App 3")
    st.write("Contenido de la App 3")
