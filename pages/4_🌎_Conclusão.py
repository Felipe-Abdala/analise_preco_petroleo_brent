import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
import plotly.express as px
import numpy as np

# SideBar e Filtros
st.sidebar.title('Filtros')
todos_anos = st.sidebar.checkbox('Dados de todo o período', value = True)
if todos_anos:
    ano = ''
else:
    ano = st.sidebar.slider('Ano', 1987, 2024)

# Título Página
st.title('Conclusão')

st.write('Oi!!')


# Abas ('Tabs')
aba1, aba2 = st.tabs(['Conclusão', 'Análise Macroeconômica'])
# aba1

