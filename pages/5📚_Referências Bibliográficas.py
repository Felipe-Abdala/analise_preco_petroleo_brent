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
st.title('Referências bibliográficas')

#Lista com bibliografia
st.write('- https://stackoverflow.com/questions/73677916/multiple-page-app-side-bar-icon-and-background-in-streamlit | data de acesso: 24/11/2024')
st.write('- https://blog.streamlit.io/introducing-multipage-apps/#tips-and-tricks | data de acesso: 24/11/2024')
st.write('- https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ | data de acesso: 22/11/2024')
st.write('- https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax | data de acesso: 29/11/2024')



