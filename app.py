import streamlit as st
from style import init_custom_theme

# 1. Configuração da página
st.set_page_config(page_title="ALEXANDRE.DEV", page_icon="🅰️", layout="centered")

init_custom_theme()

# --- ÂNCORA INÍCIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)

# 2. Cabeçalho (Sobre mim)
st.markdown(
    """
    <div class="profile-container">
        <img src="assets/profile.png" class="circular-profile-pic">
        <div class="status-badge">Disponível para Projetos</div>
    </div>
    """,
    unsafe_allow_html=True
)
st.subheader("Sou um desenvolvedor apaixonado por tecnologia, inovação e por resolver problemas reais através do código. Seja bem-vindo ao meu portfólio digital!")

st.write(""" Combinando uma base sólida em suporte de TI e infraestrutura com o desenvolvimento de software, hoje eu foco na criação de aplicações web eficientes e modernas utilizando TypeScript, Next.js e Node.js. Além disso, adoro construir automações inteligentes com IA e n8n para transformar processos manuais em fluxos digitais otimizados.""")

# Botão para baixar currículo
st.download_button(label="Baixar Currículo", data="Seu curriculo aqui", file_name="CURRICULO_TI.pdf")

st.write("")

col_esq, col_btn1, col_btn2, col_dir = st.columns([1.5, 2, 2, 1.5])

with col_btn1:
    if st.button("Iniciar Projeto",type="primary", use_container_width=True):
        st.info("Ação de iniciar projeto sera configurada em breve")
        
with col_btn2:
    if st.button("Ver Projetos", type="secondary", use_container_width=True):
        st.info("Ação de ver projetos sera configurada em breve")        
st.markdown("---")

st.write("") # Um pequeno espaço em branco antes do quadro

with st.container(border=True):
    st.subheader("Vamos tirar o seu projeto do papel?")
    st.write("Se você tem uma ideia inovadora, um desafio técnico ou precisa otimizar seus processos através de automações inteligentes, escolha como prefere falar comigo:")
    
    # Criando 3 colunas para colocar todos os botões lado a lado e organizados
    col_wa, col_lnk, col_mail = st.columns(3)
    
    with col_wa:
        # Botão principal (Verde Oliva em Destaque)
        texto_whatsapp = "Olá Alexandre! Vi seu portfólio e gostaria de iniciar um projeto."
        link_whatsapp = f"https://wa.me/55419998135013?text={texto_whatsapp.replace(' ', '%20')}"
        st.link_button("WhatsApp", link_whatsapp, use_container_width=True, type="primary")
        
    with col_lnk:
        # Botão Secundário (Transparente / Outline)
        st.link_button("LinkedIn", "https://www.linkedin.com/in/alexandre-vinicius-costa-0a6422405/", use_container_width=True, type="secondary")
        
           
    with col_mail:
        # Botão Secundário que abre o app de e-mail do cliente já preenchido
        st.link_button("E-mail", "mailto:costav.alexandre@gmail.com", use_container_width=True, type="secondary")
# --- ÂNCORA HABILIDADES ---
st.markdown('<div id="habilidades"></div>', unsafe_allow_html=True)

# 3. Seção de Habilidades
st.header("Habilidades Técnicas")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Linguagens/Frameworks")
    st.write("- Python\n- JavaScript\n- TypeScript\n- React\n- Node.js\n- Tailwind CSS\n- Pandas")

with col2:
    st.markdown("### Banco de Dados")
    st.write("- SQL\n- PostgreSQL\n- Prisma ORM")
    
with col3:
    st.markdown("### Ferramentas/Gestão")
    st.write("- Git e GitHub\n- Scrum e Kanban\n- AWS\n- ITIL, PMBOK e COBIT\n- N8N")
        
st.markdown("---")


# --- ÂNCORA PROJETOS ---
st.markdown('<div id="projetos"></div>', unsafe_allow_html=True)

# 4. Projetos em Destaque
st.header("Projetos em Destaque")

# PROJETO 1 (Destaque principal no topo)
st.subheader("1. Este Portfólio Interativo")
st.write(
    "Aplicação web desenvolvida em Python com Streamlit para centralizar meus projetos, "
    "experiências e formas de contato de maneira dinâmica."
)
st.link_button("Ver código no GitHub", "https://github.com/Alexandre11021998/meu_portifolio", type="primary")
st.write("") 

