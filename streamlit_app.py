# 👑 streamlit_app.py

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
