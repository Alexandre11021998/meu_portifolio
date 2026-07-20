import streamlit as st

def render_navegacao():
    # 1. CSS Seguro: Apenas limpa cabeçalhos padrões e esconde o menu antigo de texto
    st.markdown("""
        <style>
            /* Remove o topo padrão do Streamlit */
            header, [data-testid="stHeader"], .stAppHeader {
                display: none !important;
            }
            
            /* Garante o sumiço definitivo daquelas letras azuis antigas */
            .navbar, .nav-links, .nav-item {
                display: none !important;
            }
            
            /* Estilização interna do botão do menu para combinar com seu tema */
            div[data-testid="element-container"] button {
                background-color: #1e231e !important;
                border: 1px solid rgba(65, 65, 5, 0.6) !important;
                color: #FFFFFF !important;
            }
            div[data-testid="element-container"] button:hover {
                border-color: #bc9346 !important;
                color: #bc9346 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 2. Cria a linha do topo usando colunas normais (Sem quebrar o grid da página)
    col_logo, col_menu = st.columns([6, 1])

    with col_logo:
        # Sua Logo alinhada à esquerda
        st.markdown("""
            <div style="font-family: 'Source Sans Pro', sans-serif; font-size: 24px; font-weight: 700; letter-spacing: 1.5px; padding-top: 5px;">
                <span style="color: #FFFFFF;">ALEXANDRE.</span><span style="color: #414105;">DEV</span>
            </div>
        """, unsafe_allow_html=True)

    with col_menu:
        # O botão do Menu que abre as opções nativamente e de forma limpa à direita
        with st.popover("☰ Menu", use_container_width=True):
            st.markdown('<a href="#inicio" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600; text-align: center;">Início</a>', unsafe_allow_html=True)
            st.markdown('<a href="#habilidades" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600; text-align: center;">Habilidades</a>', unsafe_allow_html=True)
            st.markdown('<a href="#projetos" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600; text-align: center;">Projetos</a>', unsafe_allow_html=True)
            st.markdown('<a href="#contato" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600; text-align: center;">Contato</a>', unsafe_allow_html=True)

    # Linha divisória sutil para organizar o layout
    st.markdown("<hr style='border: 0; border-top: 1px solid rgba(65, 65, 5, 0.3); margin: 15px 0 30px 0;'>", unsafe_allow_html=True)