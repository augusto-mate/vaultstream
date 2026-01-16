# Changelog

Todas as mudanças notáveis do VaultStream serão documentadas aqui.

O formato segue parcialmente o padrão Keep a Changelog
e Versionamento Semântico ([SemVer](https://semver.org/spec/v2.0.0.html)).

---

## [0.1.0] - 2026-01-13

### 🚀 Added
- Download de torrents via magnet links (aria2)
- Interface web simples com Gradio
- Upload automático para:
  - Google Drive
  - OneDrive
  - Mega.nz
- Criptografia AES-256 com 7-Zip
- Notificações por e-mail:
  - início
  - falha
  - conclusão
- Limpeza automática de arquivos locais (anti-rastros)
- Suporte a Google Colab
- Suporte a VPS / Seedbox
- Suporte a Docker e Docker Compose
- Documentação técnica interna
- CONTRIBUTING.md
- Licença MIT

### 🔐 Security
- Nenhuma credencial hardcoded
- Uso exclusivo de variáveis de ambiente
- Nenhuma persistência local após upload

### ⚠️ Known limitations
- Logs de infraestrutura (ex: Colab) não são controláveis
- Interface ainda sem autenticação
- Sem histórico persistente de downloads
