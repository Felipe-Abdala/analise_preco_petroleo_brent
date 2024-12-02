import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
import plotly.express as px
import numpy as np

#Configuração gerais das páginas
st.set_page_config(page_title='Pós-Tech FIAP | Tech Challenge Fase 4 | Grupo 59', page_icon=":chart_with_upwards_trend:", layout= 'wide')

# SideBar e Filtros
st.sidebar.title('Filtros')
todos_anos = st.sidebar.checkbox('Dados de todo o período', value = True)
if todos_anos:
    ano = ''
else:
    ano = st.sidebar.slider('Ano', 1987, 2024)

st.sidebar.image("https://i.scdn.co/image/ab6765630000ba8a9543f1ed639f9830d951f154", caption="Sunrise by the mountains")

# Página
st.header('Pós-Tech FIAP Data Analytics')
st.subheader(':blue[Fase 4] | Grupo 59', divider="gray")

st.caption("O mercado de petróleo e seus derivados traz consigo voluptuosas cifras e com enfoque em sua :blue[_produção_] e :blue[_comercialização_] que o presente trabalho se debruça.")

## Visualização no Streamlit
# Abas ('Tabs')
aba1, aba2 = st.tabs(['Introdução','Objetivos'])
# aba1





# The Google Looker Studio embed URL
#looker_studio_url = "https://lookerstudio.google.com/embed/reporting/2acfe271-c0ea-4bb2-bded-1835235ac236/page/tEnnC"
#looker_studio_url = "https://lookerstudio.google.com/embed/reporting/d572c779-7cea-49cb-b82c-1b2d74d2c465/page/SaKXE"
#components.iframe(looker_studio_url, width=800, height=600)

#<iframe width="600" height="450" src="xxx" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>
