# 📨 /core/emailer.py

import smtplib
from email.mime.text import MIMEText
import os

def send_email(subject: str, body: str, smtp_server, smtp_port, email_from, email_pass, email_to):
    """
    Envia notificações por e-mail com tratamento de erro para não interromper o pipeline.
    """
    # Verifica se as credenciais existem
    if not all([smtp_server, email_from, email_pass, email_to]):
        yield "ℹ️ [EMAIL] Credenciais incompletas. Notificação ignorada."
        return  # Email opcional

    try:
        msg = MIMEText(body)
        msg["Subject"] = f"🚀 VaultStream: {subject}"
        msg["From"] = email_from
        msg["To"] = email_to

        # Usamos SMTP_SSL para segurança máxima (Porta 465)
        with smtplib.SMTP_SSL(smtp_server, int(smtp_port), timeout=10) as server:
            server.login(email_from, email_pass)
            server.send_message(msg)
        
        yield f"📧 [EMAIL] Notificação '{subject}' enviada com sucesso."
    
    except Exception as e:
        # Se o e-mail falhar (senha errada, rede), o pipeline CONTINUA
        yield f"⚠️ [EMAIL] Erro ao enviar notificação: {str(e)}"
        
