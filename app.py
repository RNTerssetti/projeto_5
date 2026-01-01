import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Análise de Anúncios de Vendas de Carros Usados')
df = pd.read_csv("datasets/vehicles.csv")
hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(df, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada

    st.write('Criando um histograma para a coluna model_year')

    fig = px.histogram(df, x="model_year")
    fig2 = px.histogram(df, x="price")

    st.plotly_chart(fig, use_container_width=True)
    

st.header('Análise de Anúncios de Vendas de Carros Usados')