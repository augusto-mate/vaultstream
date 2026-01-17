# 👑 streamlit_app.py

import streamlit as st
from core.pipeline import run_pipeline

st.set_page_config(page_title="VaultStream", layout="centered")

st.title("🚀 VaultStream")
st.write("Torrent → Criptografia → Nuvem → Limpeza")

# ----------------------------
# FORM evita reruns constantes
# ----------------------------
with st.form("vaultstream_form"):
    magnet_text = st.text_area(
        "Cole os links magnéticos (um por linha):",
        height=180,
        placeholder="magnet:?xt=urn:btih:..."
    )

    zipar = st.checkbox("Criptografar arquivos")

    destino = st.selectbox(
        "Destino (rclone):",
        ["GoogleDrive", "OneDrive", "Mega"]
    )

    submit = st.form_submit_button("🚀 Iniciar")

# ----------------------------
# Execução controlada
# ----------------------------
if submit:
    links = [l.strip() for l in magnet_text.splitlines() if l.strip()]

    if not links:
        st.error("❌ Cole pelo menos um magnet link válido.")
    else:
        st.success(f"📥 {len(links)} torrent(s) na fila")
        with st.spinner("Processando torrents..."):
            run_pipeline(
                links=links,
                destino=destino,
                zipar=zipar
            )
        st.success("✅ Processo concluído com sucesso!")
