import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Meu Portfólio", page_icon="💻", layout="centered")

# Cabeçalho / Apresentação
st.title("Olá, bem-vindo ao meu Portfólio! 👋")
st.write("Aqui você vai encontrar meus principais projetos e formas de entrar em contato.")

# Seção de Projetos (Exemplo Inicial)
st.header("🛠️ Meus Projetos")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Projeto 1")
    st.write("Descrição rápida do seu projeto de automação ou análise de dados.")
    st.link_button("Ver no GitHub", "https://github.com")

with col2:
    st.subheader("Projeto 2")
    st.write("Descrição rápida do seu projeto web ou sistema completo.")
    st.link_button("Ver no GitHub", "https://github.com")