# 👑 streamlit_app.py (corrigido)

import streamlit as st
from core.pipeline import run_pipeline

# Configuração da página
st.set_page_config(page_title="VaultStream", layout="centered")

# Header
st.title("🚀 VaultStream")
st.write("Torrent   →   Criptografia   →   Nuvem   →   Limpeza")

# Campo para múltiplos magnet links
magnet_text = st.text_area(
    "Cole os links magnéticos (um por linha):",
    height=150
)

# Checkbox para criptografia
zipar = st.checkbox("Criptografar arquivo ZIP")

# Seleção de destino
destino = st.selectbox(
    "Destino:",
    ["Google Drive", "OneDrive", "Mega.nz"]
)

# Inputs de credenciais Mega.nz
if destino == "Mega.nz":
    email_mega = st.text_input("Digite seu e-mail Mega.nz:")
    senha_mega = st.text_input("Digite sua senha Mega.nz:", type="password")
else:
    email_mega = senha_mega = None

# Botão iniciar
if st.button("Iniciar"):
    # Validação básica
    links = [l.strip() for l in magnet_text.strip().split("\n") if l.strip()]
    if not links:
        st.warning("Cole pelo menos um magnet link válido.")
    elif destino == "Mega.nz" and (not email_mega or not senha_mega):
        st.warning("Para Mega.nz, preencha e-mail e senha.")
    else:
        with st.spinner("Processando os downloads..."):
            run_pipeline(
                links=links,
                destino=destino,
                zipar=zipar,
                email_mega=email_mega,
                senha_mega=senha_mega
            )
        st.success("Todos os torrents foram processados com sucesso!")
