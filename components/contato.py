import streamlit as st

@st.dialog("Vamos tirar o seu projeto do papel?")
def render_quadro_contato():
              
        st.write("Se você tem uma ideia inovadora, um desafio técnico ou precisa otimizar seus processos através de automações inteligentes, escolha como prefere falar comigo:")
        
        col_wa, col_lnk, col_mail = st.columns(3)
        
        with col_wa:
            texto_whatsapp = "Olá Alexandre! Vi seu portfólio e gostaria de iniciar um projeto."
            link_whatsapp = f"https://wa.me/55419998135013?text={texto_whatsapp.replace(' ', '%20')}"
            st.link_button("WhatsApp", link_whatsapp, use_container_width=True, type="primary")
            
        with col_lnk:
            st.link_button("LinkedIn", "https://www.linkedin.com/in/alexandre-vinicius-costa-0a6422405/", use_container_width=True, type="secondary")
            
        with col_mail:
            st.link_button("E-mail", "mailto:costav.alexandre@gmail.com", use_container_width=True, type="secondary")

def render_rodape_redes():
    # --- ÂNCORA CONTATO ---
    st.markdown('<div id="contato"></div>', unsafe_allow_html=True)

    st.header("Vamos nos conectar?")
    st.write("Sinta-se à vontade para entrar em contato através de qualquer uma das redes abaixo:")

    col_linkedin, col_github, col_email = st.columns(3)

    with col_linkedin:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/alexandre-vinicius-costa-0a6422405/", type="primary")

    with col_github:
        st.link_button("GitHub", "https://github.com/Alexandre11021998", type="primary")

    with col_email:
        st.button("costav.alexandre@gmail.com", disabled=True)