# 🐍️ /config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

# Diretórios
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "downloads")
ENCRYPTED_DIR = os.getenv("ENCRYPTED_DIR", "encrypted")

# Criptografia
ZIP_PASSWORD = os.getenv("ZIP_PASSWORD", "vaultstream")

# rclone
RCLONE_REMOTE = os.getenv("RCLONE_REMOTE", "gdrive")
RCLONE_FOLDER = os.getenv("RCLONE_FOLDER", "VaultStream")

# Email
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")
