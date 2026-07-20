import streamlit as st

def render_navegacao():
    # 1. CSS Corretor para limpar o topo e forçar o alinhamento perfeito do menu à direita
    st.markdown("""
        <style>
            header, [data-testid="stHeader"], .stAppHeader {
                display: none !important;
            }
            .navbar, .nav-links, .nav-item {
                display: none !important;
            }
            
            /* Ajusta o container das colunas para alinhar verticalmente ao centro */
            div[data-testid="stColumns"] {
                align-items: center !important;
            }
            
            /* Remove as bordas padrões do popover do Streamlit */
            div[data-testid="element-container"] button[dir="ltr"] {
                background-color: #1e231e !important;
                border: 1px solid rgba(65, 65, 5, 0.6) !important;
                color: #FFFFFF !important;
                margin-top: 0px !important; /* Garante alinhamento */
            }
            div[data-testid="element-container"] button[dir="ltr"]:hover {
                border-color: #bc9346 !important;
                color: #bc9346 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 2. Estrutura de colunas empurrando o menu totalmente para a direita
    # Aumentamos o peso do lado esquerdo (4) e diminuímos o do menu (1) para ele ir pro canto.
    col_logo, col_menu = st.columns([4, 1])

    with col_logo:
        st.markdown("""
            <div style="font-family: 'Source Sans Pro', sans-serif; font-size: 22px; font-weight: 700; letter-spacing: 1.5px; display: inline-block; vertical-align: middle;">
                <span style="color: #FFFFFF;">ALEXANDRE.</span><span style="color: #414105;">DEV</span>
            </div>
        """, unsafe_allow_html=True)

    with col_menu:
        # O popover agora fica alinhado à direita
        with st.popover("☰ Menu", use_container_width=True):
            st.markdown('<a href="#inicio" target="_self" style="color: white; text-decoration: none; display: block; padding: 12px 0; font-weight: 600; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05);">Início</a>', unsafe_allow_html=True)
            st.markdown('<a href="#habilidades" target="_self" style="color: white; text-decoration: none; display: block; padding: 12px 0; font-weight: 600; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05);">Habilidades</a>', unsafe_allow_html=True)
            st.markdown('<a href="#projetos" target="_self" style="color: white; text-decoration: none; display: block; padding: 12px 0; font-weight: 600; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.05);">Projetos</a>', unsafe_allow_html=True)
            st.markdown('<a href="#contato" target="_self" style="color: white; text-decoration: none; display: block; padding: 12px 0; font-weight: 600; text-align: center;">Contato</a>', unsafe_allow_html=True)

    # Linha divisória sutil
    st.markdown("<hr style='border: 0; border-top: 1px solid rgba(65, 65, 5, 0.3); margin: 15px 0 25px 0;'>", unsafe_allow_html=True)