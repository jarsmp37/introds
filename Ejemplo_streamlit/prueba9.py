import streamlit as st
import pandas as pd
import numpy as np

st.title("Filtros dinámicos con Streamlit")

# Datos de ejemplo
np.random.seed(0)
df = pd.DataFrame({
    "Ciudad": np.random.choice(["Puebla", "CDMX", "Monterrey"], size=30),
    "Ventas": np.random.randint(500, 5000, size=30),
    "Mes": np.random.choice(["Enero", "Febrero", "Marzo", "Abril"], size=30)
})

# Filtros
ciudad = st.selectbox("Selecciona una ciudad:", df["Ciudad"].unique())
mes = st.multiselect("Selecciona uno o varios meses:", df["Mes"].unique(), default=df["Mes"].unique())

# Aplicar filtros
df_filtrado = df[(df["Ciudad"] == ciudad) & (df["Mes"].isin(mes))]

st.write("### Datos filtrados:")
st.dataframe(df_filtrado)

# Gráfico
st.bar_chart(df_filtrado["Ventas"])
