import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader

def carrega_pdf(caminho):
    carrega = PyMuPDFLoader(caminho)
    documento = carrega.load()
    arquivo = '\n\n'.join([doc.page_content for doc in documento])
    return arquivo
    