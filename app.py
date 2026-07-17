import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="ALEXANDRE.DEV", page_icon="🅰️", layout="centered")

# FUNDO DEGRADÊ + MARCA
st.markdown(
    """
    <style>
    /* Alvo principal do fundo do app */
    .stApp {
        background: linear-gradient(180deg, #3B443B 0%, #000000 100%);
        background-attachment: local; /* Faz o degradê acompanhar a rolagem */
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
        z-index: 999999; /* Garante que fique acima de outros elementos */
        background: transparent; /* Fundo transparente para não interferir no degradê */
    }
    .logo-white{
    
        color: #FFFFFF; /* Cor branca para o texto */
    }
    .logo-olive{
        color: #414105; /* Cor oliva para o texto */

        /*FOTO DE PERFIL*/

    .circular-profile-pic{
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
        width: 160px;
        height: 160px;
        border-radius: 50%; /* Torna a imagem circular */
        border: 5px solid #414105;
        object-fit: cover; /* Garante que a imagem preencha o círculo sem distorção */
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3); /* Adiciona uma sombra para dar profundidade */
    }
    }
    /* Ajuste para telas de celular (para o logo não bater nos botões nativos do Streamlit se a tela for muito pequena) */
    @media (max-width: 768px) {
        .custom-logo {
            position: absolute;
            top: 10px;
            left: 15px;
            font-size: 18px;
        }
    </style>
    <div class="custom-logo">
        <span class="logo-white">ALEXANDRE.</span><span class="logo-olive">DEV</span>
    </div>
    """,
    unsafe_allow_html=True
)




# 2. Cabeçalho (Sobre mim)
st.markdown('<img src="assets/profile.png" class="circular-profile-pic">', unsafe_allow_html=True)
st.title("Olá, meu nome é Alexandre!")
st.subheader("Sou um desenvolvedor apaixonado por tecnologia, inovação e por resolver problemas reais através do código. Seja bem-vindo ao meu portfólio digital!")

st.write(""" Combinando uma base sólida em suporte de TI e infraestrutura com o desenvolvimento de software, hoje eu foco na criação de aplicações web eficientes e modernas utilizando TypeScript, Next.js e Node.js. Além disso, adoro construir automações inteligentes com IA e n8n para transformar processos manuais em fluxos digitais otimizados.""")

# Botão para baixar currículo
st.download_button(label="Baixar Currículo", data="Seu curriculo aqui", file_name="CURRICULO_TI.pdf")

st.markdown("---")

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

# 5. CONTATO
st.header("Vamos nos conectar?")
st.write("Sinta-se à vontade para entrar em contato através de qualquer uma das redes abaixo:")

col_linkedin, col_github, col_email = st.columns(3)

with col_linkedin:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/alexandre-vinicius-costa-0a6422405/", type="primary")

with col_github:
    st.link_button("GitHub", "https://github.com/Alexandre11021998", type="primary"         )

with col_email:
    # Como e-mail não é um link clicável de navegador comum, um botão informativo fica ótimo
    st.button("costav.alexandre@gmail.com", disabled=True)