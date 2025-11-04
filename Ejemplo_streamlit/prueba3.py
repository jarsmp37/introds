import streamlit as st

st.title("Widgets interactivos")

# Entrada de texto
nombre = st.text_input("¿Cuál es tu nombre?")

# Selector numérico
edad = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=120, step=1)

# Desplegable
opcion = st.selectbox("Selecciona tu color favorito:", ["Rojo", "Verde", "Azul"])

# Botón
if st.button("Mostrar saludo"):
    st.success(f"¡Hola {nombre}! Tienes {edad} años y te gusta el color {opcion}.")
