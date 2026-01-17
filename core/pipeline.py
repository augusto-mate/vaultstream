# 🧪 core/pipeline.py

from config.settings import *
from core.torrent_downloader import download_torrent
from core.encrypt import encrypt_folder
from core.uploader import upload_with_rclone
from core.cleanup import cleanup_paths
from core.emailer import send_email

def run_pipeline(links, destino, zipar=False):
    for idx, magnet in enumerate(links, 1):
        try:
            # Email: download iniciado
            send_email(
                subject=f"VaultStream | Início {idx}/{len(links)}",
                body=f"Iniciando download:\n{magnet}",
                smtp_server=SMTP_SERVER,
                smtp_port=SMTP_PORT,
                email_from=EMAIL_FROM,
                email_pass=EMAIL_PASS,
                email_to=EMAIL_TO,
            )

            # Download torrent
            download_torrent(magnet, DOWNLOAD_DIR)
            
            # Criptografia opcional
            final_path = DOWNLOAD_DIR
            if zipar:
                final_path = encrypt_folder(
                    DOWNLOAD_DIR,
                    ENCRYPTED_DIR,
                    ZIP_PASSWORD
                )

            # Upload via rclone
            upload_with_rclone(final_path, destino, RCLONE_FOLDER)

            # Cleanup
            cleanup_paths(DOWNLOAD_DIR, ENCRYPTED_DIR)
            
            # Email: download concluído
            send_email(
                subject=f"VaultStream | Concluído {idx}/{len(links)}",
                body=f"Torrent enviado para {destino}",
                smtp_server=SMTP_SERVER,
                smtp_port=SMTP_PORT,
                email_from=EMAIL_FROM,
                email_pass=EMAIL_PASS,
                email_to=EMAIL_TO,
            )
            
        except Exception as e:
            send_email(
                subject="VaultStream | Erro",
                body=str(e),
                smtp_server=SMTP_SERVER,
                smtp_port=SMTP_PORT,
                email_from=EMAIL_FROM,
                email_pass=EMAIL_PASS,
                email_to=EMAIL_TO,
            )
            raise
