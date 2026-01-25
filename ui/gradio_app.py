# 🌐 ui/gradio_app.py

import os
import sys
import gradio as gr

# Configurações de path e imports
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from core.pipeline import run_pipeline

# Lógica de processamento (UI separada)
def process_links_with_logs(magnets_text, use_encryption, rclone_remote, rclone_folder, email_target):
    """
    Processa uma lista de magnet links, chamando o pipeline real e emitindo logs incrementalmente para a UI.

    Args:
        magnets_text: texto indicando um ou mais links, um por linha.

    Yields:
        Tupla (status_label: str, log_text: str) para o componente Gradio.
    """
    # Extração de links, remoção de vazios
    links = [l.strip() for l in magnets_text.splitlines() if l.strip()]    
    # Validação inicial
    if not links:
        yield "Aguardando...", "❌ Erro:", "Por favor, insira pelo menos um link."
        return

    # Acúmulo de logs para apresentação incremental
    full_log = ""
    
    # Feedback visual 
    for link in links:
        # Aqui processa o pipeline real para o link atual
        for step_log in run_pipeline(link, use_encryption, rclone_remote, rclone_folder, email_target):
            full_log += step_log + "\n"
            yield "🔄 Processando...", full_log

# Estilo visual moderno (UI Gradio)
custom_css = """
.gradio-container { background-color: #0e1117; color: white; } 
#console-box textarea { font-family: 'Courier New', monospace; background-color: #1a1c23; color: #00ff00; }"
"""

with gr.Blocks(css=custom_css, title="VaultStream Elite") as demo:
    gr.Markdown("<h1 style='text-align: center; color: #F9AB00;'>🚀 VaultStream Console</h1>")
    gr.Markdown("<p style='text-align: center; color: #bbb;'>Torrent   →   Criptografia   →   Nuvem   →   Limpeza</p>")
    
    with gr.Row():
        with gr.Column(scale=1):
            magnets_input = gr.Textbox(label="🔗 Magnet Links", placeholder="Cole seus links aqui...\nAceita múltiplos links (um por linha).\nRecomendado: Até 5 links por vez.", lines=5)

            with gr.Accordion("⚙️ Configurações de Destino", open=True):
                remote_input = gr.Textbox(label="☁️ Rclone Remote", placeholder="Ex: gdrive, mega, onedrive")
                folder_input = gr.Textbox(label="📂 Pasta Destino", placeholder="Ex: VaultStream/Torrents")
                email_input = gr.Textbox(label="📧 Notificar por E-mail (Opcional)", placeholder="seu-email@gmail.com")
                
            encrypt_check = gr.Checkbox(label="🔐 Ativar Criptografia AES-256", value=False)
            
            with gr.Row():
                btn_run = gr.Button("🚀 INICIAR", variant="primary")
                btn_clear = gr.Button("🧹 LIMPAR")
        
        with gr.Column(scale=2):
            status = gr.Textbox(value="Aguardando comando...")
            console = gr.Textbox(label="Terminal de Saída", lines=15, elem_id="console-box", interactive=False)

        # A função process_links_with_logs recebe magnets_input como input e produz outputs status e console de logs
        btn_run.click(fn=process_links_with_logs, inputs=[magnets_input, encrypt_check, remote_input, folder_input, email_input], outputs=[status, console])
        btn_clear.click(fn=lambda: ("", "Standby", "", "gdrive", "VaultStream", ""), outputs=[magnets_input, status, console, remote_input, folder_input, email_input])
        
    # Rodapé
    gr.Markdown("<p style='text-align:center; color:#555; font-size:13px;'>© 2026 VaultStream — Augusto Mate</p>")

# Executa o app
if __name__ == "__main__":
    # share=True é vital para funcionar no Colab
    demo.launch(share=True, server_name="0.0.0.0", server_port=7860, debug=True)
