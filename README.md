# VaultStream 🚀

![Open Source](https://img.shields.io/badge/Open%20Source-100%25-6AA84F)
![License](https://img.shields.io/badge/License-MIT-16A34A)
![Python](https://img.shields.io/badge/Python-3.9+-3B82F6)
![Docker](https://img.shields.io/badge/Docker-Ready-0D6EFD)
![Colab](https://img.shields.io/badge/Google%20Colab-Ready-F9AB00)
![Cloud](https://img.shields.io/badge/Cloud-First-E67E22)

<br>

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

## 🔀️ Fluxo

```text
Torrent
  ↓
Cloud 
  ↓
Email 
```

Veja o diagrama completo em [`docs/flow.md`](docs/flow.md).

---

## ⚙️ Guia Prático de Execução em Ambientes

### Google Colab (recomendado)

Clique no botão abaixo:

[![Colab](https://img.shields.io/badge/VaultStream-📓_Abrir_no_Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=F9AB00)](https://colab.research.google.com/github/augusto-mate/vaultstream/blob/main/notebooks/vaultstream_colab.ipynb)

O notebook:
- instala dependências
- configura o ambiente
- executa o VaultStream

📌 _Na Fase 3, interaja com o terminal para configurar sua nuvem._

### Interface Web (Streamlit)

Após iniciar:

```bash
streamlit run streamlit_app.py
```

- Colab: acesso via link público
- VPS/Docker: `http://localhost:8501`

### Docker (seedbox real)

```bash
docker compose up -d
```

Ideal para:
- downloads longos
- execução 24/7
- automação contínua

---

## 📁 Estrutura do Projeto

Consulte [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) para detalhes completos da árvore de diretórios, responsabilidades de cada pasta, arquivo e fluxos de build/teste. 

## 📚 Documentação

<table>
  <tr>
    <td>📝 Arquitetura técnica</td>
    <td><a href="docs/TECHNICAL.md"><code>docs/TECHNICAL.md</code></a></td>
  </tr>
  <tr>
    <td>🛡️ Segurança</td>
    <td><a href="SECURITY.md"><code>SECURITY.md</code></a></td>
  </tr>
  <tr>
    <td>🗺️ Roadmap</td>
    <td><a href="ROADMAP.md"><code>ROADMAP.md</code></a></td>
  </tr>
  <tr>
    <td>🫂 Contribuição</td>
    <td><a href="CONTRIBUTING.md"><code>CONTRIBUTING.md</code></a></td>
  </tr>
</table>

---

## 🔐 Segurança & Privacidade

- Implementação de criptografia AES-256 para proteção de dados 
- Não existem credenciais codificadas no código
- Arquivos temporários usados durante o upload são eliminados após o processamento
- Execução em Colab funciona de forma efêmera, com descarte da VM ao final da sessão

> 📜 Logs de infraestrutura (Colab, VPS, cloud) não são controláveis pelo projeto.

## ⚠️ Aviso Legal

VaultStream destina-se apenas a conteúdos legais.  
Os utilizadores são responsáveis pelo cumprimento das leis locais.

---

## 👤 Autor

Desenvolvido com 💡 por **Augusto Mate**  

| 🐙 GitHub | 🔗 LinkedIn |
| :-------: | :-------: |
| [@augusto-mate](https://github.com/augusto-mate) | [@augusto-mate](https://linkedin.com/in/augusto-mate) |

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> **Última atualização:** Janeiro 2026
