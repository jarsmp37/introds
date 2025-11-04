import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Dashboard Avanzado", layout="wide")

st.title("📊 Dashboard Avanzado de Ventas")

# Simular datos
np.random.seed(42)
df = pd.DataFrame({
    "Ciudad": np.random.choice(["Puebla", "CDMX", "Guadalajara", "Monterrey"], 200),
    "Mes": np.random.choice(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"], 200),
    "Ventas": np.random.randint(500, 10000, 200)
})

# Filtros en sidebar
st.sidebar.header("Filtros")
ciudades = st.sidebar.multiselect("Selecciona ciudades:", df["Ciudad"].unique(), default=df["Ciudad"].unique())
meses = st.sidebar.multiselect("Selecciona meses:", df["Mes"].unique(), default=df["Mes"].unique())

df_filtrado = df[(df["Ciudad"].isin(ciudades)) & (df["Mes"].isin(meses))]

# KPIs
total_ventas = df_filtrado["Ventas"].sum()
promedio_ventas = df_filtrado["Ventas"].mean()
max_ventas = df_filtrado["Ventas"].max()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total de Ventas", f"${total_ventas:,.0f}")
col2.metric("📈 Promedio", f"${promedio_ventas:,.2f}")
col3.metric("🏆 Venta Máxima", f"${max_ventas:,.0f}")

# Gráfico principal
fig = px.bar(df_filtrado, x="Mes", y="Ventas", color="Ciudad", barmode="group",
             title="Ventas por Ciudad y Mes")
st.plotly_chart(fig, use_container_width=True)

# Gráfico secundario
fig2 = px.box(df_filtrado, x="Ciudad", y="Ventas", color="Ciudad", title="Distribución de Ventas por Ciudad")
st.plotly_chart(fig2, use_container_width=True)
