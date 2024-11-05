import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv('Base_limpia.csv')

# CSS para ampliar el ancho del contenido y mostrar las métricas en una sola fila
st.markdown("""
    <style>
    .main .block-container {
        max-width: 100%;
        padding-top: 0; /* Quitar el espacio superior */
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .metric-container {
        display: flex;
        justify-content: flex-start;
        gap: 20px;
        flex-wrap: nowrap; /* Evitar que se vayan a una segunda fila */
    }
    .metric-box {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        color: white;
        font-family: sans-serif;
        width: 220px; /* Ancho fijo para que ocupen una fila */
        text-align: left;
    }
    .metric-title {
        font-size: 1rem;
        color: #ffa500;
        font-weight: bold;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Configuración del título del dashboard
st.title("Dashboard de Análisis del banco")

# Botones en la barra lateral
vista_general = st.sidebar.button("Vista General")
vista_filtrada = st.sidebar.button("Vista Filtrada")

# Vista General
if vista_general or not vista_filtrada:
    # Cuadros de métricas personalizados en una sola fila
    total_clientes = len(df)
    edad_promedio = f"{df['Edad'].mean():.1f}"
    balance_promedio = f"${df['Balance'].mean():,.2f}"
    tasa_retencion = f"{(1 - df['Salida'].mean()) * 100:.2f}%"

    st.markdown(f"""
        <div class="metric-container">
            <div class="metric-box">
                <div class="metric-title">Total de Clientes</div>
                <div class="metric-value">{total_clientes}</div>
            </div>
            <div class="metric-box">
                <div class="metric-title">Edad Promedio</div>
                <div class="metric-value">{edad_promedio}</div>
            </div>
            <div class="metric-box">
                <div class="metric-title">Balance Promedio</div>
                <div class="metric-value">{balance_promedio}</div>
            </div>
            <div class="metric-box">
                <div class="metric-title">Tasa de Retención</div>
                <div class="metric-value">{tasa_retencion}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Gráficos distribuidos en dos filas y cuatro columnas, alineados a la izquierda
    # Primera fila de gráficos
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        # Gráfico de Score Crediticio con los ajustes solicitados
        fig, ax = plt.subplots(figsize=(6, 5))

        # Histograma con colores diferenciados
        sns.histplot(df['CreditScore'], bins=30, kde=True, ax=ax, edgecolor="black", color="lightgray")
        for bar in ax.patches:
            # Colorea solo las barras dentro del rango [550, 750]
            if 550 <= bar.get_x() <= 750:
                bar.set_facecolor("#1e90ff")
            else:
                bar.set_facecolor("lightgray")  # Asegura que las barras fuera del rango queden en gris

        # Líneas punteadas rojas y más gruesas en los límites
        ax.axvline(550, color='red', linestyle='--', linewidth=2)
        ax.axvline(750, color='red', linestyle='--', linewidth=2)

        # Calcular porcentaje en el rango y desplazar el cuadro de texto
        en_rango = len(df[(df['CreditScore'] >= 550) & (df['CreditScore'] <= 750)])
        porcentaje = (en_rango / len(df)) * 100
        ax.text(0.3, 0.9, f"{porcentaje:.2f}% en el rango", transform=ax.transAxes,
                fontsize=12, color='black', ha='center', va='top',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        
        # Configuración de etiquetas y título
        ax.set_title("Score Crediticio")
        ax.set_xlabel("CreditScore")
        ax.set_ylabel("")
        ax.set_xticks([400, 500, 550, 600, 650, 700, 750, 800])

        st.pyplot(fig)

    
    with col2:
        # Gráfico de "Distribución por País" con colores de bandera, sin marco
        fig, ax = plt.subplots(figsize=(5, 4))
        
        colores_bandera = {
            'España': '#c60b1e',  # Rojo de la bandera de España
            'Francia': '#0055a4', # Azul de la bandera de Francia
            'Alemania': '#000000' # Negro de la bandera de Alemania
        }
        
        sns.countplot(data=df, x='Pais', ax=ax, palette=colores_bandera)
        ax.set_title("Distribución por País")
        ax.set_xlabel("")
        ax.set_ylabel("")

        # Quitar el marco
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        # Eliminar los valores del eje y
        ax.get_yaxis().set_visible(False)

        # Calcular el porcentaje de cada barra y agregar el valor dentro de cada barra
        total = len(df)
        for patch in ax.patches:
            height = patch.get_height()
            percentage = (height / total) * 100
            ax.text(patch.get_x() + patch.get_width() / 2, height / 2,
                    f'{percentage:.1f}%', ha='center', va='center', fontsize=14, color='white')

        st.pyplot(fig)
    
    with col3:
        # Gráfico de "Distribución por Género" sin marco y sin eje y
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(data=df, x='Genero', ax=ax, palette={'Mujer': '#ff1493', 'Hombre': '#1e90ff'})
        ax.set_title("Distribución por Género")
        ax.set_xlabel("")
        ax.set_ylabel("")
        
        # Eliminar el marco
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        
        # Eliminar los valores del eje y
        ax.get_yaxis().set_visible(False)

        # Calcular el porcentaje de cada barra y agregar el valor dentro de cada barra
        for patch in ax.patches:
            height = patch.get_height()
            percentage = (height / total) * 100
            ax.text(patch.get_x() + patch.get_width() / 2, height / 2,
                    f'{percentage:.1f}%', ha='center', va='center', fontsize=14, color='white')

        st.pyplot(fig)
    
    with col4:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.histplot(df['Edad'], bins=30, kde=True, color="green", ax=ax)
        ax.set_title("Distribución de Edad")
        st.pyplot(fig)

    # Segunda fila de gráficos
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(data=df, x='Salida', ax=ax, palette="Set2")
        ax.set_title("Clientes que han Realizado Churn")
        st.pyplot(fig)
    
    with col2:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(data=df, x='Quejas', ax=ax, palette="Set2")
        ax.set_title("Cantidad de Quejas por Cliente")
        st.pyplot(fig)
    
    with col3:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(data=df, x='#Prod', ax=ax, palette="Set2")
        ax.set_title("Cantidad de Productos por Cliente")
        st.pyplot(fig)
    
    with col4:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(data=df, x='TarjetaCredito', ax=ax, palette="Set2")
        ax.set_title("Clientes con Tarjeta de Crédito")
        st.pyplot(fig)

# Vista Filtrada
elif vista_filtrada:
    st.header("Vista Filtrada - Análisis Detallado")

    # Filtros en la barra lateral para la vista filtrada
    pais_seleccionado = st.sidebar.selectbox("Selecciona el país", df['Pais'].unique())
    genero_seleccionado = st.sidebar.selectbox("Selecciona el género", df['Genero'].unique())
    edad_seleccionada = st.sidebar.slider("Selecciona el rango de edad", 
                                          int(df['Edad'].min()), 
                                          int(df['Edad'].max()), 
                                          (int(df['Edad'].min()), int(df['Edad'].max())))

    # Filtrar el DataFrame con los criterios seleccionados
    df_filtrado = df[(df['Pais'] == pais_seleccionado) & 
                     (df['Genero'] == genero_seleccionado) & 
                     (df['Edad'] >= edad_seleccionada[0]) & 
                     (df['Edad'] <= edad_seleccionada[1])]

    # Panel General de la Vista Filtrada
    st.subheader("Estadísticas Generales")
    st.metric("Total de Clientes", len(df_filtrado))
    st.metric("Edad Promedio", f"{df_filtrado['Edad'].mean():.1f}")
    st.metric("Balance Promedio", f"${df_filtrado['Balance'].mean():,.2f}")
    st.metric("Tasa de Retención", f"{(1 - df_filtrado['Salida'].mean()) * 100:.2f}%")
