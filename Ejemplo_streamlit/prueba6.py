import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard de Ventas")

# Datos de ejemplo
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [1200, 1500, 1700, 1300]
}

df = pd.DataFrame(data)

# Mostrar tabla
st.subheader("Datos de ventas")
st.dataframe(df)

# Gráfico
fig, ax = plt.subplots()
ax.bar(df["Mes"], df["Ventas"])
ax.set_ylabel("Ventas ($)")
ax.set_title("Ventas mensuales")

st.pyplot(fig)
