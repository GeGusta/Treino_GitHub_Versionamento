# Guia de Contribuição

Obrigado por considerar contribuir para o projeto **Data Apps com Streamlit**! 🚀

## Como Contribuir

### 1. Fork e Clone

1. Faça um fork do repositório
2. Clone seu fork localmente:
```bash
git clone https://github.com/seu-usuario/data_apps_com_streamlit.git
cd data_apps_com_streamlit
```

### 2. Configurar Ambiente

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

### 3. Desenvolvimento

1. Crie uma branch para sua feature:
```bash
git checkout -b feature/nova-funcionalidade
```

2. Faça suas alterações
3. Teste localmente:
```bash
streamlit run app.py
```

4. Commit suas mudanças:
```bash
git add .
git commit -m "feat: adiciona nova funcionalidade"
```

5. Push para sua branch:
```bash
git push origin feature/nova-funcionalidade
```

### 4. Pull Request

1. Vá para o repositório original no GitHub
2. Clique em "New Pull Request"
3. Selecione sua branch
4. Descreva suas mudanças
5. Aguarde a revisão

## Padrões de Código

### Python
- Use Python 3.8+
- Siga o PEP 8
- Use type hints quando possível
- Documente funções e classes

### Streamlit
- Use `st.set_page_config()` no início dos apps
- Organize widgets logicamente
- Use cache para operações pesadas
- Mantenha a interface limpa e responsiva

### Estrutura de Arquivos
```
exemplos/
├── nome_do_exemplo.py    # Nome descritivo
├── dados/                # Dados de exemplo
└── assets/              # Imagens, CSS, etc.
```

## Tipos de Contribuição

### 🐛 Bug Fixes
- Descreva o bug claramente
- Inclua passos para reproduzir
- Teste a correção

### ✨ Novas Funcionalidades
- Explique o propósito
- Inclua exemplos de uso
- Atualize a documentação

### 📚 Melhorias na Documentação
- Corrija erros
- Adicione exemplos
- Melhore a clareza

### 🎨 Melhorias na UI/UX
- Mantenha consistência visual
- Teste em diferentes dispositivos
- Considere acessibilidade

## Checklist para Pull Requests

- [ ] Código segue os padrões estabelecidos
- [ ] Funcionalidade testada localmente
- [ ] Documentação atualizada
- [ ] Não quebra funcionalidades existentes
- [ ] Commit messages descritivas
- [ ] Pull request bem documentado

## Recursos Úteis

- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Comunidade Streamlit](https://discuss.streamlit.io/)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## Código de Conduta

- Seja respeitoso e inclusivo
- Ajude outros desenvolvedores
- Mantenha discussões construtivas
- Reporte comportamentos inadequados

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto.

---

Obrigado por contribuir! 🙏
