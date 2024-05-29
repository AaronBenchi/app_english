# Ejecutar en la terminal streamlit run app4.py
import streamlit as st
import pandas as pd
import random
#from streamlit_extras.stylable_container import stylable_container # Estilo de los botones

# Leer el contenido del archivo CSS
with open("mi_estilo.css", "r") as f:
    css = f.read()
# Renderizar los estilos CSS utilizando markdown, para que me lo coja en toda la página
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)




# Función para obtener una palabra aleatoria
def obtener_palabra_aleatoria():
    return df.sample(n=1)

# Función para obtener una palabra aleatoria con prioridad en la frecuencia
def obtener_palabra_prioridad():
    frecuencia_prioritaria = random.randint(1, 3)
    palabras_con_prioridad = df[df['frecuencia'] == frecuencia_prioritaria]
    return palabras_con_prioridad.sample(n=1)

##### Barra lateral ##### 
st.sidebar.success("Escoge tu tarjeta")
subir_archivo = st.sidebar.file_uploader("Choose a CSV file")
if subir_archivo is not None:
    df = pd.read_csv(subir_archivo, sep=';', encoding='latin-1')
    # Imprimir tabla 
    #st.write(df)
##### Barra lateral ##### 


# INICIO WEB

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
        palabra_spelling = palabra_inicial['speling'].values[0]
        palabra_EN = palabra_inicial['palabra_EN'].values[0]
        palabra_ES = palabra_inicial['palabra_ES'].values[0]


        c1, c2, c3 = st.columns([7,7,2])
#maracador numero de palabras       
        with c1:
            # HTML para el marcador circular con la fracción
            maracador_html = f"""<div class="marcador-circular">{iteraciones + 1}/{max_iteraciones}</div>"""
            # Escribir el marcador circular en el contenedor
            st.markdown(maracador_html, unsafe_allow_html=True)
#Palabra en inglés
        with c2:
            st.write(f'<img src="https://icons.veryicon.com/png/Flag/Not%20a%20Patriot/USA%20Flag.png" width="20"> <span style="font-size: 16px; font-weight: bold;">{palabra_EN}</span>', unsafe_allow_html=True)                
#Pronunciación
        with c3:        
            st.write(f'<img src="https://definicion.de/wp-content/uploads/2011/06/pronunciacion-1.png" width="20"> {palabra_spelling}', unsafe_allow_html=True, align="right")


# AUDIO  
        # Llamada a la función para obtener la palabra inicial y su índice de fila
        indice_fila_palabra_inicial = df[df['palabra_EN'] == palabra_EN].index[0]
        ruta_audio = f"tarjeta1/audio_{indice_fila_palabra_inicial}.wav"
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

            col1, col2, col3 = st.columns([7,7,2])
            
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
    
    

