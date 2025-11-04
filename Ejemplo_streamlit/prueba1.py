import streamlit as st

# Título
st.title("Mi primera app con Streamlit")

# Texto
st.write("¡Hola! Esta es mi primera aplicación interactiva.")

# Mostrar datos
st.write("Puedes mostrar texto, números o incluso DataFrames:")
st.write({"Nombre": "Juan", "Edad": 22, "Ciudad": "Puebla"})