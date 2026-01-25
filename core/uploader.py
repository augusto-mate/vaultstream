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
    # Normaliza o caminho para absoluto
    abs_path = os.path.abspath(file_path)
    # Valida a existência antes de prosseguir (usando o caminho absoluto)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"O caminho {abs_path} não existe.")

    cmd = [
        "rclone", "copy", abs_path, f"{remote}:{folder}",
        "-P",                 # Flag de progresso
        "--stats", "1s",      # Atualiza status a cada 1 segundo
        "--stats-one-line",   # Mantém o log limpo
        "--transfers=8",      # Sobe 8 arquivos/partes simultaneamente
        "--checkers=16"       # Verifica integridade em paralelo
    ]

    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1
    )

    for line in process.stdout:
        # Filtra as linhas de progresso do Rclone para o console
        if "Transferred" in line or "%" in line:
            yield f"📤 Upload: {line.strip()}"

    process.wait()
    if process.returncode != 0:
        yield "❌ Erro durante o upload para a nuvem."
        
