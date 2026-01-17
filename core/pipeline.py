# 🧪 /core/pipeline.py

from config.settings import *
# Importamos diretamente o nome do arquivo, sem o prefixo 'core.'
from torrent_downloader import download_torrent
from encrypt import encrypt_folder
from uploader import upload_with_rclone
from cleanup import cleanup_paths
from emailer import send_email     

def run_pipeline(magnet_link: str):
    send_email("VaultStream", "Download iniciado", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO)

    download_torrent(magnet_link, DOWNLOAD_DIR)
    encrypted_file = encrypt_folder(DOWNLOAD_DIR, ENCRYPTED_DIR, ZIP_PASSWORD)
    upload_with_rclone(encrypted_file, RCLONE_REMOTE, RCLONE_FOLDER)

    cleanup_paths(DOWNLOAD_DIR, ENCRYPTED_DIR)

    send_email("VaultStream", "Download concluído com sucesso", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO)



