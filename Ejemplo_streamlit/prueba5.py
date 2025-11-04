import streamlit as st
import pandas as pd

st.title("Mostrar DataFrames")

data = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [23, 25, 22],
    "Ciudad": ["Puebla", "CDMX", "Monterrey"]
}

df = pd.DataFrame(data)
st.dataframe(df)
