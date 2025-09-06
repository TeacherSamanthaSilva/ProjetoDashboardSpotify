import streamlit as st
import pandas as pd 

#Leitura da base de dados
df = pd.read_csv("cleaned_dataset.csv")


st.set_page_config(page_title="Spotify Songs", layout="wide")
# Supondo que 'df' é o DataFrame carregado

artists = df['Artist'].value_counts().index.tolist()
selected_artist = st.sidebar.selectbox('Escolha o artista:', artists)
st.bar_chart(data=df.set_index('Track')['Stream'])
df.set_index('Track', inplace=True)
# Supondo que 'df' é o DataFrame carregado
filtered_data = df[df['Artist'] == selected_artist]
display_graph = st.checkbox('Mostrar Gráfico')
if display_graph:
    st.bar_chart(filtered_data.set_index('Track')['Stream'])

#Exibindo o dataframe
st.write(df)
