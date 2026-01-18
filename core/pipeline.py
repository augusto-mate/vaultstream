# 🧪 /core/pipeline.py

import os
import shutil
import psutil 
from config.settings import *
from core.torrent_downloader import download_torrent
from core.encrypt import encrypt_folder
from core.uploader import upload_with_rclone
from core.cleanup import cleanup_paths
from core.emailer import send_email

def get_sys_info():
    disk = shutil.disk_usage("/")
    ram = psutil.virtual_memory()
    return f"📊 [SYS] Disco Livre: {disk.free // (2**30)}GB | RAM: {ram.percent}%"

def run_pipeline(magnet_link: str):
    """
    Executa o fluxo completo com feedback em tempo real para a UI.
    """
    yield "📧 Enviando notificação de início..."
    try:
        send_email("VaultStream", "Download iniciado", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO)
    except Exception as e:
        yield f"⚠️ Falha no email (opcional): {str(e)}"

    # Informações do sistema (antes de iniciar)
    yield get_sys_info()

    # 1. DOWNLOAD (Motor Aria2)
    yield "📡 Conectando aos peers e iniciando download..."
    for status in download_torrent(magnet_link, DOWNLOAD_DIR):
        yield status
    
    yield get_sys_info()

    # 2. CRIPTOGRAFIA (7-Zip)
    yield "🔐 Iniciando criptografia com senha (7-Zip)..."
    encrypted_file = ""
    for status in encrypt_folder(DOWNLOAD_DIR, ENCRYPTED_DIR, ZIP_PASSWORD):
        if "✅ Arquivo gerado" in status:
            encrypted_file = status.split(": ")[1]
        yield status

    # 3. UPLOAD (Rclone)
    yield f"🚀 Iniciando upload para {RCLONE_REMOTE}..."
    for status in upload_with_rclone(encrypted_file, RCLONE_REMOTE, RCLONE_FOLDER):
        yield status

    # 4. LIMPEZA
    yield "🧹 Realizando limpeza de arquivos temporários..."
    try:
        cleanup_paths(DOWNLOAD_DIR, ENCRYPTED_DIR)
    except Exception as e:
        yield f"⚠️ Falha na limpeza: {str(e)}"
    
        # 5. FINALIZAÇÃO
    yield "✅ TUDO PRONTO: Download, criptografia e upload concluídos!"
    
    try:
        send_email("VaultStream", "Download concluído com sucesso", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO)
    except:
        # Não falha o pipeline se o envio final falhar
        pass
        
