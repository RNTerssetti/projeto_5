import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("datasets/vehicles.csv")
st.header('Análise de Anúncios de Vendas de Carros Usados')

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(df, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um grafico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.scatter(df, x="model_year", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)



build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_histogram: # se a caixa de seleção for selecionada

    st.write('Criando um histograma para a coluna model_year')

    fig = px.histogram(df, x="model_year")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: # se a caixa de seleção for selecionada

    st.write('Criando um gráfico de dispersão para as colunas model_year e price')

    fig = px.scatter(df, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
    