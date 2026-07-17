# styles.py
import streamlit as st

def init_custom_theme():
    """Injeta o fundo degradê, a marca fixa e os estilos customizados."""
    st.markdown(
        """
        <style>
        /* Alvo principal do fundo do app */
        .stApp {
            background: linear-gradient(180deg, #3B443B 0%, #000000 100%);
            background-attachment: local;
        }

        /* ALEXANDRE.DEV - Marca no topo */
        .custom-logo {
            position: fixed;
            top: 20px;
            left: 30px;
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 22px;
            font-weight: 700;
            letter-spacing: 1.5px;
            z-index: 999999;
            background: transparent;
        }
        
        .logo-white {
            color: #FFFFFF;
        }
        
        .logo-olive {
            color: #414105;
        }

        /* FOTO DE PERFIL (Corrigido o aninhamento inválido do CSS) */
        .circular-profile-pic {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 20px;
            width: 160px;
            height: 160px;
            border-radius: 50%;
            border: 5px solid #414105;
            object-fit: cover;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
        }

        /* Ajuste para telas de celular */
        @media (max-width: 768px) {
            .custom-logo {
                position: absolute;
                top: 10px;
                left: 15px;
                font-size: 18px;
            }
        }
        </style>
        
        <div class="custom-logo">
            <span class="logo-white">ALEXANDRE.</span><span class="logo-olive">DEV</span>
        </div>
        """,
        unsafe_allow_html=True
    )