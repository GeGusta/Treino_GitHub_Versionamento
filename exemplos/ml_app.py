import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import make_classification, make_regression, load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(
    page_title="Machine Learning App",
    page_icon="🤖",
    layout="wide"
)

# Título
st.title("🤖 Machine Learning com Streamlit")
st.markdown("---")

# Sidebar para configurações
st.sidebar.title("⚙️ Configurações")

# Seleção do tipo de problema
tipo_problema = st.sidebar.selectbox(
    "Tipo de Problema",
    ["Classificação", "Regressão"]
)

# Seleção do dataset
if tipo_problema == "Classificação":
    dataset = st.sidebar.selectbox(
        "Dataset",
        ["Sintético", "Iris", "Breast Cancer"]
    )
else:
    dataset = st.sidebar.selectbox(
        "Dataset",
        ["Sintético"]
    )

# Carregando dados
@st.cache_data
def load_data(tipo, dataset_name):
    if tipo == "Classificação":
        if dataset_name == "Sintético":
            X, y = make_classification(
                n_samples=1000,
                n_features=20,
                n_informative=15,
                n_redundant=5,
                n_classes=2,
                random_state=42
            )
            feature_names = [f"Feature_{i}" for i in range(X.shape[1])]
        elif dataset_name == "Iris":
            iris = load_iris()
            X, y = iris.data, iris.target
            feature_names = iris.feature_names
        elif dataset_name == "Breast Cancer":
            cancer = load_breast_cancer()
            X, y = cancer.data, cancer.target
            feature_names = cancer.feature_names
    else:  # Regressão
        X, y = make_regression(
            n_samples=1000,
            n_features=20,
            n_informative=15,
            n_targets=1,
            random_state=42
        )
        feature_names = [f"Feature_{i}" for i in range(X.shape[1])]
    
    return X, y, feature_names

# Carregando dados
X, y, feature_names = load_data(tipo_problema, dataset)

# Informações sobre os dados
st.subheader("📊 Informações dos Dados")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Amostras", X.shape[0])
with col2:
    st.metric("Features", X.shape[1])
with col3:
    if tipo_problema == "Classificação":
        st.metric("Classes", len(np.unique(y)))
    else:
        st.metric("Targets", y.shape[1] if len(y.shape) > 1 else 1)

# Visualização dos dados
st.subheader("📈 Visualização dos Dados")

# Seleção de features para visualização
col1, col2 = st.columns(2)

with col1:
    if X.shape[1] >= 2:
        feat1 = st.selectbox("Feature X", feature_names, index=0)
        feat2 = st.selectbox("Feature Y", feature_names, index=1)
        
        idx1 = feature_names.index(feat1)
        idx2 = feature_names.index(feat2)
        
        if tipo_problema == "Classificação":
            fig = px.scatter(
                x=X[:, idx1],
                y=X[:, idx2],
                color=y,
                title=f"{feat1} vs {feat2}",
                labels={'x': feat1, 'y': feat2, 'color': 'Classe'}
            )
        else:
            fig = px.scatter(
                x=X[:, idx1],
                y=X[:, idx2],
                color=y,
                title=f"{feat1} vs {feat2}",
                labels={'x': feat1, 'y': feat2, 'color': 'Target'}
            )
        st.plotly_chart(fig, use_container_width=True)

with col2:
    # Distribuição do target
    if tipo_problema == "Classificação":
        fig = px.histogram(
            x=y,
            title="Distribuição das Classes",
            labels={'x': 'Classe', 'y': 'Frequência'}
        )
    else:
        fig = px.histogram(
            x=y,
            title="Distribuição do Target",
            labels={'x': 'Target', 'y': 'Frequência'}
        )
    st.plotly_chart(fig, use_container_width=True)

# Configuração do modelo
st.subheader("🎯 Configuração do Modelo")

# Parâmetros de treinamento
col1, col2 = st.columns(2)

with col1:
    test_size = st.slider("Tamanho do teste", 0.1, 0.5, 0.2, 0.05)
    random_state = st.number_input("Random State", value=42, min_value=0, max_value=1000)

with col2:
    cv_folds = st.number_input("Folds para Cross-Validation", value=5, min_value=2, max_value=10)
    use_scaling = st.checkbox("Usar StandardScaler", value=True)

# Seleção do modelo
if tipo_problema == "Classificação":
    modelo_nome = st.selectbox(
        "Modelo",
        ["Random Forest", "Logistic Regression", "SVM"]
    )
else:
    modelo_nome = st.selectbox(
        "Modelo",
        ["Random Forest", "Linear Regression", "SVR"]
    )

# Parâmetros específicos do modelo
st.write("### Parâmetros do Modelo")

