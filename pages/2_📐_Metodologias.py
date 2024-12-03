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
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Tech Challenge Fase 4 | Grupo 59")



st.header('Metodologia')


## Visualização no Streamlit
# Abas ('Tabs')
aba1, aba2 = st.tabs(['Metodologia Machine Learning', 'Cenários Macroeconômicos'])
# aba1


with aba1:
    st.write('''#### Metodologia do modelo de Machine Learning''')
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.info('''__1. Coleta de Dados__''')
        st.write('''- :blue[__Fonte dos Dados__]: Os dados foram extraídos da API da U.S. Energy Information Administration (EIA), que fornece informações detalhadas sobre preços de petróleo, incluindo o Brent.
- :blue[__Configuração da Requisiçãos__]: Foi usada a biblioteca requests para enviar solicitações HTTP. Os parâmetros da requisição incluem:
    - __Produto:__ EPCBRENT (preço diário do Brent).
    - __Data de início e fim:__ start_date e end_date.
    - __Frequência:__ diária.
    - __Paginação:__ A coleta foi implementada para lidar com paginação, permitindo extrair grandes volumes de dados, caso os resultados excedam o limite por requisição.
    - __Estrutura dos Dados Recebidos:__ A API retorna os dados em formato JSON, contendo um campo chamado value, que corresponde ao preço do Brent em cada dia útil.''')
        st.info(''' __2. Limpeza e Preparação dos Dados__''')
        st.write('''- :blue[__Transformação Inicial:__]
    - Os dados coletados foram armazenados em um DataFrame do pandas.
    - Colunas específicas foram renomeadas para o formato exigido pelo Prophet:
        - ds (datas).
        - y (valores a serem previstos).''')
        st.write('''- :blue[__Tratamento de Dados Ausentes:__] Foi implementado o preenchimento ou remoção de valores ausentes, garantindo que a série temporal não tenha lacunas que comprometam o modelo.')''')
        st.info(''' __3. Modelagem__''')
        st.write('''- :blue[__Inicialização do Modelo Prophet:__] O modelo Prophet foi configurado e ajustado aos dados de treino. Alguns parâmetros podem ter sido ajustados:
    - Sazonalidade:
        - Adição de sazonalidade padrão (diária, semanal ou anual), que o Prophet detecta automaticamente.
        - Configuração manual de sazonalidades específicas, se necessário.
    - Hiperparâmetros:
        - Intervalo de confiança padrão foi usado ou ajustado para maior precisão.''')
 
    with coluna2:
        st.info(''' __4. Validação e Avaliação__''')
        st.write('''- :blue[__Divisão dos Dados:__] Foi utilizada a validação cruzada com o módulo cross_validation do Prophet:
    - A série temporal foi dividida em intervalos de __treino__ e __teste__.
    - __Previsões__ foram realizadas para o conjunto de __teste__.''')
        st.write('''- :blue[__Métricas de Desempenho:__] As previsões foram avaliadas com métricas como:
    - MAE (Erro Médio Absoluto): mede o erro absoluto médio.
    - RMSE (Erro Quadrático Médio): avalia a magnitude do erro.
    - RAIZ(RMSE): fornece um valor interpretável para o erro médio em unidades reais.''')
        st.write('''- :blue[__Comparação com Modelos Alternativos:__] O modelo foi comparado com outros métodos de previsão, como média ou tendência linear, para verificar sua robustez.''')
        st.info(''' __5. Geração de Previsões__''')
        st.write('''- :blue[__Horizonte de Previsão:__] As previsões foram geradas para um horizonte futuro especificado pelo usuário (número de dias).
- :blue[__Intervalos de Confiança:__] Para cada previsão, o Prophet gerou intervalos de confiança que indicam a incerteza dos valores previstos.''')





with aba2:
    st.write('''#### Cenário Macroeconômico e Preço do Petróleo (1987 - 2024)''')
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.info(''':blue[__Década de 1980-1990__]: Estabilidade e Primeiro Choque''')
        st.write('''- Após a crise dos anos 1970, a década de 1980 viu preços mais estáveis, com o barril de petróleo oscilando entre 15-25 USD.
        - Em 1990, a Guerra do Golfo impulsionou os preços para cima, mas a rápida resolução do conflito estabilizou novamente o mercado.''')
        st.info(''' :blue[__Década de 1990__]: Baixa Volatilidade''')
        st.write('''- A década foi marcada por relativa estabilidade econômica global, mas a crise financeira asiática em 1997 reduziu temporariamente a demanda de petróleo.
        - O barril permaneceu em torno de 20-30 USD, com oscilações moderadas.''')
        st.info(''' :blue[__2000-2010__]: Alta Volatilidade e Crises''')
        st.write('''- A ascensão da China e de outras economias emergentes aumentou a demanda por petróleo, elevando os preços.
        - Em 2008, o preço do barril chegou a 140 USD, antes de despencar para menos de 40 USD com a crise financeira global.
        - A invasão do Iraque em 2003 também gerou picos de preços.''')

    with coluna2:
        st.info(''' :blue[__2020-2024__]: Pandemia, Recuperação e Geopolítica''')
        st.write('''- A pandemia de COVID-19 em 2020 gerou uma queda drástica na demanda e os preços chegaram a ficar negativos por questões logísticas.
    - A recuperação econômica pós-pandemia impulsionou os preços novamente para mais de 80 USD por barril.
    - A invasão da Ucrânia pela Rússia em 2022 elevou o preço do petróleo, devido a sanções econômicas e interrupções nas cadeias de suprimento de energia.
    - A transição energética global e o foco em energias renováveis começam a mudar a perspectiva de longo prazo da demanda por petróleo.''')
        st.info('''  :blue[__Tendências Futuras__]:''')
        st.write('''Transição energética: A busca por alternativas renováveis deve reduzir gradualmente a demanda global por petróleo.
        - Geopolítica e ESG: Conflitos em regiões produtoras e políticas ambientais de grandes economias continuarão a influenciar o mercado.
        - Influência da China e da Índia: As economias emergentes, particularmente China e Índia, continuarão sendo grandes impulsionadores da demanda de curto e médio prazo.''')
