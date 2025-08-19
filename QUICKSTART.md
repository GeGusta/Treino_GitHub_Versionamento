# 🚀 Guia de Início Rápido

Este guia te ajudará a começar com o projeto **Data Apps com Streamlit** em menos de 5 minutos!

## ⚡ Instalação Rápida

### Opção 1: Script Automático (Recomendado)

```bash
# Clone o repositório
git clone <url-do-seu-repositorio>
cd data_apps_com_streamlit

# Execute o script de instalação
chmod +x install.sh
./install.sh
```

### Opção 2: Instalação Manual

```bash
# Clone o repositório
git clone <url-do-seu-repositorio>
cd data_apps_com_streamlit

# Instale as dependências
pip install -r requirements.txt
```

## 🎯 Primeiros Passos

### 1. App Principal (Tutorial Completo)
```bash
streamlit run app.py
```
- Tutorial interativo completo
- Demonstração de todos os widgets
- Visualizações avançadas
- Machine Learning
- Upload de arquivos

### 2. Exemplo Básico
```bash
streamlit run exemplos/exemplo_basico.py
```
- Implementação do exemplo do README
- Widgets básicos
- Gráficos simples

### 3. Dashboard de Vendas
```bash
streamlit run exemplos/dashboard_vendas.py
```
- Dashboard completo de vendas
- Filtros interativos
- Múltiplas visualizações

### 4. Machine Learning
```bash
streamlit run exemplos/ml_app.py
```
- Classificação e regressão
- Múltiplos algoritmos
- Avaliação de modelos

## 🎮 Script de Execução

Use o script interativo para escolher qual app executar:

```bash
python run_exemplos.py
```

## 📊 Dados de Exemplo

O projeto inclui dados de exemplo em `dados_exemplo/vendas.csv` que você pode usar para testar o upload de arquivos.

## 🔧 Configuração

### Ambiente Virtual (Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

### Configuração do Streamlit
O arquivo `.streamlit/config.toml` já está configurado com:
- Tema personalizado
- Configurações de servidor
- Otimizações de performance

## 🎨 Personalização

### Mudando o Tema
Edite `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

### Adicionando Novos Exemplos
1. Crie um novo arquivo em `exemplos/`
2. Adicione ao `run_exemplos.py`
3. Documente no README

## 🐛 Solução de Problemas

### Erro: "streamlit: command not found"
```bash
pip install streamlit
```

### Erro: "Module not found"
```bash
pip install -r requirements.txt
```

### Erro: "Port already in use"
```bash
streamlit run app.py --server.port 8501
```

## 📚 Próximos Passos

1. **Explore os exemplos** - Execute cada app para entender os conceitos
2. **Modifique o código** - Experimente alterar widgets e visualizações
3. **Crie seu próprio app** - Use os exemplos como base
4. **Compartilhe** - Publique no Streamlit Community Cloud

## 🔗 Links Úteis

- [Documentação Oficial](https://docs.streamlit.io/)
- [Comunidade](https://discuss.streamlit.io/)
- [Streamlit Community Cloud](https://streamlit.io/cloud)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

## 💡 Dicas

- **Hot Reload**: Salve o arquivo para ver mudanças instantaneamente
- **Widgets**: Use `st.sidebar` para organizar controles
- **Cache**: Use `@st.cache_data` para operações pesadas
- **Layout**: Use `st.columns()` para layouts responsivos

---

**Divirta-se criando Data Apps! 🎉**
