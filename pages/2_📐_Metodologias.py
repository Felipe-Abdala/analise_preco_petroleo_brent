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
    st.write('#### 1. Coleta de Dados')
    st.write('''- :blue[__Fonte dos Dados__]: Os dados foram extraídos da API da U.S. Energy Information Administration (EIA), que fornece informações detalhadas sobre preços de petróleo, incluindo o Brent.
- :blue[__Configuração da Requisiçãos__]: Foi usada a biblioteca requests para enviar solicitações HTTP. Os parâmetros da requisição incluem:
    - __Produto:__ EPCBRENT (preço diário do Brent).
    - __Data de início e fim:__ start_date e end_date.
    - __Frequência:__ diária.
    - __Paginação:__ A coleta foi implementada para lidar com paginação, permitindo extrair grandes volumes de dados, caso os resultados excedam o limite por requisição.
    - __Estrutura dos Dados Recebidos:__ A API retorna os dados em formato JSON, contendo um campo chamado value, que corresponde ao preço do Brent em cada dia útil.''')
    st.write('#### 2. Limpeza e Preparação dos Dados')
    st.write('''- :blue[__Transformação Inicial:__]
    - Os dados coletados foram armazenados em um DataFrame do pandas.
    - Colunas específicas foram renomeadas para o formato exigido pelo Prophet:
        - ds (datas).
        - y (valores a serem previstos).''')
    st.write('''- :blue[__Tratamento de Dados Ausentes:__] Foi implementado o preenchimento ou remoção de valores ausentes, garantindo que a série temporal não tenha lacunas que comprometam o modelo.')''')
    st.write('#### 3. Modelagem')
    st.write('''- :blue[__Inicialização do Modelo Prophet:__] O modelo Prophet foi configurado e ajustado aos dados de treino. Alguns parâmetros podem ter sido ajustados:
    - Sazonalidade:
        - Adição de sazonalidade padrão (diária, semanal ou anual), que o Prophet detecta automaticamente.
        - Configuração manual de sazonalidades específicas, se necessário.
    - Hiperparâmetros:
        - Intervalo de confiança padrão foi usado ou ajustado para maior precisão.''')
    st.write('#### 4. Validação e Avaliação')
    st.write('''- :blue[__Divisão dos Dados:__] Foi utilizada a validação cruzada com o módulo cross_validation do Prophet:
    - A série temporal foi dividida em intervalos de __treino__ e __teste__.
    - __Previsões__ foram realizadas para o conjunto de __teste__.
- :blue[__Métricas de Desempenho:__] As previsões foram avaliadas com métricas como:
   - MAE (Erro Médio Absoluto): mede o erro absoluto médio.
   - RMSE (Erro Quadrático Médio): avalia a magnitude do erro.
   - RAIZ(RMSE): fornece um valor interpretável para o erro médio em unidades reais.
- :blue[__Comparação com Modelos Alternativos:__] O modelo foi comparado com outros métodos de previsão, como média ou tendência linear, para verificar sua robustez.''')
    st.write('#### 5. Geração de Previsões')
    st.write('''- :blue[__Horizonte de Previsão:__] As previsões foram geradas para um horizonte futuro especificado pelo usuário (número de dias).
- :blue[__Intervalos de Confiança:__] Para cada previsão, o Prophet gerou intervalos de confiança que indicam a incerteza dos valores previstos.''')
