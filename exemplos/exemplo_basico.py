import streamlit as st
import pandas as pd

# Título do app
st.write("""
# Meu primeiro app
Olá *mundo!*
""")

# Criando dados de exemplo
df = pd.DataFrame({
    "categoria": list("ABCDEFGH"),
    "vendas": [10, 20, 30, 40, 50, 60, 70, 80]
})

# Mostrando os dados
st.write("### Dados de Vendas")
st.dataframe(df)

# Criando um gráfico
st.write("### Gráfico de Vendas")
st.line_chart(df, x="categoria", y="vendas")

# Widgets interativos
st.write("### Interatividade")
number = st.slider("Escolha um número", 0, 100)
st.write(f"Você escolheu: {number}")

# Color picker
color = st.color_picker("Escolha uma cor")
st.write(f"Cor escolhida: {color}")

# Date input
date = st.date_input("Escolha uma data")
st.write(f"Data escolhida: {date}")

# File uploader
file = st.file_uploader("Envie um arquivo")
if file:
    st.write(f"Arquivo carregado: {file.name}")

# Radio buttons
pet = st.radio("Escolha um pet", ["Cachorro", "Gato", "Pássaro"])
st.write(f"Você escolheu: {pet}")

# Gráfico de barras
st.write("### Gráfico de Barras")
st.bar_chart(df, x="categoria", y="vendas")
