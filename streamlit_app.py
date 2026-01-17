# 👑 streamlit_app.py

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
from core.pipeline import run_pipeline

st.markdown("""
    <style>
    .stProgress > div > div > div > div { background-color: #F9AB00; }
    .stButton>button { background-color: #F9AB00; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

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
