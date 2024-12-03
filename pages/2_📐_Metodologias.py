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

# SideBar e Filtros
st.sidebar.title('Filtros')
todos_anos = st.sidebar.checkbox('Dados de todo o período', value = True)
if todos_anos:
    ano = ''
else:
    ano = st.sidebar.slider('Ano', 1987, 2024)



st.header('Metodologia')


## Visualização no Streamlit
# Abas ('Tabs')
aba1, aba2 = st.tabs(['Metodologia Machine Learning', 'Cenários Macroeconômicos'])
# aba1

with aba1:
    st.markdown('#### 1. Coleta de Dados')
    st.markdown(':blue[__Fonte dos Dados__]: Os dados foram extraídos da API da U.S. Energy Information Administration (EIA), que fornece informações detalhadas sobre preços de petróleo, incluindo o Brent.')