# Organizando Projetos 2 e 3 lado a lado
col_p2, col_p3 = st.columns(2)

with col_p2:
    st.subheader("2. Key_Master")
    st.caption("Gerenciamento de ativos logísticos")
    st.write("Sistema de gestão de chaves para entrega e retirada, permitindo o controle de forma eficiente e segura.")
    st.image("assets/key_master.png", caption="Interface inicial do Key_Master", use_container_width=True)
    st.write("**Tecnologias:** React, PostgreSQL, GitHub Actions") 
    st.write("**Impacto:** Digitalização de processos manuais reduzindo tempo de cadastro e procura.")
    st.link_button("Código no GitHub", "https://github.com/Alexandre11021998/keymaster", type="primary")
    st.link_button("Acesse o site", "https://keywarden-hub.lovable.app/", type="primary")

with col_p3:
    st.subheader("3. Zelo")
    st.caption("Gerenciamento Hospitalar")
    st.write("Sistema de gerenciamento hospitalar desenvolvido para otimizar o fluxo de trabalho, permitindo a consulta eficiente de pacientes e status.")
    st.image("assets/zelo.png", caption="Interface inicial do Zelo", use_container_width=True)
    st.write("**Tecnologias:** Next.js, TypeScript, Node.js, PostgreSQL, Prisma ORM, Tailwind CSS")
    st.write("**Impacto:** Melhorou a eficiência operacional e a experiência do paciente.")
    st.link_button("Código no GitHub", "https://github.com/Alexandre11021998/Zelo", type="primary")
    st.link_button("Acesse o site", "https://zelo-hub.lovable.app/", type="primary")

st.write("") 

# Organizando Projetos 4 e 5 lado a lado
col_p4, col_p5 = st.columns(2)

with col_p4:
    st.subheader("4. LicitIA")
    st.caption("Triagem de licitações automatizada")
    st.write("Sistema de triagem de licitações utilizando inteligência artificial para automatizar a análise de documentos e identificar oportunidades relevantes.")
    st.image("assets/licitai.png", caption="Interface inicial do LicitIA", use_container_width=True)
    st.write("**Tecnologias:** n8n, Inteligência Artificial, JavaScript, Engenharia de Prompt, JSON, API’s")
    st.write("**Impacto:** Redução do tempo de triagem de documentos de horas para menos de 30 segundos, mitigando o risco de erro humano.")
    st.link_button("Código no GitHub", "https://github.com/Alexandre11021998/licitai-triagem-editais", type="primary")

with col_p5:
    st.subheader("5. Ferramentas na Mão")
    st.caption("Aluguel de Ferramentas")
    st.write("Aplicativo de aluguel de ferramentas que conecta usuários a uma rede de prestadores de serviços, permitindo o aluguel rápido e seguro de ferramentas.")
    st.image("assets/ferramentas_na_mao.png", caption="Interface inicial do Ferramentas na Mão", use_container_width=True)
    st.write("**Tecnologias:** Next.js, Node.js, PostgreSQL, Prisma")
    st.write("") # ajuste de espaçamento
    st.link_button("Código no GitHub", "https://github.com/Alexandre11021998/ferramentas-na-mao", type="primary")
    st.link_button("Acesse o site", "https://ferramenta-na-m-o.vercel.app/?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQMMjU2MjgxMDQwNTU4AAGngKOYbZ8cKrPZkQQoPfi625amgQWCiYU0imwO-OS_hmpSNkoRL66D6GpXdbA_aem_ld0Z08M3kckLDZK39cfGdQ", type="primary" )

st.markdown("---")


# --- ÂNCORA CONTATO ---
st.markdown('<div id="contato"></div>', unsafe_allow_html=True)

# 5. CONTATO
st.header("Vamos nos conectar?")
st.write("Sinta-se à voltar para entrar em contato através de qualquer uma das redes abaixo:")

col_linkedin, col_github, col_email = st.columns(3)

with col_linkedin:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/alexandre-vinicius-costa-0a6422405/", type="primary")

with col_github:
    st.link_button("GitHub", "https://github.com/Alexandre11021998", type="primary")

with col_email:
    st.button("costav.alexandre@gmail.com", disabled=True)