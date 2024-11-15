import streamlit as st  
import pandas as pd  
import numpy as np  
import time  

# Configuración de la página  
st.set_page_config(page_title="Monitoreo de Modelos ML", layout="wide")  

# Título de la aplicación  
st.title("Dashboard de Monitoreo de Modelos de Machine Learning")  

# Simulación de datos de métricas  
def get_mock_data():  
    # Generar datos aleatorios para la simulación  
    timestamps = pd.date_range(start='2024-11-01', periods=30, freq='D')  
    data = {  
        'Fecha': timestamps,  
        'Precisión': np.random.uniform(0.7, 1.0, size=len(timestamps)),  
        'Recall': np.random.uniform(0.6, 1.0, size=len(timestamps)),  
        'F1 Score': np.random.uniform(0.6, 1.0, size=len(timestamps)),  
        'Alertas': np.random.choice(['OK', 'Alertas'], size=len(timestamps), p=[0.7, 0.3])  
    }  
    return pd.DataFrame(data)  

# Obtener datos simulados  
df = get_mock_data()  

# Gráficos de métricas  
st.subheader("Métricas del Modelo")  
st.line_chart(df.set_index('Fecha')[['Precisión', 'Recall', 'F1 Score']])  

# Tabla de métricas  
st.subheader("Resumen de Métricas")  
st.dataframe(df)  

# Mostrar alertas  
st.subheader("Alertas Recientes")  
alertas = df[df['Alertas'] == 'Alertas']  
st.dataframe(alertas)  

# Acción para simular una actualización de datos  
if st.button('Actualizar Datos'):  
    with st.spinner('Actualizando...'):  
        time.sleep(1)  # Simulación de tiempo de espera por actualización  
        df = get_mock_data()  # Actualiza los datos  
        st.success("Datos actualizados") 
