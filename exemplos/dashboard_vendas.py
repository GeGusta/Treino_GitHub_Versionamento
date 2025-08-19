import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Dashboard de Vendas")
st.markdown("---")

# Criando dados de exemplo mais realistas
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
categorias = ['Eletrônicos', 'Roupas', 'Livros', 'Casa', 'Esportes']
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']

# Gerando dados aleatórios
data = []
for date in dates:
    for _ in range(np.random.randint(5, 15)):  # 5-15 vendas por dia
        data.append({
            'data': date,
            'categoria': np.random.choice(categorias),
            'regiao': np.random.choice(regioes),
            'vendas': np.random.normal(1000, 300),
            'quantidade': np.random.randint(1, 10),
            'cliente_id': np.random.randint(1000, 9999)
        })

df = pd.DataFrame(data)
df['receita'] = df['vendas'] * df['quantidade']

# Sidebar para filtros
st.sidebar.title("🔍 Filtros")

# Filtro de data
date_range = st.sidebar.date_input(
    "Período",
    value=(df['data'].min(), df['data'].max()),
    min_value=df['data'].min(),
    max_value=df['data'].max()
)

# Filtro de categoria
categoria_filtro = st.sidebar.multiselect(
    "Categoria",
    options=categorias,
    default=categorias
)

# Filtro de região
regiao_filtro = st.sidebar.multiselect(
    "Região",
    options=regioes,
    default=regioes
)

# Aplicando filtros
if len(date_range) == 2:
    df_filtrado = df[
        (df['data'] >= pd.to_datetime(date_range[0])) &
        (df['data'] <= pd.to_datetime(date_range[1])) &
        (df['categoria'].isin(categoria_filtro)) &
        (df['regiao'].isin(regiao_filtro))
    ]
else:
    df_filtrado = df

# Métricas principais
st.subheader("📈 Métricas Principais")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Receita Total",
        f"R$ {df_filtrado['receita'].sum():,.0f}",
        f"{((df_filtrado['receita'].sum() / df['receita'].sum()) - 1) * 100:.1f}%"
    )

with col2:
    st.metric(
        "Vendas Totais",
        f"{len(df_filtrado):,}",
        f"{((len(df_filtrado) / len(df)) - 1) * 100:.1f}%"
    )

with col3:
    st.metric(
        "Ticket Médio",
        f"R$ {df_filtrado['receita'].mean():,.0f}",
        f"{((df_filtrado['receita'].mean() / df['receita'].mean()) - 1) * 100:.1f}%"
    )

with col4:
    st.metric(
        "Clientes Únicos",
        f"{df_filtrado['cliente_id'].nunique():,}",
        f"{((df_filtrado['cliente_id'].nunique() / df['cliente_id'].nunique()) - 1) * 100:.1f}%"
    )

# Gráficos
st.subheader("📊 Análise de Vendas")

# Gráfico 1: Evolução temporal
col1, col2 = st.columns(2)

with col1:
    # Receita por dia
    receita_diaria = df_filtrado.groupby('data')['receita'].sum().reset_index()
    fig_tempo = px.line(
        receita_diaria, 
        x='data', 
        y='receita',
        title='Evolução da Receita Diária'
    )
    fig_tempo.update_layout(height=400)
    st.plotly_chart(fig_tempo, use_container_width=True)

with col2:
    # Receita por categoria
    receita_categoria = df_filtrado.groupby('categoria')['receita'].sum().reset_index()
    fig_categoria = px.bar(
        receita_categoria,
        x='categoria',
        y='receita',
        title='Receita por Categoria',
        color='receita'
    )
    fig_categoria.update_layout(height=400)
    st.plotly_chart(fig_categoria, use_container_width=True)

# Gráfico 2: Análise por região
col1, col2 = st.columns(2)

with col1:
    # Receita por região
    receita_regiao = df_filtrado.groupby('regiao')['receita'].sum().reset_index()
    fig_regiao = px.pie(
        receita_regiao,
        values='receita',
        names='regiao',
        title='Distribuição de Receita por Região'
    )
    fig_regiao.update_layout(height=400)
    st.plotly_chart(fig_regiao, use_container_width=True)

with col2:
    # Heatmap categoria vs região
    pivot_table = df_filtrado.pivot_table(
        values='receita',
        index='categoria',
        columns='regiao',
        aggfunc='sum'
    ).fillna(0)
    
    fig_heatmap = px.imshow(
        pivot_table,
        title='Heatmap: Categoria vs Região',
        aspect='auto'
    )
    fig_heatmap.update_layout(height=400)
    st.plotly_chart(fig_heatmap, use_container_width=True)

# Análise detalhada
st.subheader("🔍 Análise Detalhada")

# Top produtos por categoria
st.write("### Top 5 Categorias por Receita")
top_categorias = df_filtrado.groupby('categoria')['receita'].sum().sort_values(ascending=False).head(5)
st.dataframe(top_categorias.reset_index())

# Análise de tendências
st.write("### Análise de Tendências")
col1, col2 = st.columns(2)

with col1:
    # Receita mensal
    df_filtrado['mes'] = df_filtrado['data'].dt.to_period('M')
    receita_mensal = df_filtrado.groupby('mes')['receita'].sum().reset_index()
    receita_mensal['mes'] = receita_mensal['mes'].astype(str)
    
    fig_mensal = px.line(
        receita_mensal,
        x='mes',
        y='receita',
        title='Receita Mensal'
    )
    st.plotly_chart(fig_mensal, use_container_width=True)

with col2:
    # Distribuição de vendas
    fig_dist = px.histogram(
        df_filtrado,
        x='receita',
        nbins=30,
        title='Distribuição de Receita por Venda'
    )
    st.plotly_chart(fig_dist, use_container_width=True)

# Tabela de dados
st.subheader("📋 Dados Detalhados")
st.dataframe(df_filtrado.head(100))

# Download dos dados
st.subheader("💾 Download dos Dados")
csv = df_filtrado.to_csv(index=False)
st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name=f"vendas_{datetime.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
)
