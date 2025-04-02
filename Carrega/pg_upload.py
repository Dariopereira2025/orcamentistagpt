import streamlit as st
from Carrega.fc_carrega import carrega_arquivos

def upload_arquivo():
    with st.container(border=True):
        arquivo = st.file_uploader(label="Escolha o PDF", type=['.pdf'])
        if arquivo:
            if st.button(label="Upload", use_container_width=True):
                #carrega_arquivos(arquivo=arquivo)
                documento = carrega_arquivos(arquivo=arquivo)
                st.session_state['arquivo']=documento

