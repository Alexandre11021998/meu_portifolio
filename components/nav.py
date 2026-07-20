import streamlit as st

def render_navegacao():
    # Inicializa o estado do menu aberto/fechado
    if "menu_aberto" not in st.session_state:
        st.session_state.menu_aberto = False

    # CSS para posicionar o botão fixo no canto superior direito e esconder o menu antigo
    st.markdown("""
        <style>
            /* Remove o topo padrão do Streamlit */
            header, [data-testid="stHeader"], .stAppHeader {
                display: none !important;
            }
            
            /* Remove de vez as letras azuis antigas */
            .navbar, .nav-links, .nav-item {
                display: none !important;
            }

            /* --- FIXAÇÃO DO BOTÃO NO CANTO SUPERIOR DIREITO --- */
            div[data-testid="element-container"]:has(button[key="btn_hamburguer"]) {
                position: absolute !important;
                top: 15px !important;
                right: 15px !important;
                z-index: 999999 !important;
                width: auto !important;
            }

            /* Estilo visual do botão */
            button[key="btn_hamburguer"] {
                background-color: #1e231e !important;
                border: 1px solid rgba(65, 65, 5, 0.6) !important;
                color: #FFFFFF !important;
                padding: 5px 15px !important;
            }
            
            button[key="btn_hamburguer"]:hover {
                border-color: #bc9346 !important;
                color: #bc9346 !important;
                background-color: #1e231e !important;
            }
            
            /* Container do Menu Dropdown */
            .menu-dropdown-container {
                background-color: #1e231e;
                border: 1px solid rgba(65, 65, 5, 0.6);
                border-radius: 8px;
                padding: 10px;
                margin-top: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Renderiza a Logo alinhada à esquerda normalmente
    st.markdown("""
        <div style="font-family: 'Source Sans Pro', sans-serif; font-size: 24px; font-weight: 700; letter-spacing: 1.5px; padding-top: 5px; margin-bottom: 15px;">
            <span style="color: #FFFFFF;">ALEXANDRE.</span><span style="color: #414105;">DEV</span>
        </div>
    """, unsafe_allow_html=True)

    # Cria o botão de alternância do menu (ele vai direto para o canto superior direito via CSS)
    texto_botao = "✖ Fechar" if st.session_state.menu_aberto else "☰ Menu"
    if st.button(texto_botao, key="btn_hamburguer"):
        st.session_state.menu_aberto = not st.session_state.menu_aberto
        st.rerun()

    # Se o menu estiver aberto, mostra os botões de navegação
    if st.session_state.menu_aberto:
        with st.container():
            st.markdown('<div class="menu-dropdown-container">', unsafe_allow_html=True)
            
            # Funções para fechar o menu e rolar a página
            if st.button("Início", use_container_width=True, key="lnk_inicio"):
                st.session_state.menu_aberto = False
                st.markdown('<script>window.location.href="#inicio";</script>', unsafe_allow_html=True)
                st.rerun()
                
            if st.button("Habilidades", use_container_width=True, key="lnk_hab"):
                st.session_state.menu_aberto = False
                st.markdown('<script>window.location.href="#habilidades";</script>', unsafe_allow_html=True)
                st.rerun()
                
            if st.button("Projetos", use_container_width=True, key="lnk_proj"):
                st.session_state.menu_aberto = False
                st.markdown('<script>window.location.href="#projetos";</script>', unsafe_allow_html=True)
                st.rerun()
                
            if st.button("Contato", use_container_width=True, key="lnk_cont"):
                st.session_state.menu_aberto = False
                st.markdown('<script>window.location.href="#contato";</script>', unsafe_allow_html=True)
                st.rerun()
                
            st.markdown('</div>', unsafe_allow_html=True)

    # Linha divisória
    st.markdown("<hr style='border: 0; border-top: 1px solid rgba(65, 65, 5, 0.3); margin: 5px 0 25px 0;'>", unsafe_allow_html=True)