if "Random Forest" in modelo_nome:
    col1, col2, col3 = st.columns(3)
    with col1:
        n_estimators = st.slider("Número de árvores", 10, 200, 100)
    with col2:
        max_depth = st.slider("Profundidade máxima", 3, 20, 10)
    with col3:
        min_samples_split = st.slider("Min samples split", 2, 20, 2)

# Botão para treinar
if st.button("🚀 Treinar Modelo"):
    with st.spinner("Treinando modelo..."):
        # Preparando dados
        if use_scaling:
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
        else:
            X_scaled = X
        
        # Dividindo dados
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=test_size, random_state=random_state
        )
        
        # Criando modelo
        if tipo_problema == "Classificação":
            if modelo_nome == "Random Forest":
                model = RandomForestClassifier(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    random_state=random_state
                )
            elif modelo_nome == "Logistic Regression":
                model = LogisticRegression(random_state=random_state)
            elif modelo_nome == "SVM":
                model = SVC(random_state=random_state)
        else:
            if modelo_nome == "Random Forest":
                model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    random_state=random_state
                )
            elif modelo_nome == "Linear Regression":
                model = LinearRegression()
            elif modelo_nome == "SVR":
                model = SVR()
        
        # Treinando modelo
        model.fit(X_train, y_train)
        
        # Predições
        y_pred = model.predict(X_test)
        
        # Métricas
        st.success("✅ Modelo treinado com sucesso!")
        
        # Resultados
        st.subheader("📊 Resultados")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if tipo_problema == "Classificação":
                accuracy = accuracy_score(y_test, y_pred)
                st.metric("Acurácia", f"{accuracy:.3f}")
                
                # Cross-validation
                cv_scores = cross_val_score(model, X_scaled, y, cv=cv_folds)
                st.metric("CV Score (média)", f"{cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
            else:
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)
                st.metric("MSE", f"{mse:.3f}")
                st.metric("R²", f"{r2:.3f}")
        
        with col2:
            if tipo_problema == "Classificação":
                # Matriz de confusão
                cm = confusion_matrix(y_test, y_pred)
                fig, ax = plt.subplots(figsize=(6, 4))
                sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
                ax.set_title('Matriz de Confusão')
                ax.set_xlabel('Predito')
                ax.set_ylabel('Real')
                st.pyplot(fig)
            else:
                # Gráfico de predições vs reais
                fig = px.scatter(
                    x=y_test,
                    y=y_pred,
                    title="Predições vs Valores Reais",
                    labels={'x': 'Valores Reais', 'y': 'Predições'}
                )
                fig.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], 
                                       y=[y_test.min(), y_test.max()], 
                                       mode='lines', name='Linha ideal'))
                st.plotly_chart(fig, use_container_width=True)
        
        # Relatório detalhado
        if tipo_problema == "Classificação":
            st.write("### Relatório de Classificação")
            st.text(classification_report(y_test, y_pred))
        
        # Feature importance (apenas para Random Forest)
        if "Random Forest" in modelo_nome:
            st.write("### Importância das Features")
            
            feature_importance = pd.DataFrame({
                'feature': feature_names,
                'importance': model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            fig = px.bar(
                feature_importance.head(10),
                x='importance',
                y='feature',
                title='Top 10 Features Mais Importantes'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Predições em tempo real
        st.subheader("🔮 Predições em Tempo Real")
        st.write("Insira valores para fazer uma predição:")
        
        # Criando inputs para features
        input_data = []
        col1, col2 = st.columns(2)
        
        for i, feature in enumerate(feature_names[:10]):  # Limitando a 10 features para não sobrecarregar
            if i % 2 == 0:
                with col1:
                    value = st.number_input(f"{feature}", value=0.0, step=0.1)
            else:
                with col2:
                    value = st.number_input(f"{feature}", value=0.0, step=0.1)
            input_data.append(value)
        
        # Completando com zeros se necessário
        while len(input_data) < len(feature_names):
            input_data.append(0.0)
        
        if st.button("🔮 Fazer Predição"):
            input_array = np.array(input_data).reshape(1, -1)
            
            if use_scaling:
                input_scaled = scaler.transform(input_array)
            else:
                input_scaled = input_array
            
            prediction = model.predict(input_scaled)[0]
            
            if tipo_problema == "Classificação":
                st.success(f"🎯 Predição: Classe {prediction}")
            else:
                st.success(f"🎯 Predição: {prediction:.3f}")

# Informações adicionais
st.markdown("---")
st.markdown("""
### 💡 Dicas:
- **Classificação**: Tente diferentes modelos para comparar performance
- **Regressão**: Observe o R² para avaliar a qualidade do modelo
- **Feature Importance**: Apenas disponível para Random Forest
- **Cross-Validation**: Use para uma avaliação mais robusta do modelo
""")
