import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Configuración del sidebar
st.sidebar.title("Menu")
st.sidebar.write("Filtros y opciones")

# Selección de vista
page = st.sidebar.radio("Selecciona una vista", ["Vista 1", "Vista 2", "Vista 3"])

# Filtros
st.sidebar.write("Seleccione rango de fechas:")
start_date = st.sidebar.date_input("Fecha de inicio", datetime(2023, 1, 1))
end_date = st.sidebar.date_input("Fecha de fin", datetime(2023, 12, 31))

st.sidebar.write("Seleccione categoría:")
category = st.sidebar.selectbox(
    "Categoría",
    ["Categoría A", "Categoría B", "Categoría C"]
)

# Título y estilo de fondo en la página principal
st.markdown(
    f"""
    <style>
    .main {{
        background-image: url("https://www.naukri.com/campus/career-guidance/what-is-data-science");
        background-size: cover;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Función para renderizar contenido según la página seleccionada
def render_page_content(page):
    if page == "Vista 1":
        st.title("Vista 1")
        # Gráfica de ejemplo
        fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 1, 2], name=category)])
        fig.update_layout(title_text="Gráfica de ejemplo")
        st.plotly_chart(fig)

    elif page == "Vista 2":
        st.title("Vista 2")
        # Otra gráfica de ejemplo
        fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[2, 4, 5], mode='lines', name='SF')])
        fig.update_layout(title_text="Otra gráfica de ejemplo")
        st.plotly_chart(fig)

    elif page == "Vista 3":
        st.title("Vista 3")
        st.write("Contenido adicional para esta vista.")

# Llamar a la función para renderizar el contenido de la página
render_page_content(page)

# Ejemplo de actualización de gráfico basado en los filtros seleccionados
st.write("Gráfica filtrada:")
filtered_fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 1, 2], name=category)])
filtered_fig.update_layout(title_text=f'Gráfica filtrada: {category}')
st.plotly_chart(filtered_fig)
