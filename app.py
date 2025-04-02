import streamlit as st
from Acesso.login import login
from Carrega.pg_upload import upload_arquivo
from Chat.pg_chat import pag_chat

st.set_page_config(page_title="assistente", layout='centered')

def main():
    if 'dados' not in st.session_state:
        login()
    elif st.session_state.dados and ('arquivo' not in st.session_state):
        upload_arquivo()
    elif st.session_state.dados and st.session_state.arquivo:
        pag_chat()
    else:
        st.write(st.session_state.dados)
        st.markdown(st.session_state.arquivo)
        st.markdown(st.session_state.memoria)

if __name__=="__main__":
    main()