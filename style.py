# styles.py
import streamlit as st

def init_custom_theme():
    """Injeta o fundo degradê e os estilos do cabeçalho de perfil."""
    st.markdown(
        """
        <style>
        /* Fundo do app */
        .stApp {
            background: linear-gradient(180deg, #3B443B 0%, #000000 100%);
            background-attachment: local;
        }

        /* --- CONTAINER CENTRALIZADO DO PERFIL --- */
        .profile-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            margin-top: 60px;
            margin-bottom: 25px;
            width: 100%;
        }

        .circular-profile-pic {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            border: 5px solid #414105;
            object-fit: cover;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
            margin-bottom: 15px;
        }

        /* BADGE EM FORMATO DE PÍLULA CENTRALIZADA */
        .status-badge {
            display: inline-block;
            background-color: rgba(65, 65, 5, 0.3);
            color: #FFFFFF;
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 14px;
            font-weight: 500;
            padding: 6px 20px;
            border-radius: 50px;
            border: 1px solid rgba(65, 65, 5, 0.6);
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }

        .main-title {
            color: #FFFFFF;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 10px;
        }
        
        .main-subtitle {
            color: #A0AEC0;
            font-size: 1.25rem;
            font-weight: 400;
            max-width: 600px;
            margin: 0 auto;
        }

        /* Efeito de rolagem suave nativo */
        html {
            scroll-behavior: smooth;
        }
        </style>
        """,
        unsafe_allow_html=True
    )