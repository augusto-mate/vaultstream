<!-- 📄 /docs/ARCHITECTURE.md -->

## 📂️ Estrutura do Projeto

```text
vaultstream/
├── .github							# CI/CD
│   └── workflows
│   	└── ci.yml
├── .gitignore						# Previne vazamento, ruído em PRs e erros comuns
├── config/							# Configurações do projeto
│   └── settings.py
├── assets							# Recursos estáticos
│   └── logo.png
├── core/							# Núcleo/implementação principal
│   ├── __init__.py
│   ├── cleanup.py
│   ├── emailer.py
│   ├── encrypt.py
│   ├── pipeline.py
│   ├── torrent_downloader.py
│   └── uploader.py
├── docker/							# Configurações de ambiente/container
│   ├── docker-compose.yml
│   └── Dockerfile
├── docs/							# Documentação adicional
│   ├── flow.md
│   └── TECHNICAL.md
├── notebooks/						# Notebooks para reprodução/experimentos
│   └── vaultstream_colab.ipynb
├── examples/						# Exemplos/Seeds de dados
│   ├── .env						# NÃO versionar
│   └── magnets.txt
├── README.md						# Visão geral do projeto, instruções rápidas
├── CHANGELOG.md					# Histórico de alterações
├── ROADMAP.md						# Planos futuros
├── CONTRIBUTING.md					# Guia de contribuição
├── LICENSE							# Licença
├── requirements.txt				# Dependências principais
├── main.py							# Ponto de entrada
├── streamlit_app.py				# App Streamlit
└── SECURITY.md						# Boas práticas de segurança 
```
