import pandas as pd
import streamlit as st
import plotly.express as px

"""Pelo menos um cabeçalho. Você pode usar [st.header()] para fazer isso. Na lição sobre aplicativos web, mostramos como criar um cabeçalho.
Um botão que, ao ser clicado, cria um histograma plotly-express. Para fazer isso, considere usar as funções st.write() e st.plotly_chart() (os materiais estão em inglês). Aqui está um exemplo de como você pode fazer isso:"""

df = pd.read_csv("datasets/vehicles.csv")
hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(df, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
