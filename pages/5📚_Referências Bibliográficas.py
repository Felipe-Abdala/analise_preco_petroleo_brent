import streamlit as st
import streamlit.components.v1 as components
import plotly as plt
import plotly.express as px
import plotly.graph_objects as go
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import time
import datetime
from datetime import date, timedelta
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt
from streamlit_plotly_events import plotly_events
from IPython.display import display


#Configuração gerais das páginas
st.set_page_config(page_title='Pós-Tech FIAP | Tech Challenge Fase 4 | Grupo 59', page_icon=":chart_with_upwards_trend:", layout= 'wide')


# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Tech Challenge Fase 4 | Grupo 59")

# Título Página
st.title('Referências bibliográficas')
st.info('''__GitHub: repositório com o modelo e configurações Streamlit__''')
st.write('''- Disponível em: https://github.com/Felipe-Abdala/analise_preco_petroleo_brent/tree/main''')

st.info('''__Petróleo: eventos econômicos, históricos e políticos__''')
st.write('''- IPEA |  Disponível em: https://www.ipea.gov.br/desafios/index.php?option=com_content&view=article&id=2083:catid=28&Itemid=23 | Data de acesso: 24/11/2024
- Petróleo Brent | Disponível em: https://guru.com.vc/glossario/brent/ | Data de acesso: 24/11/2024''')

st.info('''__Bibliotecas e Ferramentas__''')
st.write('''- Prophet (Ferramenta de Previsão) | Disponível em: https://facebook.github.io/prophet/ | Data de acesso: 22/11/2024
- Scikit-learn (Machine Learning e Métricas) | Disponível em: https://scikit-learn.org/ | Data de acesso: 22/11/2024
- Plotly (Visualizações Interativas) | Disponível em: https://plotly.com/ | Data de acesso: 22/11/2024''')

st.info('''__Fonte de Dados: API da EIA (Energy Information Administration)__''')
st.write('''- Disponível em: https://www.eia.gov/opendata/ | Data de acesso: 22/11/2024''')


st.info('''__Fonte de imagens__''')
st.write('''-  Disponível em: https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png | Data de acesso: 22/11/2024
- Disponível em: https://media.licdn.com/dms/image/v2/D4D12AQHhGT2iS1QlLQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1670405199782?e=2147483647&v=beta&t=2Um0S28DuWFwpyxV-ybrjCURUJu2yueWKdR9HSuiuO0 | Data de acesso: 22/11/2024
- Disponível em: https://images.pexels.com/photos/1716008/pexels-photo-1716008.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1 | Data de acesso: 22/11/2024''')
st.info('''__Conceitos Estatísticos e Métricas: Erro Absoluto Médio (MAE), Erro Percentual Absoluto Médio (MAPE), Raiz do Erro Quadrático Médio (RMSE)__''')
st.write('''- Disponível em: https://otexts.com/fpp2/ | Data de acesso: 24/11/2024
- Disponível em: https://blog.streamlit.io/introducing-multipage-apps/#tips-and-tricks | Data de acesso: 24/11/2024
- Disponível em: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ | Data de acesso: 22/11/2024
- Disponível em: https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax | Data de acesso: 29/11/2024
- Disponível em: https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png | Data de acesso: 24/11/2024 
- Disponível em: https://images.pexels.com/photos/1716008/pexels-photo-1716008.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr | Data de acesso: 24/11/2024 ''')


