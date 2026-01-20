<!-- 📄 /docs/ARCHITECTURE.md -->

## 🗂️ Estrutura do Projeto

```text
vaultstream/
├── .github/						# CI/CD (config de workflows, integração com PRs, testes, build)
│   └── workflows/
│   	└── ci.yml
├── .gitignore						# Evita versionar artefatos sensíveis e ruído (envs, dados de usuário, logs)
├── config/							# Configurações da aplicação
│   ├── __init__.py
│   └── settings.py
├── core/							# Núcleo/implementação principal
│   ├── __init__.py
│   ├── cleanup.py
│   ├── emailer.py
│   ├── encrypt.py
│   ├── pipeline.py
│   ├── torrent_downloader.py
│   └── uploader.py
├── ui/							    # Interface Web (Gradio)
│   └── gradio_app.py
├── docker/							# Configuração de ambiente/container para desenvolvimento/produção
│   ├── docker-compose.yml
│   └── Dockerfile
├── docs/							# Documentação adicional, fluxos
│   ├── TECHNICAL.md
│   ├── flow.md
│   └── assets/                     # Recursos estáticos
│       └── logo.png
├── notebooks/						# Notebooks para experimentos/reprodução de fluxos
│   └── vaultstream_colab.ipynb
├── examples/						# Exemplos/Seeds de dados
│   ├── .env						# NÃO deve ser versionado (usar .env.local)
│   └── magnets.txt
├── README.md						# Visão geral do projeto, instruções de instalação
├── CHANGELOG.md					# Histórico de alterações
├── ROADMAP.md						# Planos futuros
├── CONTRIBUTING.md					# Guia de contribuição (How to contribute)
├── LICENSE							# Licença do projeto
├── requirements.txt				# Dependências principais
├── main.py							# Ponto de entrada principal da aplicação
└── SECURITY.md						# Boas práticas de segurança, políticas de resposta a incidentes
```

