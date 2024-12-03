import streamlit as st
import streamlit.components.v1 as components
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
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Tech Challenge Fase 4 | Grupo 59")

# Título Página
st.title('Referências bibliográficas')

#Lista com bibliografia
st.write('''- ¹ https://stackoverflow.com/questions/73677916/multiple-page-app-side-bar-icon-and-background-in-streamlit | data de acesso: 24/11/2024
- ² https://www.ipea.gov.br/desafios/index.php?option=com_content&view=article&id=2083:catid=28&Itemid=23 | data de acesso: 24/11/2024
- ³ https://guru.com.vc/glossario/brent/ | data de acesso: 24/11/2024
- https://blog.streamlit.io/introducing-multipage-apps/#tips-and-tricks | data de acesso: 24/11/2024
- https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ | data de acesso: 22/11/2024
- https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax | data de acesso: 29/11/2024
- https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png | data de acesso: 24/11/2024 
- https://images.pexels.com/photos/1716008/pexels-photo-1716008.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr | data de acesso: 24/11/2024 ''')
