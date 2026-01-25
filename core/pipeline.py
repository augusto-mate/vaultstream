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

def run_pipeline(magnet_link: str, use_encryption: bool, r_remote: str, r_folder: str, email_to: str):
    """
    Executa o fluxo completo com feedback em tempo real para a UI.
    """
    # Não falha o pipeline se o envio inicial falhar
    yield "📧 Enviando notificação de início..."
    try:
        send_email("VaultStream", "Download iniciado", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO)
    except Exception as e:
        yield f"⚠️ Falha no email (opcional): {str(e)}"

    # Feedback curto com o link (limitado para manter o UI responsivo)
    yield f"🔄 Iniciando Pipeline para: {magnet_link[:40]}..."
    
    # Informações do sistema (antes de iniciar)
    yield get_sys_info()

    # Notificação Inicial específica do pipeline (log iterável)
    for log in send_email("Tarefa Iniciada", f"O download do magnet {magnet_link[:30]} começou.", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO):
        yield log
    
    # 1. DOWNLOAD (Motor Aria2)
    yield "📡 Conectando aos peers e iniciando download..."
    for status in download_torrent(magnet_link, DOWNLOAD_DIR):
        yield status
    
    yield get_sys_info()

    # 2. Processamento de Arquivo com Senha (7-Zip)
    final_path = ""
	# CRIPTOGRAFIA DIRETO
    if use_encryption:
        yield "🔐 Criptografia ativada (AES-256). Processando..."
    	for status in encrypt_folder(DOWNLOAD_DIR, ENCRYPTED_DIR, ZIP_PASSWORD):
            if "✅ Arquivo gerado" in status:
                final_path = status.split(": ")[1].strip()
            yield status
	# CRIPTOGRAFIA OPCIONAL
    else:
        yield "⏩ Criptografia ignorada. Preparando arquivos originais..."
        # Pega a primeira pasta/arquivo dentro do download_dir para subir
        items = os.listdir(DOWNLOAD_DIR)
        if items:
            final_path = os.path.join(DOWNLOAD_DIR, items[0])
        else:
            yield "❌ Erro: Nenhum arquivo encontrado para upload."
            return

    # 3. UPLOAD (Rclone)
    if final_path and os.path.exists(final_path):
        yield f"🚀 Enviando para {r_remote}:{r_folder}..."
        for status in upload_with_rclone(final_path, r_remote, r_folder):
            yield status

    # 4. LIMPEZA
    yield "🧹 Realizando limpeza de arquivos temporários..."
    try:
        cleanup_paths(DOWNLOAD_DIR, ENCRYPTED_DIR)
    except Exception as e:
        yield f"⚠️ Falha na limpeza: {str(e)}"

    yield get_sys_info()

    # Notificação Final Interativa
    if email_to:
        for log in send_email("Tarefa Concluída", "O arquivo foi processado e enviado para a nuvem.", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO):
            yield log
    
    yield "🏁 [CONCLUÍDO]"
	
    # 5. FINALIZAÇÃO
    yield "✅ TUDO PRONTO: Download, criptografia e upload concluídos!"
    
    try:
        send_email("VaultStream", "Download concluído com sucesso", SMTP_SERVER, SMTP_PORT, EMAIL_FROM, EMAIL_PASS, EMAIL_TO)
    except:
        # Não falha o pipeline se o envio final falhar
        pass
