import streamlit as st

def render_navegacao():
    # 1. Remove as barras e cabeçalhos padrões do Streamlit
    st.markdown("""
        <style>
            header, [data-testid="stHeader"], .stAppHeader {
                display: none !important;
            }
            /* Corrige o espaçamento do topo da página */
            .block-container {
                padding-top: 2rem !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 2. Cria uma linha horizontal para servir de Navbar usando colunas nativas
    # col_logo cuida do nome (Alexandre) e col_menu cuida do botão no canto direito
    col_logo, col_menu = st.columns([8, 1])

    with col_logo:
        # Renderiza apenas a sua logo bonita usando HTML simples
        st.markdown("""
            <div style="font-family: 'Source Sans Pro', sans-serif; font-size: 22px; font-weight: 700; letter-spacing: 1.5px;">
                <span style="color: #FFFFFF;">ALEXANDRE.</span><span style="color: #414105;">DEV</span>
            </div>
        """, unsafe_allow_html=True)

    with col_menu:
        # st.popover cria o botão perfeito de menu e abre um container limpo ao ser clicado
        with st.popover("☰", use_container_width=False):
            # Links estilizados como botões para navegação rápida por âncoras
            st.markdown('<a href="#inicio" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600;">Início</a>', unsafe_allow_html=True)
            st.markdown('<a href="#habilidades" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600;">Habilidades</a>', unsafe_allow_html=True)
            st.markdown('<a href="#projetos" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600;">Projetos</a>', unsafe_allow_html=True)
            st.markdown('<a href="#contato" target="_self" style="color: white; text-decoration: none; display: block; padding: 10px 0; font-weight: 600;">Contato</a>', unsafe_allow_html=True)

    # Linha sutil para dividir a navbar do conteúdo, combinando com o seu tema
    st.markdown("<hr style='border: 0; border-top: 1px solid rgba(65, 65, 5, 0.3); margin-top: 10px; margin-bottom: 30px;'>", unsafe_allow_html=True)