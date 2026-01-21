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

## 📁 Estrutura do projeto

Consulte [`ARCHITECTURE.md`](ARCHITECTURE.md) para detalhes completos sobre a árvore de diretórios, responsabilidades por pasta, arquivos-chave e fluxos de build e testes.

---

## ⬇️ Torrent engine

### Tecnologia

- **aria2**

### Benefícios

- Estabilidade
- Suporte a magnet links
- Excelente desempenho
- Facilidade de automação

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
- progresso 
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

Veja o diagrama completo do fluxo de dados e das etapas do pipeline em [`flow.md`](flow.md).

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
