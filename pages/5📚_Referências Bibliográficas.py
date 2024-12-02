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

# Título Página
st.title('Referências bibliográficas')

#Lista com bibliografia
st.write('- https://stackoverflow.com/questions/73677916/multiple-page-app-side-bar-icon-and-background-in-streamlit | data de acesso: 24/11/2024')
st.write('- https://blog.streamlit.io/introducing-multipage-apps/#tips-and-tricks | data de acesso: 24/11/2024')
st.write('- https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ | data de acesso: 22/11/2024')
st.write('- https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax | data de acesso: 29/11/2024')



