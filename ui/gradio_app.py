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
def process_links_with_logs(magnets_text, use_encryption, rclone_remote, rclone_folder):
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
        for step_log in run_pipeline(link, use_encryption, rclone_remote, rclone_folder):
            full_log += step_log + "\n"
            yield "🔄 Processando...", full_log

def reset_interface():
    # Retorna valores iniciais e força o status para Standby
    return gr.update(value=""), gr.update(value="Standby"), gr.update(value="")

# Estilo visual moderno (UI Gradio) — Dark Mode
custom_css = """
.gradio-container { background-color: #0e1117; }
#side-col { display: flex; flex-direction: column; gap: 15px; }
#console-box textarea { font-family: 'Fira Code', 'Courier New', monospace !important; background-color: #161b22 !important; color: #58a6ff !important; border: 1px solid #30363d !important; }
"""

with gr.Blocks(css=custom_css, title="VaultStream Elite") as demo:
    gr.Markdown("<h1 style='text-align: center; color: #f0883e;'>🚀 VaultStream Elite Console</h1>")
    gr.Markdown("<p style='text-align: center; color: #bbb;'>Torrent   →   Criptografia   →   Nuvem   →   Limpeza</p>")

    # Força colunas com a mesma altura
    with gr.Row(equal_height=True):
        with gr.Column(elem_id="side-col", scale=1):
            magnets_input = gr.Textbox(label="🔗 Magnet Links", placeholder="Um por linha (até 5 links por vez)...\nEx: magnet:?xt=urn:btih:...", lines=10)

            # with gr.Accordion("⚙️ Configurações de Destino", open=True):
                # remote_input = gr.Textbox(label="☁️ Rclone Remote", placeholder="Ex: gdrive, mega, onedrive")
                # folder_input = gr.Textbox(label="📂 Pasta Upload", placeholder="Ex: VaultStream/Torrents")
                # email_input = gr.Textbox(label="📧 Notificar por E-mail (Opcional)", placeholder="seu-email@gmail.com")

            # Agrupa campos para consistência
            with gr.Group():
                remote_input = gr.Textbox(label="☁️ Rclone Remote", value="gdrive")
                folder_input = gr.Textbox(label="📂 Pasta Destino", value="VaultStream/Torrents")
                encrypt_check = gr.Checkbox(label="🔐 Ativar Criptografia AES-256 (Modo Rápido)", value=False)
            
            with gr.Row():
                btn_run = gr.Button("🚀 INICIAR", variant="primary")
                btn_clear = gr.Button("🧹 LIMPAR")
        
        with gr.Column(scale=2):
            status_label = gr.Textbox(value="Aguardando comando...", label="Status Atual")
            # Ajustado para alinhar com a coluna esquerda
            console_output = gr.Textbox(label="🖳 Terminal de Saída", lines=22, elem_id="console-box", interactive=False)

        # A função process_links_with_logs recebe magnets_input como input e produz outputs status e console de logs
        btn_run.click(fn=process_links_with_logs, inputs=[magnets_input, encrypt_check, remote_input, folder_input], outputs=[status_label, console_output])
        # btn_clear.click(fn=lambda: ("", "Standby", "", "gdrive", "VaultStream"), outputs=[magnets_input, status_label, console_output, remote_input, folder_input])
        btn_clear.click(
            fn=reset_interface,
            inputs=None,
            outputs=[magnets_input, status_label, console_output],
            queue=False # Importante: pula a fila para limpar instantaneamente
        )
        
    # Rodapé
    gr.Markdown("<p style='text-align:center; color:#555; font-size:13px;'>© 2026 VaultStream — Augusto Mate</p>")

# Executa o app
if __name__ == "__main__":
    # share=True é vital para funcionar no Colab
    demo.launch(share=True, server_name="0.0.0.0", server_port=7860, debug=True)
