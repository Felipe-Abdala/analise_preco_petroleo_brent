import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
import requests
import pandas as pd
import numpy as np
from datetime import date, timedelta
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt


st.header('Modelo interativo e resultados')

# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Tech Challenge Fase 4 | Grupo 59")

## Visualização no Streamlit
# Abas ('Tabs')
aba1, aba2 = st.tabs(['Modelo', 'Resultados e insights'])

# início - Aba 1 - Corpo da página
with aba1:
    st.markdown("Seguem abaixo as orientações para uso do modelo:")
    st.markdown("* Digite um **número inteiro** como a quantidade de :blue[dias] a ser previsto pelo modelo.")
    st.markdown("* Este **número inteiro** de dias deve ser entre :blue[1 e 90].")
    st.write("")
    st.write("")

    #Parâmetro
    prediction_days = st.number_input("Selecione a quantidade de dias que deseje que o modelo preveja", value=None, placeholder="Digite um número inteiro entre 1 e 90...", min_value=1, max_value=90, step = 1)

    st.success('Modelo executado com sucesso!', icon = "✅")

# Fim - Aba 1 - Corpo da página

# início - Aba 2 - Corpo da página
with aba2:
    st.markdown("   Com base na análise do modelo, identificamos que ... .")
    looker_studio_url = "https://lookerstudio.google.com/embed/reporting/d572c779-7cea-49cb-b82c-1b2d74d2c465/page/SaKXE"
    components.iframe(looker_studio_url, width=800, height=600)
# Fim - Aba 2 - Corpo da página
