import streamlit as st


def page1():
    genero = st.radio(
        "Escolha o gênero do filme",
        ('Ação', 'Comédia', 'Suspense', 'Terror'))

    page = st.button('Próximo')
    form = st.button('Limpar Formulário')


st.experimental_rerun()