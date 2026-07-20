import streamlit as st

def render_navegacao():
    # 1. Injeção de CSS agressivo para esconder o menu duplicado e arrumar o layout
    st.markdown("""
        <style>
            /* 1. Esconde as barras nativas padrões do Streamlit */
            header, [data-testid="stHeader"], .stAppHeader {
                display: none !important;
            }
            
            /* 2. FORÇA O SUMIÇO DO MENU COM AS LETRAS (Início, Habilidades, Projetos...) */
            /* Isso vai caçar qualquer div antiga ou texto que esteja no topo e ocultá-lo */
            .navbar, .nav-links, .nav-item {
                display: none !important;
            }
            
            /* 3. PEGA A BARRA ESCURA DO TOPO E FAZ DELA A NOSSA NAVBAR OFICIAL */
            /* Garante que o topo da tela seja limpo e fixo */
            div[data-testid="stHorizontalBlock"]:first-of-type {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                width: 100% !important;
                z-index: 99999 !important;
                background: #111111 !important; /* Cor idêntica à sua barra escura */
                padding: 10px 40px !important;
                border-bottom: 1px solid rgba(65, 65, 5, 0.2);
                box-sizing: border-box;
            }

            /* 4. SELECIONA O BOTÃO POP-OVER E JOGA ELE PARA O CANTO SUPERIOR DIREITO */
            div[data-testid="element-container"]:has(button[dir="ltr"]) {
                position: fixed !important;
                top: 12px !important;
                right: 40px !important;
                z-index: 100000 !important;
                margin: 0 !important;
            }

            /* Estiliza o botão do popover para parecer um ícone de menu limpo */
            div[data-testid="element-container"] button[dir="ltr"] {
                background-color: transparent !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                color: #FFFFFF !important;
                border-radius: 4px !important;
                padding: 4px 12px !important;
            }

            div[data-testid="element-container"] button[dir="ltr"]:hover {
                border-color: #bc9346 !important;
                color: #bc9346 !important;
            }
            
            /* Adiciona um recuo para o conteúdo do portfólio não sumir atrás da barra fixa */
            .block-container {
                padding-top: 5rem !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 2. Layout da Navbar usando colunas nativas do Streamlit
    col_logo, col_menu = st.columns([8, 1])

    with col_logo:
        # Renderiza sua logo
        st.markdown("""
            <div style="font-family: 'Source Sans Pro', sans-serif; font-size: 22px; font-weight: 700; letter-spacing: 1.5px; margin-top: 5px;">
                <span style="color: #FFFFFF;">ALEXANDRE.</span><span style="color: #414105;">DEV</span>
            </div>
        """, unsafe_allow_html=True)

    with col_menu:
        # Cria o botão "☰" nativo que abre o menu suspenso ao ser clicado
        with st.popover("☰", use_container_width=False):
            st.markdown('<a href="#inicio" target="_self" style="color: white; text-decoration: none; display: block; padding: 8px 0; font-weight: 600;">Início</a>', unsafe_allow_html=True)
            st.markdown('<a href="#habilidades" target="_self" style="color: white; text-decoration: none; display: block; padding: 8px 0; font-weight: 600;">Habilidades</a>', unsafe_allow_html=True)
            st.markdown('<a href="#projetos" target="_self" style="color: white; text-decoration: none; display: block; padding: 8px 0; font-weight: 600;">Projetos</a>', unsafe_allow_html=True)
            st.markdown('<a href="#contato" target="_self" style="color: white; text-decoration: none; display: block; padding: 8px 0; font-weight: 600;">Contato</a>', unsafe_allow_html=True)