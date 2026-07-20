import streamlit as st
from style import init_custom_theme

# Importando os componentes modulares
from components.nav import render_navegacao
from components.hero import render_hero
from components.contato import render_quadro_contato, render_rodape_redes
from components.habilidades import render_habilidades
from components.projetos import render_projetos

# 1. Configuração global da página
st.set_page_config(page_title="ALEXANDRE.DEV", page_icon="🅰", layout="centered")
st.markdown("<style>html { scroll-behavior: smooth; }</style>", unsafe_allow_html=True)

# Injeta os Temas CSS customizados
init_custom_theme()

# Injeta a Navbar responsiva fixa no topo (Computador e Celular)
render_navegacao()

# 2. Renderização das seções estruturadas
render_hero()

#render_quadro_contato()

render_habilidades()

render_projetos()

render_rodape_redes()