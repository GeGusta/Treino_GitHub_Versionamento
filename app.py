import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="Data Apps com Streamlit - Tutorial",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🚀 Tutorial de Data Apps com Streamlit")
st.markdown("---")

# Sidebar com navegação
st.sidebar.title("📚 Navegação")
page = st.sidebar.selectbox(
    "Escolha uma seção:",
    ["🏠 Início", "📊 Exemplo Básico", "🎛️ Widgets Interativos", "📈 Visualizações", "🤖 Machine Learning", "📁 Upload de Arquivos"]
)

if page == "🏠 Início":
    st.header("Bem-vindo ao Tutorial de Streamlit!")
    
    st.markdown("""
    ### Os 3 princípios do Streamlit:
    
    1. **Abrace o scripting** - Crie apps em poucas linhas
    2. **Traga interação** - Widgets simples como variáveis
    3. **Publique instantaneamente** - Deploy fácil e rápido
    
    ---
    """)
    
    # Exemplo rápido
    st.subheader("⚡ Exemplo Rápido")
    col1, col2 = st.columns(2)
    
    with col1:
        st.code("""
import streamlit as st
import pandas as pd

st.write("# Meu primeiro app")
df = pd.read_csv("dados.csv")
st.line_chart(df)
        """, language="python")
    
    with col2:
        st.success("✅ Resultado: Data App rodando em segundos!")
        st.info("💡 Salve o arquivo e veja a atualização automática!")

elif page == "📊 Exemplo Básico":
    st.header("📊 Exemplo Básico - Dashboard de Vendas")
    
    # Criando dados de exemplo
    categorias = list("ABCDEFGH")
    vendas = [10, 20, 30, 40, 50, 60, 70, 80]
    
    df = pd.DataFrame({
        "categoria": categorias,
        "vendas": vendas
    })
    
    st.write("### Dados de Vendas por Categoria")
    st.dataframe(df)
    
    # Gráfico de barras
    st.write("### Gráfico de Barras")
    st.bar_chart(df, x="categoria", y="vendas")
    
    # Estatísticas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Vendas", f"R$ {df['vendas'].sum():,.0f}")
    with col2:
        st.metric("Média", f"R$ {df['vendas'].mean():.1f}")
    with col3:
        st.metric("Maior Venda", f"R$ {df['vendas'].max():,.0f}")

