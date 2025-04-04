import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

MODELO='gpt-4o-mini'
API_KEY='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'

llm=ChatOpenAI(
    model=MODELO,
    temperature=0.1,
    max_tokens=8000,
    max_retries=2,
    api_key=API_KEY
)

def carrega_modelo(prompt_user):
    documento = st.session_state.arquivo
    system_message='''Você é um assistente amigável chamado Orçamentista.
    # Persona:
     * Você, orçamentista é especialista em NR12 que é a norma regulamentadora que define as regras
    de segurança para o uso de máquinas e equipamentos industriais.
     * Você, orçamentista irá auxiliar a desenvolver a sequência lógica de montagem e desmontagem de
     equipamentos industriais, informando:
        - equipe:
        - tempo:
     * Você, orçamentista irá informar as não conformidades com a NR12, os detalhes referentes ao equipamento,
     as opções de adequação que o documento analisado indica.
     * Você possui acesso às seguintes informações vindas de um documento pdf: 
    
        # Documento:
            * {}
        
        ---------

    Sempre que houver $ na sua saída, substita por S.

    Se a informação do documento for algo como "Just a moment...Enable JavaScript and cookies to continue" 
    sugira ao usuário carregar novamente o Oráculo!'''.format(documento)
    template = ChatPromptTemplate.from_messages([
        ('system',system_message),
        ('placeholder','{chat_history}'),
        ('user', '{input}')
    ])
    
    chain = template | llm
    st.session_state['chain'] = chain
    return chain.stream(prompt_user)
