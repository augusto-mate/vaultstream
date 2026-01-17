# 👑 streamlit_app.py

import os
import sys

# Pega o caminho absoluto de onde o streamlit_app.py está
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

import streamlit as st
# Agora o Python vai olhar diretamente na ROOT_DIR para achar a pasta 'core'
from core.pipeline import run_pipeline

st.set_page_config(page_title="VaultStream", layout="centered")

st.title("🚀 VaultStream")
st.write("Torrent → Criptografia → Nuvem → Limpeza")

magnet = st.text_area("Cole o magnet link")

if st.button("Iniciar"):
    if magnet.strip():
        with st.spinner("Processando..."):
            run_pipeline(magnet)
        st.success("Processo concluído!")
    else:
        st.warning("Cole um magnet link válido.")



