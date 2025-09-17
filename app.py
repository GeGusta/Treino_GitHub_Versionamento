import streamlit as st

st.markdown("# Salário em Dados ")

salario_pos = {
    "Júnior": 4000,
    "Pleno": 8500,
    "Sênior": 13000,
}

col1, col2 = st.columns(2)

with col1:
    select_box_posicao = st.selectbox("Senioridade", options=salario_pos.keys())

with col2:
    input_tempo_exp = st.number_input("Tempo de experiência", min_value = 0, max_value = 35, help = "Anos de experiência trabalhando")

salario = salario_pos[select_box_posicao] + (input_tempo_exp * 500)

st.markdown(f"## Salário: R$ {salario:,.2f}")   