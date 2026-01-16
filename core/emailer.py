# 📨 /core/emailer.py

import smtplib
from email.mime.text import MIMEText

def send_email(subject: str, body: str, smtp_server, smtp_port, email_from, email_pass, email_to):
    if not all([smtp_server, email_from, email_pass, email_to]):
        return  # Email opcional

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email_from
    msg["To"] = email_to

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(email_from, email_pass)
        server.send_message(msg)
