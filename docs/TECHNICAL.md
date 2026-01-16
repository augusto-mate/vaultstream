<!-- 📄 /docs/TECHNICAL.md -->

# VaultStream — Technical Documentation

Este documento descreve a arquitetura interna, decisões técnicas e fluxo de execução do VaultStream.

Destinado a:
- contribuidores
- mantenedores
- usuários avançados
- adaptação para VPS / seedbox

---

## 🧱 Arquitetura geral

VaultStream é organizado como um **pipeline modular**:

```text
UI (Gradio)
   ↓
Input Validation
   ↓
Torrent Engine (aria2)
   ↓
Temporary Storage
   ↓
Encryption Layer (7-Zip AES-256)
   ↓
Cloud Transfer (rclone / Mega API)
   ↓
Cleanup & Notifications
```

Cada etapa é desacoplada para facilitar manutenção e extensões.

---

## 🗂️ Estrutura do projeto

```css
vaultstream/
├── .github							# CI/CD
│   └── workflows
│   	└── ci.yml
├── .gitignore 						# Previne vazamento, ruído em PRs e erros comuns
├── assets							# Recursos estáticos
│   └── logo.png
├── config/							# Configurações do projeto
│   └── settings.py
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
│   ├── ARCHITECTURE.md
│   ├── flow.md
│   └── TECHNICAL.md
├── examples/						# Exemplos/Seeds de dados
│   ├── .env						# NÃO versionar
│   └── magnets.txt
├── notebooks/						# Notebooks para reprodução/experimentos
│   └── vaultstream_colab.ipynb
├── CHANGELOG.md					# Histórico de alterações
├── CONTRIBUTING.md					# Guia de contribuição
├── LICENSE							# Licença
├── main.py							# Ponto de entrada
├── README.md						# Visão geral do projeto, instruções rápidas
├── requirements.txt		    	# Dependências principais
├── ROADMAP.md						# Planos futuros
├── SECURITY.md						# Boas práticas de segurança 
└── streamlit_app.py		    	# App Streamlit
```

---

## ⬇️ Torrent engine

### Tecnologia

- **aria2**
- Motivos:
	- estável
	- suporta magnet links
	- excelente desempenho
	- fácil automação

### Execução

- Downloads ocorrem em diretório temporário
- Progresso monitorado via stdout
- Timeout e falhas são capturados

---

## 🔐 Criptografia

### Tecnologia

- **7-Zip**
- Algoritmo: AES-256

### Características

- Protege conteúdo e nomes de arquivos
- Senha fornecida via variável de ambiente
- Criptografia ocorre antes do upload

---

## ☁️ Upload para nuvem

### Tecnologia principal

- **rclone**

### Serviços suportados

- Google Drive
- OneDrive
- Mega.nz (API direta opcional)

### Observações

- rclone é preferido por ser:
	- open-source
	- confiável
	- extensível
	- amplamente usado em produção

---

## 📧 Notificações

### Eventos monitorados

- início do download
- progresso (opcional)
- falha
- conclusão

### Implementação

- SMTP padrão
- compatível com Gmail, ProtonMail, etc.
- totalmente opcional

---

## 🧹 Limpeza (anti-rastros)

Após upload bem-sucedido:
- arquivos temporários são apagados
- diretórios removidos
- logs sensíveis descartados

Objetivo:

> zero persistência local

---

## 🐳 Docker & VPS

### Docker

- Imagem mínima
- Executa como seedbox real
- Interface web via Gradio

### VPS

- Execução 24/7
- Ideal para:
	- downloads longos
	- automação
	- uso contínuo

---

## 🔄 Fluxo resumido

```text
User → UI → aria2 → encrypt → rclone → cloud → cleanup → notify
```

---

## 🚀 Extensões futuras (roadmap)

- Webhook (Telegram / Discord)
- Painel de histórico
- Suporte a S3 / Backblaze
- Modo headless (API REST)
- Auth na interface web

---

## ️⚠️ Aviso técnico

VaultStream não controla:
- logs de infraestrutura (ex: Colab)
- políticas de provedores externos

Usuários são responsáveis por conformidade legal.
