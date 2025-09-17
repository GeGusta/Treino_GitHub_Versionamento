# 📊 Projeto de Previsão de Salário - Data App com Streamlit

Este projeto foi desenvolvido durante a **live do canal Jornada de Dados** ([assista aqui](https://www.youtube.com/live/TMtjnQ4sPTE)) e demonstra como criar um **Data App completo** para previsão de salários na área de dados usando **Streamlit**.

## 🎯 Sobre o Projeto

Este é um sistema de **Machine Learning** que prevê faixas salariais para profissionais de dados baseado em características como:
- Idade
- Gênero
- Localização (UF)
- Cargo atual
- Nível de senioridade
- Tempo de experiência em dados
- Tempo de experiência em TI

O projeto inclui tanto o **modelo de ML** quanto uma **interface web interativa** criada com Streamlit.

## 🚀 Como Funciona

### 1. **Modelo de Machine Learning** (`train.py`)
- Utiliza dados reais da comunidade de dados brasileira
- Implementa técnicas de **feature engineering** e **imputação de dados**
- Treina um modelo de classificação para prever faixas salariais
- Usa **scikit-learn** e **feature-engine** para o processamento

### 2. **Data App Interativo** (`app.py`)
- Interface web criada com **Streamlit**
- Permite ao usuário inserir suas informações
- Retorna a previsão de faixa salarial em tempo real
- Interface intuitiva e responsiva

## 📁 Estrutura do Projeto

```
data_apps_com_streamlit/
├── app.py              # Data App com Streamlit
├── train.py            # Script de treinamento do modelo
├── data/
│   └── dataset.csv     # Dataset com dados de salários
└── README.md           # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Python** - Linguagem principal
- **Streamlit** - Framework para criar Data Apps
- **Pandas** - Manipulação de dados
- **Scikit-learn** - Machine Learning
- **Feature-engine** - Feature engineering
- **Matplotlib/Plotly** - Visualizações

## 🎥 Baseado na Live do Jornada de Dados

Este projeto foi desenvolvido seguindo a **live do canal Jornada de Dados** sobre Data Apps com Streamlit. A live aborda:

- Como criar aplicações de dados interativas
- Integração entre ML e interfaces web
- Boas práticas para Data Apps
- Deploy e compartilhamento de projetos

**🔗 [Assista a live completa aqui](https://www.youtube.com/live/TMtjnQ4sPTE)**

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install streamlit pandas scikit-learn feature-engine
```

### Executar o Data App
```bash
streamlit run app.py
```

### Treinar o Modelo
```bash
python train.py
```

## 📊 Funcionalidades do Data App

1. **Input de Dados**: Interface para inserir informações pessoais e profissionais
2. **Previsão em Tempo Real**: Calcula a faixa salarial prevista instantaneamente
3. **Visualizações**: Gráficos e análises dos dados
4. **Responsivo**: Funciona em desktop e mobile

## 🎯 Casos de Uso

- **Profissionais de dados** que querem entender o mercado
- **Recrutadores** que precisam de insights salariais
- **Estudantes** aprendendo sobre Data Apps
- **Empresas** analisando tendências salariais

## 🤝 Contribuição

Este projeto foi criado para fins educacionais. Sinta-se à vontade para:
- Fazer fork do projeto
- Sugerir melhorias
- Reportar bugs
- Adicionar novas funcionalidades

## 📚 Recursos Adicionais

- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Canal Jornada de Dados](https://www.youtube.com/@jornadadedados)
- [Comunidade de Dados Brasileira](https://www.linkedin.com/company/comunidade-de-dados-brasileira/)

---

**Desenvolvido durante a live do Jornada de Dados** 🎥📊

*Transformando dados em insights com Streamlit!*
