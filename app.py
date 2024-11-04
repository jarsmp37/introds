import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título del Dashboard
st.title("Mi Dashboard en Streamlit")

# Cargar Datos
data = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valores': np.random.randint(1, 100, 4)
})

# Mostrar Datos en la Interfaz
st.subheader("Tabla de Datos")
st.dataframe(data)

# Crear un Gráfico de Barras
st.subheader("Gráfico de Barras")
fig, ax = plt.subplots()
ax.bar(data['Categoría'], data['Valores'], color='skyblue')
st.pyplot(fig)

# Botón para Actualizar
if st.button("Actualizar Datos"):
    data['Valores'] = np.random.randint(1, 100, 4)
    st.write("Datos actualizados.")
    st.dataframe(data)
