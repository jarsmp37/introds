import streamlit as st

st.title("Ejemplo de pestañas en Streamlit")

tab1, tab2, tab3 = st.tabs(["Datos", "Gráficas", "Conclusiones"])

with tab1:
    st.write("Aquí puedes mostrar tablas o descripciones de datos.")

with tab2:
    st.line_chart({"Ventas": [100, 150, 200, 180, 220]})

with tab3:
    st.write("Conclusión: las ventas muestran una tendencia creciente con una ligera caída en el cuarto periodo.")
