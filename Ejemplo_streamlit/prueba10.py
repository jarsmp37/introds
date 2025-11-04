import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Gráficos interactivos con Plotly")

# Datos
df = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
    "Ventas": [1200, 1500, 1700, 1300, 1800],
    "Región": ["Norte", "Sur", "Centro", "Norte", "Sur"]
})

# Gráfico de barras
fig = px.bar(df, x="Mes", y="Ventas", color="Región", title="Ventas por región y mes")
st.plotly_chart(fig, use_container_width=True)
