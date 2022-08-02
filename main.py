import streamlit as st

#def page_switcher(page):
    #st.session_state.runpage = page1


def main():
    if 'genero' not in st.session_state:
        st.session_state.genero = 1

    st.session_state.genero = st.radio(
        "Escolha o gênero do filme",
        ('Ação', 'Comédia', 'Suspense', 'Terror'),index=st.session_state.genero)
    print(st.session_state.genero)

    btn = st.button('Próxima página')
    if btn:
        st.session_state.runpage = page1
        st.experimental_rerun()


def page1():

    LGPD = st.selectbox(
        'Sua privacidade e segurança é muito importante para nós! Seguimos a LGPD.',
        ('Termo de consetimento', ''))

    agree = st.checkbox("Declaro que concordo com o Termo de Constimento")

    btn = st.button('Próxima página')
    if btn:
        st.session_state.runpage = page2
        st.experimental_rerun()

    btn2 = st.button('Voltar')
    if btn2:
        st.session_state.runpage = main
        st.experimental_rerun()


def page2():
    name = st.text_input('Qual seu nome completo?', )
    number = st.text_input('Qual seu contato *(Com DDD)? EX: 99 999990000', )

    call = st.checkbox("Ligação Telefonica")
    Telegram = st.checkbox("Telegram")
    Facebook = st.checkbox("Facebook Messager")
    sms = st.checkbox("SMS")
    WhatsApp = st.checkbox("Whatsapp")

    btn = st.button('Voltar')
    if btn :
        st.session_state.runpage = page1
        st.experimental_rerun()

    btn2 = st.button('Próxima página')
    if btn2:
        st.session_state.runpage = page2
        st.experimental_rerun()

if __name__ == '__main__':
    if 'runpage' not in st.session_state :
        st.session_state.runpage = main
        st.session_state.runpage()
