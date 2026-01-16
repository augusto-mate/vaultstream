# VaultStream 🚀

![Release](https://img.shields.io/github/v/release/augusto-mate/vaultstream)
![CI](https://img.shields.io/github/actions/workflow/status/augusto-mate/vaultstream/ci.yml)
![Open Source](https://img.shields.io/badge/Open%20Source-100%25-16A34A)

![License](https://img.shields.io/badge/License-MIT-3B82F6)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB)
![Docker](https://img.shields.io/badge/Docker-Ready-0D6EFD)
![Colab](https://img.shields.io/badge/Google%20Colab-Ready-F9AB00)

**VaultStream** é um projeto **open-source** que automatiza o fluxo completo:

> **Torrent → Criptografia → Nuvem → Limpeza automática**

Com foco em **privacidade**, **simplicidade** e **execução na nuvem**.

---

## ✨ Funcionalidades Principais

- ⬇️ Download de torrents via magnet (aria2)
- 🗝️ Criptografia forte **AES-256** (7-Zip)
- ☁️ Upload automático para:
  - Google Drive
  - OneDrive
  - Mega.nz
- 📧 Notificações por e-mail (início, progresso, falha, sucesso)
- 🧹 Remoção segura de arquivos locais (anti-rastros)
- 🌐 Interface web via **Streamlit**
- 🐳 Suporte a Docker / VPS
- 🧪 Compatível com **Google Colab**
- 🆓 Totalmente gratuito e com código-fonte aberto

<br>

## 🎨 Identidade Visual

<p align="justify">
  <img src="assets/logo.png" alt="VaultStream Logo" width="500" />
</p>

> **Segurança em movimento. Automação orientada por propósito.**  

<br>

## 🔀️ Arquitetura (fluxo)

```text
Magnet Links
     ↓
aria2 (torrent)
     ↓
Arquivos temporários
     ↓
7-Zip (AES-256)
     ↓
rclone (upload cloud)
     ↓
Google Drive / OneDrive / Mega
     ↓
Limpeza automática
     ↓
Notificação por e-mail
```

Veja o diagrama completo em [`docs/flow.md`](docs/flow.md).

<br>

## ⚙️ Guia Prático de Execução em Ambientes

### Google Colab (recomendado)

Clique no botão abaixo:

[![Colab](https://img.shields.io/badge/VaultStream-📓_Abrir_no_Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=F9AB00)](https://colab.research.google.com/github/augusto-mate/vaultstream/blob/main/notebooks/vaultstream_colab.ipynb)

O notebook:
- instala dependências
- configura o ambiente
- executa o VaultStream

<br>

### Interface Web (Streamlit)

Após iniciar:

```bash
streamlit run streamlit_app.py
```

- Colab: acesso via link público
- VPS/Docker: `http://localhost:8501`

<br>

### Docker (seedbox real)

```bash
docker compose up -d
```

Ideal para:
- downloads longos
- execução 24/7
- automação contínua

<br>

## 📁 Estrutura do Projeto

Consulte [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) para detalhes completos da árvore de diretórios, responsabilidades de cada pasta, arquivo e fluxos de build/teste. 

<br>

## 📘 Documentação

- 📄 Arquitetura técnica: [`docs/TECHNICAL.md`](docs/TECHNICAL.md)
- 🔒 Segurança: [`SECURITY.md`](SECURITY.md)
- 🛣️ Roadmap: [`ROADMAP.md`](ROADMAP.md)
- 🤝 Contribuição: [`CONTRIBUTING.md`](CONTRIBUTING.md)

<br>

## 🔐 Segurança & Privacidade

- Implementação de criptografia AES-256 para proteção de dados 
- Não existem credenciais codificadas no código
- Arquivos temporários usados durante o upload são eliminados após o processamento
- Execução em Colab funciona de forma efêmera, com descarte da VM ao final da sessão

📜 Logs de infraestrutura (Colab, VPS, cloud) não são controláveis pelo projeto.

<br>

## ⚠️ Aviso Legal

VaultStream é apenas uma ferramenta técnica.  
O usuário é totalmente responsável por garantir o uso legal do software e dos conteúdos transferidos.

<br>

## 👤 Autor

Desenvolvido com 💡 por **Augusto Mate**  

| 🐙 GitHub | 🔗 LinkedIn |
| :-------: | :-------: |
| [@augusto-mate](https://github.com/augusto-mate) | [@augusto-mate](https://linkedin.com/in/augusto-mate) |

<br>

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> **Última atualização:** Janeiro 2026
