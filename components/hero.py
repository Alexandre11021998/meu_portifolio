import streamlit as st
import base64
import os

from .contato import render_quadro_contato

def render_hero():
    # --- ÂNCORA INÍCIO ---
    st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)

    # 1. Caminho para a foto
    caminho_foto = "assets/profile.png"
    
    # 2. Lógica para converter a imagem em Base64 de forma segura
    img_base64 = ""
    if os.path.exists(caminho_foto):
        with open(caminho_foto, "rb") as image_file:
            img_base64 = base64.b64encode(image_file.read()).decode()
    
    # Cabeçalho (Sobre mim)
    # 3. CSS Injetado para garantir o círculo perfeito e o preenchimento
    st.markdown(
        f"""
        <style>
            .profile-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin-bottom: 20px;
            }}
            .circular-profile-pic {{
                width: 160px !important;
                height: 160px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                border: 3px solid #4CAF50 !important;
                display: block !important;
            }}
            .status-badge {{
                margin-top: 12px;
                /* Adicione aqui o restante do seu estilo para o badge se necessário */
            }}
        </style>
        
        <div class="profile-container">
            <img src="data:image/png;base64,{img_base64}" class="circular-profile-pic">
            <div class="status-badge">Disponível para Projetos</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.subheader("Sou um desenvolvedor apaixonado por tecnologia, inovação e por desenvolver soluções através do código. Seja bem-vindo ao meu portifólio digital!")

    st.write(""" Combinando uma base sólida em suporte de TI e infraestrutura com o desenvolvimento de software, hoje eu foco na criação de aplicações web eficientes e modernas utilizando TypeScript, Next.js e Node.js. Além disso, adoro construir automações inteligentes com IA e n8n para transformar processos manuais em fluxos digitais otimizados.""")

    # Botão para baixar currículo
    st.download_button(label="Baixar Currículo", data="Seu curriculo aqui", file_name="CURRICULO_TI.pdf")

    st.write("")

    col_esq, col_btn1, col_btn2, col_dir = st.columns([1.5, 2, 2, 1.5])

    with col_btn1:
     if st.button("Iniciar Projeto", type="primary", use_container_width=True):
        render_quadro_contato()
            
    with col_btn2:
    # Criamos um botão HTML customizado que aponta para #projetos na mesma aba
     with col_btn2:
      st.markdown(
        """
        <a href="#projetos" target="_self" style="text-decoration: none; width: 100%; display: block;">
            <button style="
                width: 100%;
                background-color: transparent;
                color: #606C38; 
                border: 1px solid currentColor;
                padding: 10px 16px;
                border-radius: 8px;
                cursor: pointer;
                font-weight: 500;
                font-size: 16px;
                opacity: 0.85; /* Dá um leve toque moderno de transparência */
                transition: all 0.2s ease-in-out;
            " onmouseover="this.style.borderColor='#ff4b4b'; this.style.color='#ff4b4b'; this.style.opacity='1';" 
               onmouseout="this.style.borderColor='currentColor'; this.style.color='inherit'; this.style.opacity='0.85';">
                Ver meus Projetos
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
            
    st.markdown("---")