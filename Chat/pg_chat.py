import streamlit as st
import os
from langchain.memory import ConversationBufferMemory
from Chat.modelo import carrega_modelo

MEMORIA=ConversationBufferMemory()

def pag_chat():
    memoria=st.session_state.get('memoria', MEMORIA)
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)
    
    input_usuario = st.chat_input('Fale o que deseja do assistente')
    if input_usuario:
        #Humano
        chat = st.chat_message('human')
        chat.markdown(input_usuario)
        #Assistente
        chat = st.chat_message('ai')
        resposta = chat.write_stream(carrega_modelo(prompt_user=input_usuario))
        #inserindo na memória
        memoria.chat_memory.add_user_message(input_usuario)
        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria