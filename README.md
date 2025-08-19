# Tutorial de Data Apps com Streamlit

O **Streamlit** é um framework open-source em Python que permite criar **aplicações de dados interativas** de forma simples e rápida.

---

## Comece em menos de 1 minuto

Instale o Streamlit como qualquer outra biblioteca Python:

```bash
pip install streamlit
```

E depois rode o comando de exemplo:

```bash
streamlit hello
```

---

## Os 3 princípios do Streamlit

### 1. **Abrace o scripting**

Crie um app em poucas linhas de código, com uma API super simples. Sempre que salvar o arquivo, ele atualiza automaticamente.

```python
# my_app.py
import streamlit as st
import pandas as pd

st.write("""
# Meu primeiro app
Olá *mundo!*
""")

df = pd.read_csv("meus_dados.csv")
st.line_chart(df)
```

⚡ Resultado: um Data App rodando em segundos.

---

### 2. **Traga interação**

Adicionar widgets é tão simples quanto declarar variáveis.
Você não precisa configurar backend, rotas, HTTP, frontend, HTML, CSS ou JS.

```python
number = st.slider("Escolha um número", 0, 100)
color = st.color_picker("Escolha uma cor")
date = st.date_input("Escolha uma data")
file = st.file_uploader("Envie um arquivo")
pet = st.radio("Escolha um pet", ["Cachorro", "Gato", "Pássaro"])
```

Você pode ainda gerar gráficos e interações com seus dados:

```python
import pandas as pd

df = pd.DataFrame({
    "categoria": list("ABCDEFGH"),
    "vendas": [10, 20, 30, 40, 50, 60, 70, 80]
})

st.bar_chart(df, x="categoria", y="vendas")
```

---

### 3. **Publique instantaneamente**

Você escolhe como disponibilizar seu Data App:

* **De graça** no [Streamlit Community Cloud](https://streamlit.io/cloud) (apps públicos).
* **Com confiabilidade corporativa** via Snowflake.
* Ou no ambiente que você preferir (Docker, servidores próprios, etc).

---

## Exemplos de apps incríveis feitos com Streamlit

* [Streamlit extras](https://github.com/arnaudmiribel/streamlit-extras)
* [Roadmap oficial](https://github.com/streamlit/roadmap)
* [Prettymapp](https://github.com/chrieke/prettymapp)
* [GW Quickview](https://github.com/jkanner/streamlit-quickview)
* [30 Days of Streamlit](https://github.com/streamlit/30days)
* [Streamlit ECharts Demo](https://github.com/andfanilo/streamlit-echarts-demo)

---

## Quem já usa Streamlit

> “É o próximo passo em ferramentas de ML e Data Science.” — **Dominik Moritz, Vega-Lite**
>
> “Streamlit democratiza a criação de Data Apps.” — **Koen Havlik, Uber**
>
> “Muito mais fácil de construir e iterar.” — **Danny Nguyen, Yelp**

E empresas como **Google X, Uber, Yelp, Stitch Fix** já utilizam Streamlit no dia a dia.

---

## Compatibilidade

Funciona praticamente com tudo do ecossistema Python:

* **Visualização**: Matplotlib, Plotly, Altair, Bokeh, Deck.GL, Vega-Lite
* **IA/ML**: TensorFlow, PyTorch, Scikit-learn, Keras
* **Dados**: Pandas, NumPy, OpenCV
* E muito mais, com [Streamlit Components](https://docs.streamlit.io/library/components).

---

## Conclusão

O Streamlit é uma forma rápida, simples e poderosa de transformar seus **scripts de Python em Data Apps interativos**.

Clone este repositório, rode os exemplos e crie seu primeiro Data App agora mesmo 🚀

---

👉 Luciano, quer que eu já monte a **estrutura inicial do repositório (README.md, requirements.txt e um exemplo `app.py`)** para você só dar o push no GitHub?
