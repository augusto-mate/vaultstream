# 📤 /core/uploader.py

import subprocess
import os

def upload_with_rclone(file_path: str, remote: str, folder: str):
    """
    Upload de arquivo/pasta para um remote via rclone.

    Args:
        file_path (str): caminho local do arquivo ou pasta
        remote (str): nome do remote configurado no rclone (Google Drive, OneDrive, Mega)
        folder (str): pasta destino dentro do remote
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O caminho {file_path} não existe")

    cmd = [
        "rclone",
        "copy",
        file_path,
        f"{remote}:{folder}"
    ]
    subprocess.run(cmd, check=True)
