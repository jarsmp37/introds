import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Gráfica con Matplotlib")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
