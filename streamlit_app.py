# 👑 streamlit_app.py

import streamlit as st
from core.pipeline import run_pipeline

# Configuração da página
st.set_page_config(page_title="VaultStream", layout="centered")

# Header
st.title("🚀 VaultStream")
st.write("Torrent    →    Criptografia    →    Nuvem    →    Limpeza")

# Campo para múltiplos magnet links
magnet_text = st.text_area(
    "Cole os links magnéticos (um por linha):",
    height=150
)

# Checkbox para criptografia
zipar = st.checkbox("Criptografar arquivo ZIP")

# Seleção de destino via rclone
destino = st.selectbox(
    "Destino:",
    ["GoogleDrive", "OneDrive", "Mega"]
)

# Botão iniciar
if st.button("Iniciar"):
    links = [l.strip() for l in magnet_text.strip().split("\n") if l.strip()]
    if not links:
        st.warning("Cole pelo menos um magnet link válido.")
    else:
        with st.spinner("Processando os torrents..."):
            run_pipeline(links=links, destino=destino, zipar=zipar)
        st.success("Todos os torrents foram processados com sucesso!")
