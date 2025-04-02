import streamlit as st
import json

def verifica_login():
    if st.session_state.senha == st.session_state.usuarios[st.session_state.usuario]['senha']:
        st.session_state.dados = list(st.session_state.usuarios[st.session_state.usuario].values())[1:]
    else:
        st.warning("erro")

def login():
    file = open("Acesso/usuarios.json","r")
    usuarios = json.load(file)
    st.session_state['usuarios']=usuarios
    file.close()
    
    with st.form(key="formulario", clear_on_submit=True):
        usuario = st.selectbox(label="Escolha o usuario:", options=usuarios.keys(), key="usuario")
        senha = st.text_input("senha",type='password',key="senha")
        dados = st.form_submit_button("Logar", use_container_width=True, on_click=verifica_login)
