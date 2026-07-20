import streamlit as st

def render_navegacao():
    # 1. CSS Corretor para limpar o topo padrão do Streamlit
    st.markdown("""
        <style>
            header, [data-testid="stHeader"], .stAppHeader {
                display: none !important;
            }
            .navbar, .nav-links, .nav-item {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 2. Renderiza apenas a Logo alinhada à esquerda
    st.markdown("""
        <div style="font-family: 'Source Sans Pro', sans-serif; font-size: 22px; font-weight: 700; letter-spacing: 1.5px; padding-top: 5px; margin-bottom: 5px;">
            <span style="color: #FFFFFF;">ALEXANDRE.</span><span style="color: #414105;">DEV</span>
        </div>
    """, unsafe_allow_html=True)

    # Linha divisória sutil abaixo da logo
    st.markdown("<hr style='border: 0; border-top: 1px solid rgba(65, 65, 5, 0.3); margin: 15px 0 25px 0;'>", unsafe_allow_html=True)