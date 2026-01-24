# 🚀 VaultStream 

![VaultStream](https://img.shields.io/badge/Security_on_the_move-Automation_with_purpose-6A737D?labelColor=DCDCDC)

**O pipeline definitivo para processamento de torrents: Download → Criptografia → Nuvem → Limpeza.**  

## 📝 O que é o VaultStream?

**VaultStream** é uma ferramenta poderosa e automatizada projetada para capturar Magnet Links, baixar o conteúdo via Aria2, aplicar criptografia AES-256 (via 7-Zip) e realizar o upload direto para sua nuvem favorita (Google Drive, OneDrive, MEGA, S3, etc.) utilizando Rclone. Tudo isso com uma interface web moderna e feedback em tempo real.

### Diferenciais

- **Interface Gradio**: Interface web limpa e responsiva acessível por link público via Colab.
- **Feedback Estilo qBittorrent**: Acompanhe velocidade, peers e progresso de cada etapa em tempo real.
- **Segurança**: Criptografia de nível militar nos seus arquivos antes de subirem para a nuvem.
- **Eficiência**: Motor Aria2 para downloads ultra-rápidos com DHT habilitado.
- **Autolimpeza**: Gerenciamento inteligente de disco para evitar lotação em ambientes como o Google Colab.

## 🛠️ Arquitetura

O sistema é dividido em módulos especializados:
- `core/torrent_downloader.py`: Gerencia o motor de download Aria2.
- `core/encrypt.py`: Responsável pela compressão e senha dos arquivos.
- `core/uploader.py`: Interface de comunicação com o Rclone.
- `core/pipeline.py`: O orquestrador que une todas as etapas com logs em tempo real.

## 💻 Como executar 

### Google Colab (recomendado)

1. Clique no botão abaixo para abrir o arquivo `VaultStream_Gradio.ipynb` no Colab.  
[![Colab](https://img.shields.io/badge/📓_Open_in_Colab-6A737D?style=for-the-badge)](https://colab.research.google.com/github/augusto-mate/vaultstream/blob/main/notebooks/vaultstream_colab.ipynb)
2. Execute a **Fase 1** para instalar as dependências.
3. Sincronize seu repositório na **Fase 2**.
4. Configure seu provedor de nuvem na **Fase 3** (`rclone config`).
5. Inicie a interface na **Fase 4** e acesse o link público gerado.

### Docker / VPS 

1. Suba os containers com Docker Compose: ```docker compose up -d```
2. Acesse a interface web na porta `7860` (ex.: `http://localhost:7860`).

> Ideal para downloads longos, execução 24/7 e automação contínua.  

## ⚙️ Variáveis de Ambiente

O sistema utiliza as seguintes variáveis (configuráveis via Colab Secrets ou arquivo `.env`):
- `ZIP_PASSWORD`: Senha para a criptografia dos arquivos.
- `RCLONE_REMOTE`: Nome do remote configurado no Rclone (ex: `gdrive`).
- `RCLONE_FOLDER`: Pasta de destino na nuvem.

---

## ⚠️ Aviso Legal

> **VaultStream destina-se apenas a conteúdos legais.**  
> **Os utilizadores são responsáveis pelo cumprimento das leis locais.**

---

## 📚 Documentação

Nesta secção encontra os principais recursos para compreender, manter e evoluir o projeto:
- [`docs/TECHNICAL.md`](docs/TECHNICAL.md): Arquitetura técnica.  
- [`SECURITY.md`](SECURITY.md): Segurança.  
- [`ROADMAP.md`](ROADMAP.md): Roadmap.   
- [`CONTRIBUTING.md`](CONTRIBUTING.md): Contribuição.

## 👨🏽‍💻 Desenvolvedor

Criado por **Augusto Mate** — 2026.  
Conecte-se comigo no [GitHub](https://github.com/augusto-mate) e no [LinkedIn](https://www.linkedin.com/in/augusto-mate).

## 📄  Licença

Este projeto está licenciado sob a **MIT License**.  
Consulte [LICENSE](LICENSE) para mais detalhes.

---

### 📖 Inspiração

> "O Senhor guardará a tua saída e a tua entrada, desde agora e para sempre." — **Salmos 121:8**
