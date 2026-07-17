import streamlit as st

def render_projetos():
    # --- ÂNCORA PROJETOS ---
    st.markdown('<div id="projetos"></div>', unsafe_allow_html=True)

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