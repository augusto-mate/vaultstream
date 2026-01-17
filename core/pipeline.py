# 🧪 /core/pipeline.py

from config.settings import *
from core.torrent_downloader import download_torrent
from core.encrypt import encrypt_folder
from core.uploader import upload_with_rclone, upload_to_mega
from core.cleanup import cleanup_paths
from core.emailer import send_email


def run_pipeline(
    links: list,
    destino: str = "Google Drive",
    zipar: bool = False,
    email_mega: str = None,
    senha_mega: str = None
):
    for idx, magnet_link in enumerate(links, 1):
        try:
            # Email: download iniciado
            send_email(
                subject=f"VaultStream: Iniciando download {idx}/{len(links)}",
                body=f"Iniciando download do torrent:\n{magnet_link}",
                server=SMTP_SERVER,
                port=SMTP_PORT,
                sender=EMAIL_FROM,
                password=EMAIL_PASS,
                receiver=EMAIL_TO
            )

            # Download
            download_torrent(magnet_link, DOWNLOAD_DIR)

            # Criptografia
            final_file = DOWNLOAD_DIR
            if zipar:
                final_file = encrypt_folder(DOWNLOAD_DIR, ENCRYPTED_DIR, ZIP_PASSWORD)

            # Upload
            if destino == "Mega.nz":
                upload_to_mega(final_file, email_mega, senha_mega)
            else:
                upload_with_rclone(final_file, destino, RCLONE_FOLDER)

            # Limpeza
            cleanup_paths(DOWNLOAD_DIR, ENCRYPTED_DIR)

            # Email: download concluído
            send_email(
                subject=f"VaultStream: Download concluído {idx}/{len(links)}",
                body=f"Torrent finalizado e enviado para {destino}:\n{magnet_link}",
                server=SMTP_SERVER,
                port=SMTP_PORT,
                sender=EMAIL_FROM,
                password=EMAIL_PASS,
                receiver=EMAIL_TO
            )

        except Exception as e:
            send_email(
                subject=f"VaultStream: Falha no download {idx}/{len(links)}",
                body=f"Ocorreu um erro ao processar o torrent:\n{magnet_link}\n\nErro: {str(e)}",
                server=SMTP_SERVER,
                port=SMTP_PORT,
                sender=EMAIL_FROM,
                password=EMAIL_PASS,
                receiver=EMAIL_TO
            )
