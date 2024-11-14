{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "05de7cd9-d869-443d-bc65-97c2fb896594",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-14 17:36:24.768 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\jafra\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st  \n",
    "import pandas as pd  \n",
    "import numpy as np  \n",
    "import time  \n",
    "\n",
    "# Configuración de la página  \n",
    "st.set_page_config(page_title=\"Monitoreo de Modelos ML\", layout=\"wide\")  \n",
    "\n",
    "# Título de la aplicación  \n",
    "st.title(\"Dashboard de Monitoreo de Modelos de Machine Learning\")  \n",
    "\n",
    "# Simulación de datos de métricas  \n",
    "def get_mock_data():  \n",
    "    # Generar datos aleatorios para la simulación  \n",
    "    timestamps = pd.date_range(start='2024-11-01', periods=30, freq='D')  \n",
    "    data = {  \n",
    "        'Fecha': timestamps,  \n",
    "        'Precisión': np.random.uniform(0.7, 1.0, size=len(timestamps)),  \n",
    "        'Recall': np.random.uniform(0.6, 1.0, size=len(timestamps)),  \n",
    "        'F1 Score': np.random.uniform(0.6, 1.0, size=len(timestamps)),  \n",
    "        'Alertas': np.random.choice(['OK', 'Alertas'], size=len(timestamps), p=[0.7, 0.3])  \n",
    "    }  \n",
    "    return pd.DataFrame(data)  \n",
    "\n",
    "# Obtener datos simulados  \n",
    "df = get_mock_data()  \n",
    "\n",
    "# Gráficos de métricas  \n",
    "st.subheader(\"Métricas del Modelo\")  \n",
    "st.line_chart(df.set_index('Fecha')[['Precisión', 'Recall', 'F1 Score']])  \n",
    "\n",
    "# Tabla de métricas  \n",
    "st.subheader(\"Resumen de Métricas\")  \n",
    "st.dataframe(df)  \n",
    "\n",
    "# Mostrar alertas  \n",
    "st.subheader(\"Alertas Recientes\")  \n",
    "alertas = df[df['Alertas'] == 'Alertas']  \n",
    "st.dataframe(alertas)  \n",
    "\n",
    "# Acción para simular una actualización de datos  \n",
    "if st.button('Actualizar Datos'):  \n",
    "    with st.spinner('Actualizando...'):  \n",
    "        time.sleep(1)  # Simulación de tiempo de espera por actualización  \n",
    "        df = get_mock_data()  # Actualiza los datos  \n",
    "        st.success(\"Datos actualizados\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
