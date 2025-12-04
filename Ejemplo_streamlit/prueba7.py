import streamlit as st
st.title("Ejemplo de Layouts en Streamlit")
# Sidebar
st.sidebar.header("Configuraciones")
nombre = st.sidebar.text_input("Nombre del usuario:")
mostrar_info = st.sidebar.checkbox("Mostrar información adicional")
# Columnas
col1, col2 = st.columns(2)
col1.write("Columna 1: puede contener texto, imágenes o gráficos.")
col2.write("Columna 2: útil para comparaciones o métricas.")
# Expander
with st.expander("Ver detalles"):
    st.write("Este texto está dentro de un expander y se puede ocultar.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=150)

if mostrar_info:
    st.success(f"Bienvenido, {nombre}! Has activado la opción de información adicional.")
