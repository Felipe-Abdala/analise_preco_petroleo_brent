import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
import requests
import pandas as pd
import numpy as np
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt


# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Tech Challenge Fase 4 | Grupo 59 | Imagem disponível em: vide bibliografia")

# Título Página
st.title('Conclusão')

coluna1, coluna2 = st.columns(2)
with coluna1:
    st.info('''######  Dentre as principais :blue[__causas econômicas__] para a Variação do Preço do Petróleo destacam-se as seguintes:''')
    st.write(''' 1. __Oferta e Demanda Global:__
    - A :blue[demanda global por petróleo] é altamente sensível ao crescimento econômico, especialmente nas economias avançadas e emergentes.
    - A oferta é influenciada pela :blue[capacidade de produção] dos principais países produtores, como Arábia Saudita, Rússia, Estados Unidos, e pela atuação da OPEP (Organização dos Países Exportadores de Petróleo).
2. __Geopolítica e Conflitos:__
    - :blue[Instabilidades políticas] e conflitos em regiões produtoras, como o Oriente Médio, têm impacto direto nos preços do petróleo. Exemplos:
        - Invasão do Kuwait pelo Iraque em 1990 (Guerra do Golfo).
        - Invasão do Iraque pelos EUA em 2003.
        - Sanções ao Irã devido ao programa nuclear.
3. __Decisões da OPEP:__
    - A OPEP atua para :blue[regular a produção de petróleo] entre seus membros, tentando estabilizar o mercado. Cortes ou aumentos na produção têm impacto direto nos preços.
4. __Avanços Tecnológicos:__
    - O :blue[desenvolvimento de novas tecnologias de extração], como o fracking e a exploração em águas profundas, alterou a dinâmica da oferta global.
    - A :blue[transição energética] para fontes renováveis também começa a exercer influência sobre a demanda futura de petróleo.
5. __Choques Econômicos:__
    - :blue[Crises econômicas globais] reduzem a demanda por petróleo. Exemplo:
    - A :blue[crise financeira] de 2008 reduziu drasticamente o preço do petróleo.
    - A :blue[pandemia de COVID-19] em 2020 levou a uma queda histórica na demanda, com os preços até ficando negativos em algumas circunstâncias.
6. __Taxa de Câmbio:__
    - O petróleo é precificado em dólares. :blue[Flutuações no valor do dólar] em relação a outras moedas afetam o preço do petróleo globalmente.''')

with coluna2:
    st.info(''' ######  Tais observações são corroboradas pelo :blue[__Modelo de Machine Learning__] utilizado, com o indicativo de: ''')
#    - A ''')