elif page == "🎛️ Widgets Interativos":
    st.header("🎛️ Widgets Interativos")
    
    st.write("### Adicionar widgets é tão simples quanto declarar variáveis!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Widgets Básicos")
        
        # Slider
        number = st.slider("Escolha um número", 0, 100, 50)
        st.write(f"Você escolheu: **{number}**")
        
        # Color picker
        color = st.color_picker("Escolha uma cor", "#ff0000")
        st.write(f"Cor escolhida: {color}")
        
        # Date input
        date = st.date_input("Escolha uma data", datetime.now())
        st.write(f"Data escolhida: {date}")
        
        # File uploader
        file = st.file_uploader("Envie um arquivo", type=['csv', 'xlsx', 'txt'])
        if file:
            st.success(f"Arquivo carregado: {file.name}")
    
    with col2:
        st.subheader("Widgets de Seleção")
        
        # Radio buttons
        pet = st.radio("Escolha um pet", ["🐕 Cachorro", "🐱 Gato", "🐦 Pássaro"])
        st.write(f"Você escolheu: {pet}")
        
        # Selectbox
        cidade = st.selectbox("Escolha uma cidade", ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"])
        st.write(f"Cidade escolhida: {cidade}")
        
        # Checkbox
        if st.checkbox("Mostrar informações extras"):
            st.info("Esta é uma informação extra que aparece quando você marca o checkbox!")
        
        # Multiselect
        frutas = st.multiselect("Escolha suas frutas favoritas", 
                               ["🍎 Maçã", "🍌 Banana", "🍊 Laranja", "🍓 Morango", "🍇 Uva"])
        if frutas:
            st.write("Suas frutas favoritas:", ", ".join(frutas))

elif page == "📈 Visualizações":
    st.header("📈 Visualizações Avançadas")
    
    # Criando dados mais complexos
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    data = pd.DataFrame({
        'data': dates,
        'vendas': np.random.normal(100, 20, 100).cumsum(),
        'lucro': np.random.normal(30, 5, 100).cumsum(),
        'categoria': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    st.write("### Dados de Vendas ao Longo do Tempo")
    
    # Plotly
    st.subheader("📊 Gráfico com Plotly")
    fig = px.line(data, x='data', y='vendas', title='Evolução das Vendas')
    st.plotly_chart(fig, use_container_width=True)
    
    # Gráfico de dispersão
    st.subheader("🎯 Gráfico de Dispersão")
    fig_scatter = px.scatter(data, x='vendas', y='lucro', color='categoria', 
                           title='Vendas vs Lucro por Categoria')
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Matplotlib/Seaborn
    st.subheader("📈 Gráfico com Matplotlib/Seaborn")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data, x='categoria', y='vendas', ax=ax)
    ax.set_title('Distribuição de Vendas por Categoria')
    st.pyplot(fig)
    
    # Gráfico de pizza
    st.subheader("🥧 Gráfico de Pizza")
    vendas_por_categoria = data.groupby('categoria')['vendas'].sum()
    fig_pie = px.pie(values=vendas_por_categoria.values, 
                    names=vendas_por_categoria.index,
                    title='Total de Vendas por Categoria')
    st.plotly_chart(fig_pie, use_container_width=True)

elif page == "🤖 Machine Learning":
    st.header("🤖 Machine Learning com Streamlit")
    
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report
    
    st.write("### Classificação com Random Forest")
    
    # Gerando dados
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, 
                             n_redundant=5, random_state=42)
    
    # Dividindo dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Parâmetros do modelo
    col1, col2 = st.columns(2)
    with col1:
        n_estimators = st.slider("Número de árvores", 10, 200, 100)
        max_depth = st.slider("Profundidade máxima", 3, 20, 10)
    
    with col2:
        if st.button("🚀 Treinar Modelo"):
            with st.spinner("Treinando modelo..."):
                # Treinando modelo
                model = RandomForestClassifier(n_estimators=n_estimators, 
                                             max_depth=max_depth, 
                                             random_state=42)
                model.fit(X_train, y_train)
                
                # Predições
                y_pred = model.predict(X_test)
                accuracy = accuracy_score(y_test, y_pred)
                
                # Resultados
                st.success(f"✅ Modelo treinado com sucesso!")
                st.metric("Acurácia", f"{accuracy:.3f}")
                
                # Relatório de classificação
                st.write("### Relatório de Classificação")
                st.text(classification_report(y_test, y_pred))
                
                # Feature importance
                feature_importance = pd.DataFrame({
                    'feature': [f'Feature {i}' for i in range(X.shape[1])],
                    'importance': model.feature_importances_
                }).sort_values('importance', ascending=False)
                
                st.write("### Importância das Features")
                fig = px.bar(feature_importance.head(10), x='importance', y='feature',
                           title='Top 10 Features Mais Importantes')
                st.plotly_chart(fig, use_container_width=True)

elif page == "📁 Upload de Arquivos":
    st.header("📁 Upload e Análise de Arquivos")
    
    st.write("### Faça upload de um arquivo CSV ou Excel para análise")
    
    uploaded_file = st.file_uploader(
        "Escolha um arquivo", 
        type=['csv', 'xlsx', 'xls'],
        help="Suporta arquivos CSV e Excel"
    )
    
    if uploaded_file is not None:
        try:
            # Detectando tipo de arquivo
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success(f"✅ Arquivo carregado com sucesso: {uploaded_file.name}")
            
            # Informações básicas
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Linhas", len(df))
            with col2:
                st.metric("Colunas", len(df.columns))
            with col3:
                st.metric("Tamanho", f"{uploaded_file.size / 1024:.1f} KB")
            
            # Visualização dos dados
            st.write("### Primeiras linhas dos dados")
            st.dataframe(df.head())
            
            # Informações sobre as colunas
            st.write("### Informações das colunas")
            st.dataframe(df.info())
            
            # Estatísticas descritivas
            if df.select_dtypes(include=[np.number]).columns.any():
                st.write("### Estatísticas descritivas")
                st.dataframe(df.describe())
            
            # Visualizações automáticas
            st.write("### Visualizações automáticas")
            
            # Selecionando colunas numéricas
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            
            if len(numeric_cols) > 0:
                col1, col2 = st.columns(2)
                
                with col1:
                    if len(numeric_cols) >= 1:
                        selected_col = st.selectbox("Escolha uma coluna para histograma", numeric_cols)
                        fig = px.histogram(df, x=selected_col, title=f'Distribuição de {selected_col}')
                        st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    if len(numeric_cols) >= 2:
                        col_x = st.selectbox("Coluna X", numeric_cols, index=0)
                        col_y = st.selectbox("Coluna Y", numeric_cols, index=1)
                        fig = px.scatter(df, x=col_x, y=col_y, title=f'{col_x} vs {col_y}')
                        st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.error(f"❌ Erro ao carregar arquivo: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🚀 Criado com <strong>Streamlit</strong> | 
    <a href='https://docs.streamlit.io/' target='_blank'>Documentação</a> | 
    <a href='https://discuss.streamlit.io/' target='_blank'>Comunidade</a></p>
</div>
""", unsafe_allow_html=True)
