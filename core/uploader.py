# 📤 /core/uploader.py

import subprocess
import os
from mega import Mega

# ---------------------------------------
# Upload usando rclone (Google Drive / OneDrive)
# ---------------------------------------
def upload_with_rclone(file_path: str, remote: str, folder: str):
    """
    Upload de arquivo/pasta para um remote via rclone.
    
    Args:
        file_path (str): caminho local do arquivo ou pasta
        remote (str): nome do remote configurado no rclone
        folder (str): pasta destino dentro do remote
    """
    cmd = [
        "rclone",
        "copy",
        file_path,
        f"{remote}:{folder}"
    ]
    subprocess.run(cmd, check=True)


# ---------------------------------------
# Upload para Mega.nz usando API oficial
# ---------------------------------------
def upload_to_mega(file_path: str, email: str, senha: str):
    """
    Upload de arquivo/pasta para Mega.nz
    
    Args:
        file_path (str): caminho local do arquivo ou pasta
        email (str): e-mail da conta Mega.nz
        senha (str): senha da conta Mega.nz
    """
    if not all([email, senha]):
        raise ValueError("E-mail e senha da conta Mega.nz são obrigatórios")

    mega = Mega()
    m = mega.login(email, senha)

    # Se for pasta, enviar todos os arquivos dentro dela
    if os.path.isdir(file_path):
        for f in os.listdir(file_path):
            caminho_completo = os.path.join(file_path, f)
            if os.path.isfile(caminho_completo):
                m.upload(caminho_completo)
            elif os.path.isdir(caminho_completo):
                # Para subpastas, você pode adaptar para upload recursivo se necessário
                m.upload(caminho_completo)
    elif os.path.isfile(file_path):
        m.upload(file_path)
    else:
        raise FileNotFoundError(f"O caminho {file_path} não existe")
