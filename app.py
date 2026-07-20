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

# 2. Renderização das seções estruturadas com as âncoras para o menu

# --- SEÇÃO: INÍCIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
render_hero()

# --- SEÇÃO: HABILIDADES ---
st.markdown('<div id="habilidades"></div>', unsafe_allow_html=True)
render_habilidades()

# --- SEÇÃO: PROJETOS ---
st.markdown('<div id="projetos"></div>', unsafe_allow_html=True)
render_projetos() # Nota: Ajustado para o nome da função que você importou acima (render_projetos)

# --- SEÇÃO: CONTATO ---
st.markdown('<div id="contato"></div>', unsafe_allow_html=True)
# Se você for reativar o quadro de contato futuramente, a âncora já está no lugar certo
# render_quadro_contato() 
render_rodape_redes()