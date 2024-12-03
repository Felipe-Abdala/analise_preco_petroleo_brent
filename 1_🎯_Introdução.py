import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import plotly.graph_objects as go
import requests
import pandas as pd
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from math import sqrt
from sklearn.metrics import mean_absolute_error, mean_squared_error
#import plotly.express as px



#Configuração gerais das páginas
st.set_page_config(page_title='Pós-Tech FIAP | Tech Challenge Fase 4 | Grupo 59', page_icon=":chart_with_upwards_trend:", layout= 'wide')

# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM 354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Tech Challenge Fase 4 | Grupo 59 | Imagem disponível em: vide bibliografia")

# Página
st.header('Análise Preço Petróleo *Brent*')
st.markdown(' Pós-Tech FIAP Data Analytics | :blue[Tech-challenge Fase 4] | Grupo 59')

## Visualização no Streamlit
aba1, aba2 = st.tabs(['Introdução','Objetivos'])
with aba1:
	coluna1, coluna2 = st.columns(2)
	with coluna1:
		st.write('''#### Contextualização histórica''')
		st.write(''' Desde o advento da moderna indústria petrolífera no século XIX, o petróleo é uma das :blue[*commodities*] com grande impacto político e econômico desde então.''')
		st.write(''' Com o desenvolvimento do mercado internacional do petróleo, convencionou-se a organizá-lo a partir da :blue[cotação de 2 de seus tipos], sendo eles:
- *Brent*;
- WIT.''')
		st.write(''' O petróleo tem em sua formação de preço a influência de marcos :blue[geopolíticos, econômicos e socio-ambientais]. Portanto, sobre esses fatores que o presente estudo se volta para trazer no mínimo 4 *insights* sobre essas relações entre preço e eventos.''')

	with coluna2:
		st.image("https://images.pexels.com/photos/1716008/pexels-photo-1716008.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", caption="Mercado de petróleo. | Imagem disponível em: vide bibliografia")


with aba2:
	st.write('''#### Objetivos do estudo''')
	coluna1, coluna2 = st.columns(2)
	with coluna1:
		st.write('''- Analisar a :blue[flutuação do preço do petróleo] no intervalo temporal de :blue[1987 a 2024];
- Criar um :blue[dashboard interativo] parar gerar, no mínimo, :blue[4 *insights*] sobre a variação do preço do petróleo, envolvendo cenários geopolíticas, crises econômicas e demanda global por energia.
- Desenvolver um :blue[modelo de previsão para 90 dias].
- Executar com input do usário um :blue[modelo de Machine Learning] que preveja o preço do petróleo *Brent* diariamente;
- Criar um :blue[plano para fazer o deploy] em produção do modelo, com as ferramentas que são necessárias;
- :blue[Disponibilizar via Streamlit] o modelo em produção.''')

	with coluna2:
		st.image("https://media.licdn.com/dms/image/v2/D4D12AQHhGT2iS1QlLQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1670405199782?e=2147483647&v=beta&t=2Um0S28DuWFwpyxV-ybrjCURUJu2yueWKdR9HSuiuO0", caption="Modelos de Machine learning e cotação do Petróleo. | Imagem disponível em: vide bibliografia ")

