import streamlit as st
import tempfile
from Carrega.fc_loader import carrega_pdf

def carrega_arquivos(arquivo):
    with tempfile.NamedTemporaryFile(suffix='pdf',delete=False) as temp:
        temp.write(arquivo.read())
        nome_temporario = temp.name
        documento = carrega_pdf(nome_temporario)
        return documento
