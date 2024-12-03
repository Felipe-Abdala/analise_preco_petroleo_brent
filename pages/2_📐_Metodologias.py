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
    st.markdown(':blue[__Configuração da Requisiçãos__]: Foi usada a biblioteca requests para enviar solicitações HTTP. Os parâmetros da requisição incluem:')
    st.markdown('- __Produto:__ EPCBRENT (preço diário do Brent).')
    st.markdown('- __Data de início e fim:__ start_date e end_date.')
    st.markdown('- __Frequência:__ diária.')
    st.markdown('- __Paginação:__ A coleta foi implementada para lidar com paginação, permitindo extrair grandes volumes de dados, caso os resultados excedam o limite por requisição.')
    st.markdown('- __Estrutura dos Dados Recebidos:__ A API retorna os dados em formato JSON, contendo um campo chamado value, que corresponde ao preço do Brent em cada dia útil.')

