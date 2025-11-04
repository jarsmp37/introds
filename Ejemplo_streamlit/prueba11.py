import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

st.title("📊 Dashboard Interactivo de Ventas")

# Datos simulados
np.random.seed(1)
df = pd.DataFrame({
    "Ciudad": np.random.choice(["Puebla", "CDMX", "Guadalajara", "Monterrey"], 100),
    "Mes": np.random.choice(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"], 100),
    "Ventas": np.random.randint(500, 5000, 100)
})

# Sidebar con filtros
st.sidebar.header("Filtros")
ciudad = st.sidebar.selectbox("Selecciona una ciudad:", ["Todas"] + list(df["Ciudad"].unique()))
meses = st.sidebar.multiselect("Selecciona meses:", df["Mes"].unique(), default=df["Mes"].unique())

# Aplicar filtros
df_filtrado = df[df["Mes"].isin(meses)]
if ciudad != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Ciudad"] == ciudad]

# Layout de columnas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Datos filtrados")
    st.dataframe(df_filtrado)

with col2:
    st.subheader("Gráfico de ventas")
    fig = px.bar(df_filtrado, x="Mes", y="Ventas", color="Ciudad", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

# Métricas
st.markdown("---")
st.subheader("Resumen general")

total_ventas = df_filtrado["Ventas"].sum()
promedio = df_filtrado["Ventas"].mean()

col3, col4 = st.columns(2)
col3.metric("Total de ventas", f"${total_ventas:,.0f}")
col4.metric("Promedio de ventas", f"${promedio:,.2f}")
