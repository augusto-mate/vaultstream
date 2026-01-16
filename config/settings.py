# 🐍️ /config/settings.py

import os

# Diretórios
BASE_DIR = "/content/vaultstream" if os.path.exists("/content") else "/tmp/vaultstream"
DOWNLOAD_DIR = f"{BASE_DIR}/downloads"
ENCRYPTED_DIR = f"{BASE_DIR}/encrypted"

# Criptografia
ZIP_PASSWORD = os.getenv("VAULTSTREAM_ZIP_PASSWORD", "vaultstream123")

# Email
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

# rclone
RCLONE_REMOTE = os.getenv("RCLONE_REMOTE", "gdrive")
RCLONE_FOLDER = os.getenv("RCLONE_FOLDER", "VaultStream")
