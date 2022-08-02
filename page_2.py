import streamlit as st

def page2():

    termo = "Termo de consetimento"
    LGPD = st.selectbox(
        'Sua privacidade e segurança é muito importante para nós! Seguimos a LGPD.',
        ('Termo de consetimento', ''))

    agree = st.checkbox("Declaro que concordo com o Termo de Constimento")

    page = st.button('Anterior')
    page2 = st.button('Próximo')
    form = st.button('Limpar Formulário')

    if page2 and agree:
        page_3.page3()

if(__name__ == "__main__"):
    page2()