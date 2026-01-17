# 🌐 ui/gradio_app.py

import sys
import os
import gradio as gr

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from core.pipeline import run_pipeline

def run_ui(magnets_text, destino, zipar):
    links = [l.strip() for l in magnets_text.splitlines() if l.strip()]
    if not links:
        return "❌ Nenhum magnet link válido."

    run_pipeline(links, destino, zipar)
    return f"✅ {len(links)} torrent(s) processado(s) com sucesso!"

with gr.Blocks(title="VaultStream") as demo:
    gr.Markdown("# 🚀 VaultStream")
    gr.Markdown("Torrent → Criptografia → Nuvem → Limpeza")

    magnets = gr.Textbox(
        label="Magnet links (um por linha)",
        lines=6,
        placeholder="magnet:?xt=urn:btih:..."
    )

    destino = gr.Dropdown(
        ["GoogleDrive", "OneDrive", "Mega"],
        label="Destino (rclone)",
        value="GoogleDrive"
    )

    zipar = gr.Checkbox(label="Criptografar arquivos")

    output = gr.Textbox(label="Status")

    btn = gr.Button("🚀 Iniciar")
    btn.click(run_ui, inputs=[magnets, destino, zipar], outputs=output)

demo.launch(share=True)
