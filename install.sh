#!/bin/bash

# Script de instalação para o projeto Data Apps com Streamlit
# Compatível com macOS e Linux

echo "🚀 Instalando Data Apps com Streamlit..."
echo "========================================"

# Verificar se Python 3.12 está instalado
if command -v python3.12 &> /dev/null; then
    PYTHON_CMD="python3.12"
    echo "✅ Python 3.12 encontrado"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "✅ Python 3 encontrado"
else
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.8+ primeiro."
    exit 1
fi

# Verificar versão do Python
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "📦 Versão do Python: $PYTHON_VERSION"

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Tentando instalar..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        $PYTHON_CMD get-pip.py
        rm get-pip.py
    else
        # Linux
        sudo apt-get update
        sudo apt-get install -y python3-pip
    fi
fi

# Criar ambiente virtual (opcional)
read -p "🤔 Deseja criar um ambiente virtual? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Criando ambiente virtual..."
    $PYTHON_CMD -m venv venv
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        source venv/bin/activate
    else
        # Linux
        source venv/bin/activate
    fi
    
    echo "✅ Ambiente virtual criado e ativado"
    echo "💡 Para ativar manualmente: source venv/bin/activate"
fi

# Instalar dependências
echo "📦 Instalando dependências..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Verificar instalação
echo "🔍 Verificando instalação..."
if python3 -c "import streamlit; print('✅ Streamlit instalado:', streamlit.__version__)" 2>/dev/null; then
    echo "✅ Instalação concluída com sucesso!"
else
    echo "❌ Erro na instalação do Streamlit"
    exit 1
fi

# Tornar o script run_exemplos.py executável
chmod +x run_exemplos.py

echo ""
echo "🎉 Instalação concluída!"
echo "========================="
echo ""
echo "Para executar o app principal:"
echo "  streamlit run app.py"
echo ""
echo "Para executar exemplos específicos:"
echo "  streamlit run exemplos/exemplo_basico.py"
echo "  streamlit run exemplos/dashboard_vendas.py"
echo "  streamlit run exemplos/ml_app.py"
echo ""
echo "Ou use o script de execução:"
echo "  python3 run_exemplos.py"
echo ""
echo "📚 Documentação: https://docs.streamlit.io/"
echo "💬 Comunidade: https://discuss.streamlit.io/"
echo ""
