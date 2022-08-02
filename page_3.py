import streamlit as st

def page3():

    name = st.text_input('Qual seu nome completo?',)
    number = st.text_input('Qual seu contato *(Com DDD)? EX: 99 999990000',)

    call = st.checkbox("Ligação Telefonica")
    Telegram = st.checkbox("Telegram")
    Facebook = st.checkbox("Facebook Messager")
    sms = st.checkbox("SMS")
    WhatsApp = st.checkbox("Whatsapp")

if(__name__ == "__main__"):
    page3()