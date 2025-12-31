import pandas as pd
import streamlit as st
import plotly.express as px

"""Etapa 4. Desenvolver o dashboard do aplicativo web
Crie um arquivo app.py no diretório raiz do projeto. Para criar um arquivo .py, clique em "New File" (Novo arquivo) no VS Code e armazene-o no diretório do projeto com o nome desejado e a extensão .py.
Importe streamlit como st, pandas e plotly_express no início do arquivo.
Leia o arquivo CSV do conjunto de dados em um DataFrame. O código será o mesmo que você tinha no Jupyter Notebook ao explorar o conjunto de dados.
Agora, vamos criar o conteúdo do aplicativo baseado em Streamlit. Aqui está o que queremos que você inclua nele:
Pelo menos um cabeçalho. Você pode usar [st.header()] para fazer isso. Na lição sobre aplicativos web, mostramos como criar um cabeçalho.
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
