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
    st.info('''######  Dentre as principais :blue[__causas econômicas__] para a Variação do Preço do Petróleo destacam-se as seguintes:''')
    st.write('''
        O modelo Prophet, utilizado para prever o preço do petróleo Brent, é uma ferramenta poderosa que traduz as flutuações do mercado de petróleo em previsões precisas. Este modelo não apenas fornece uma previsão numérica, mas também reflete de maneira robusta os impactos econômicos globais que moldam esses preços ao longo do tempo. Vamos entender como as métricas do modelo e as suas previsões se alinham com os eventos que influenciam o mercado de petróleo:

- Métricas de Avaliação do Modelo
             
As métricas de desempenho do Prophet revelam como o modelo captura de forma eficiente as tendências e as variações nos preços do petróleo:

- MAE (Erro Absoluto Médio): 8.82 USD

Em média, o modelo erra por apenas 8.82 USD nas suas previsões. Para um mercado altamente volátil como o do petróleo, esse erro é notavelmente baixo, o que demonstra a eficácia do modelo em prever com precisão, mesmo em horizontes temporais mais longos.

- MSE (Erro Quadrático Médio): 101.52 USD²

O MSE destaca a sensibilidade do modelo às grandes flutuações de preço. Durante eventos como crises econômicas ou mudanças políticas drásticas, o modelo consegue capturar essas variações intensas, embora penalize desvios mais pronunciados, como os vistos em eventos inesperados.

- RMSE (Raiz do Erro Quadrático Médio): 10.08 USD

O RMSE, derivado do MSE, nos dá uma visão clara da magnitude dos erros médios do modelo. Com um valor de 10.08 USD, o modelo é capaz de refletir com precisão os padrões gerais, mas ainda pode mostrar desvios durante momentos de instabilidade no mercado, como crises geopolíticas.

- MAPE (Erro Percentual Absoluto Médio): 11.46%

Essa métrica indica que as previsões do modelo estão, em média, a 11% do valor real. Em um mercado tão volátil quanto o do petróleo, esse índice é excelente, refletindo uma previsão de longo prazo bastante sólida, apesar das flutuações imprevisíveis.

- Acuracidade: 88.54%

Uma acuracidade de 88.54% demonstra que o modelo está acertando a maioria das suas previsões. Isso é particularmente relevante em um mercado de preços de petróleo, onde as condições externas podem mudar rapidamente e tornar a previsão desafiadora.    

            ''')
