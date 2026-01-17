# 👑 streamlit_app.py

import os
import sys

# Define a raiz e a pasta core
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(ROOT_DIR, "core")

# Adiciona ambos ao path
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if CORE_DIR not in sys.path:
    sys.path.insert(1, CORE_DIR)

import streamlit as st
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




