# styles.py
import streamlit as st

def init_custom_theme():
    """Injeta o fundo degradê, o menu de navegação fixo e os estilos do cabeçalho de perfil."""
    st.markdown(
        """
        <style>
        /* Fundo do app */
        .stApp {
            background: linear-gradient(180deg, #3B443B 0%, #000000 100%);
            background-attachment: local;
        }

        /* BARRA DE NAVEGAÇÃO FIXA NO TOPO */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 40px;
            z-index: 999999;
            background: rgba(59, 68, 59, 0.4); /* Fundo sutil com blur */
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(65, 65, 5, 0.2);
        }
        
        /* Logo (Lado Esquerdo) */
        .logo-container {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 22px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-decoration: none !important;
        }
        .logo-white { color: #FFFFFF; }
        .logo-olive { color: #414105; }

        /* Links de Menu (Lado Direito) */
        .nav-links {
            display: flex;
            gap: 25px;
        }
        .nav-item {
            color: #A0AEC0;
            text-decoration: none !important;
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 15px;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        .nav-item:hover {
            color: #FFFFFF; /* Muda para branco ao passar o mouse */
        }

        /* --- CONTAINER CENTRALIZADO DO PERFIL --- */
        .profile-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            margin-top: 60px; /* Adicionado para não ficar coberto pela navbar fixa */
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

        /* Força a centralização de títulos específicos do topo se necessário */
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

        @media (max-width: 768px) {
            .navbar {
                padding: 15px 20px;
            }
            .logo-container {
                font-size: 18px;
            }
            .nav-links {
                gap: 15px;
            }
            .nav-item {
                font-size: 13px;
            }
        }
        </style>
        
        <div class="navbar">
            <a href="#inicio" class="logo-container">
                <span class="logo-white">ALEXANDRE.</span><span class="logo-olive">DEV</span>
            </a>
            <div class="nav-links">
                <a href="#inicio" class="nav-item">Início</a>
                <a href="#habilidades" class="nav-item">Habilidades</a>
                <a href="#projetos" class="nav-item">Projetos</a>
                <a href="#contato" class="nav-item">Contato</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )