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


st.header('Modelo interativo e resultados')

# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM 354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Tech Challenge Fase 4 | Grupo 59 | Imagem disponível em: vide bibliografia")

## Visualização no Streamlit
# Abas ('Tabs')
aba1, aba2 = st.tabs(['Modelo', 'Resultados e insights'])





# início - Aba 1 - Corpo da página
with aba1:
    st.info('''Digite abaixo a quantidade de dias, entre :blue[1 e 90], a fim de que o modelo preveja a cotação do preço do barril do Petróleo Brent.''')

    #Parâmetro
    prediction_days = st.number_input("", value=1, placeholder="Digite um nº inteiro entre 1 e 90 para Previsão do Modelo e tecle ENTER...", min_value=1, max_value=90, step = 1)
    
    st.divider()
    st.write('''#### Modelo de Machine Learning''')

    #Modelo
    # Configurações iniciais
    #st.status('''### :blue[__O Modelo está em execução__]: tempo estimado de 3 minutos''')
    st.warning(''' A execução do modelo tem o :blue[__tempo estimado em 5 minutos__]. Aguarde até a mensagem de :green[__"Concluído"__] aparecer no final da página. ''')
    api_key = "kjZJakW4UuR2fvPQPEoC5c1Ngyvfj96lnYUj9rcJ"
    start_date = "1987-05-25"
    end_date = "2024-11-30"
    #prediction_days = 30  # Altere para 30, 60 ou 90 conforme necessário

    # Coleta de dados da API
    url = "https://api.eia.gov/v2/petroleum/pri/spt/data/"
    params = {
        'api_key': api_key,
        'facets[product][]': 'EPCBRENT',
        'data[]': 'value',
        'frequency': 'daily',
        'start': start_date,
        'end': end_date,
        'offset': 0
    }

    all_data = []
    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and 'data' in data['response']:
                brent_data = data['response']['data']
                all_data.extend(brent_data)
                if len(brent_data) < 5000:
                    break
                params['offset'] += 5000
            else:
                raise ValueError("Erro: Nenhum dado encontrado na resposta.")
        else:
            raise ConnectionError(f"Erro na requisição: Status Code {response.status_code}")

    raw_data = pd.DataFrame(all_data)
    raw_data = raw_data[['period', 'value']].rename(columns={'period': 'ds', 'value': 'y'})
    raw_data['ds'] = pd.to_datetime(raw_data['ds'])
    raw_data['y'] = pd.to_numeric(raw_data['y'], errors='coerce')
    raw_data = raw_data.dropna()

    #st.write("Total de registros coletados:", len(raw_data))
    # Separação de treino e teste
    train = raw_data.iloc[:-prediction_days]
    test = raw_data.iloc[-prediction_days:]

    # Treinamento do modelo
    model = Prophet()
    model.fit(train)

    future = model.make_future_dataframe(periods=prediction_days)
    forecast = model.predict(future)
    forecast_filtered = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(prediction_days)

    # Cálculo de métricas
    y_true = test['y'].values
    y_pred = forecast_filtered['yhat'].values

    non_zero_mask = y_true != 0
    y_true = y_true[non_zero_mask]
    y_pred = y_pred[non_zero_mask]

    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = sqrt(mse)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    accuracy = 100 - mape


    #Métricas
    st.info('''##### Métricas do Modelo''')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        col1.write(f'''##### :blue[__MAE__]
                {mae:.2f}''')
    with col2:
        col2.write(f'''##### :blue[__MSE__]
                {mse:.2f}''')
    with col3:
        col3.write(f'''##### :blue[__RMSE__]
                {rmse:.2f}''')
    with col4:
        col4.write(f'''##### :blue[__MAPE__]
                {mape:.2f}%''')
    with col5:
        col5.write(f'''##### :blue[__Accuracy__]
                {accuracy:.2f}%''')
        



    col1, col2, col3, col4 = st.columns(4)
    with col1:
        col1.write(f'''##### :blue[__Total registros__]
                {len(raw_data)}''')
    with col2:
        start_date_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        col2.write(f'''##### :blue[__Data início: histórico__]
                {start_date_dt}''')
    with col3:
        end_date_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        col3.write(f'''##### :blue[__Data fim: histórico__]          
                {end_date_dt}''')
    with col4:
        data_a_prever = datetime.datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=prediction_days)
        data_a_prever_dt = data_a_prever.strftime("%d/%m/%Y")
        col4.write(f'''##### :blue[__Data previsão__]          
                {data_a_prever_dt}''')
    st.divider()

    # Validação cruzada
    df_cv = cross_validation(model, initial='730 days', period='180 days', horizon=f"{prediction_days} days")
    performance = performance_metrics(df_cv)
    st.info('''##### Métricas da Validação Cruzada e da previsão dos dias selecionados''')
    st.write("###### Tabela com as métricas da validação cruzada")
    st.write(performance)

    # Exibindo a tabela diretamente
    # Filtrar a previsão para os últimos prediction_days
    forecast_table = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(prediction_days)

    # Renomear colunas para algo mais amigável
    forecast_table = forecast_table.rename(columns={
        'ds': 'Data',
        'yhat': 'Previsão',
        'yhat_lower': 'Limite Inferior',
        'yhat_upper': 'Limite Superior'
    })

    # Exibindo a tabela
    display(forecast_table)
    st.write("###### Tabela com previsão dos dias selecionados com os limites")
    st.write(forecast_table)


    # Visualização interativa
    fig = go.Figure()

    # Adicionar os dados históricos
    fig.add_trace(go.Scatter(
        x=raw_data['ds'], 
        y=raw_data['y'], 
        mode='lines', 
        name='Histórico',
        line=dict(color='blue', dash='solid')  # Linha sólida para histórico
    ))

    # Adicionar previsão
    fig.add_trace(go.Scatter(
        x=forecast['ds'], 
        y=forecast['yhat'], 
        mode='lines', 
        name='Previsão', 
        line=dict(dash='dot', color='orange')  # Linha pontilhada para previsão
    ))

    # Adicionar limites de confiança
    fig.add_trace(go.Scatter(
        x=forecast['ds'], 
        y=forecast['yhat_upper'], 
        mode='lines', 
        name='Limite Superior', 
        line=dict(color='rgba(204, 204, 204, 0.6)'),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=forecast['ds'], 
        y=forecast['yhat_lower'], 
        mode='lines', 
        name='Limite Inferior', 
        line=dict(color='rgba(204, 204, 204, 0.6)'),
        fill='tonexty',
        fillcolor='rgba(204, 204, 204, 0.3)',
        showlegend=True
    ))

    # Linha de início da previsão
    start_date = raw_data['ds'].iloc[-prediction_days]
    fig.add_vline(x=start_date, line=dict(color="red", dash="dash"), name="Início da Previsão")

    fig.update_layout(
        title="Previsão do Preço do Petróleo Brent",
        xaxis_title="Data",
        yaxis_title="Preço Brent (USD)",
        legend_title="Legenda",
        template="plotly_white"
    )

    st.divider()
    st.info('''##### Exibição gráfica do modelo de *machine learnig*''')
    plotly_events(fig)


st.success('Modelo executado com sucesso!', icon = "✅")

#SALVAR EM CSV
data_as_csv = forecast_table.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download base de dados como CSV", 
    data_as_csv, 
    "Modelo_ML_Brent.csv",
    "text/csv",
    key="download-tools-csv",
)

# Fim - Aba 1 - Corpo da página

# início - Aba 2 - Corpo da página
with aba2:
    looker_studio_url = "https://lookerstudio.google.com/embed/reporting/d572c779-7cea-49cb-b82c-1b2d74d2c465/page/SaKXE"
    components.iframe(looker_studio_url, width=800, height=600)

# Fim - Aba 2 - Corpo da página
