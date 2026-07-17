import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="ALEXANDRE.DEV", page_icon="🅰️", layout="centered")

# 2. Cabeçalho (Sobre mim)
st.title("Olá, meu nome é Alexandre!")
st.subheader("Sou um desenvolvedor apaixonado por tecnologia, inovação e por resolver problemas reais através do código. Seja bem-vindo ao meu portfólio digital!")

st.write(""" Combinando uma base sólida em suporte de TI e infraestrutura com o desenvolvimento de software, hoje eu foco na criação de aplicações web eficientes e modernas utilizando TypeScript, Next.js e Node.js. Além disso, adoro construir automações inteligentes com IA e n8n para transformar processos manuais em fluxos digitais otimizados.""")

    # Botão para baixar currículo
st.download_button(label="Baixar Currículo", data="Seu curriculo aqui", file_name="CURRICULO_TI.pdf")

st.markdown("---")

   # . 3. Seção de Habilidades
st.header("Habilidades Técnicas")
   # Organizando em colunas para melhor visualização
col1, col2, col3 = st.columns(3)

with col1:
        st.subheader("Linguagens e Frameworks")
        st.write("- Python")
        st.write("- JavaScript")
        st.write("- Typescript")
        st.write("- React")
        st.write("- Node.js")
        st.write("- Tailwind CSS")
        st.write("- Pandas")

with col2:
        st.subheader("Banco de dados")
        st.write("- SQL")
        st.write("- PostgreSQL")
        st.write("- Prisma ORM")
    
with col3:
        st.subheader("Ferramentas e Gestões")
        st.write("- Git e GitHub")
        st.write("- Scrum e Kanban")
        st.write("- AWS")
        st.write("- ITIL, PMBOK e COBIT")
        st.write("- N8N")
        
st.markdown("---")

    #PROJETOS EM DESTAQUE
st.header("Projetos em Destaque")

    # PORTIFÓLIO DE PROJETOS
st.subheader("1. Este Portfólio Interativo")
st.write(
    "Aplicação web desenvolvida em Python com Streamlit para centralizar meus projetos, "
    "experiências e formas de contato de maneira dinâmica."
)
st.markdown("[Ver código no GitHub](https://github.com/Alexandre11021998/meu_portifolio)")

st.write("") # Espaçamento

# Key_Master
st.subheader("2. Key_Master - Gerenciameto de ativos logisticos")
st.write( "Sistema de gestão de chaves para entrega e retirada, permitindo o controle de forma eficiente e segura."
)
st.write(" Tecnologias: React, PostgreSQL, GitHub Actions") 
st.write("Impacto: Digitalização de processos manuais reduzindo tempo de cadastro e procura.")
st.markdown("[Ver código no GitHub](https://github.com/Alexandre11021998/keymaster)")
st.markdown("[Acesse o site aqui ](https://keywarden-hub.lovable.app/)")
# Espaçamento

st.markdown("---")

# Zelo
st.subheader("3. Zelo - Sistema de Gerenciamento Hospitalar")
st.write(
    "Sistema de gerenciamento hospitalar desenvolvido para otimizar o fluxo de trabalho, "
    "permitindo a consulta eficiente de pacientes e status."
   
)
st.write("Tecnologias: Next.js, TypeScript, Node.js, PostgreSQL, Prisma ORM, Tailwind CSS")
st.write("Impacto: Melhorou a eficiência operacional e a experiência do paciente.")
st.markdown("[Ver código no GitHub](https://github.com/Alexandre11021998/Zelo)")
st.markdown("[Acesse o site aqui ](https://zelo-hub.lovable.app/)")

# LicitIA
st.subheader("4. LicitIA - Sistema de triagem de licitações com automtizada")
st.write(
    "Sistema de triagem de licitações utilizando inteligência artificial para automatizar a análise de documentos e identificar oportunidades relevantes."
)
st.write("Tecnologias: n8n, Inteligência Artificial, JavaScript, Engenharia de Prompt, JSON, API’s")
st.write("Impacto: Redução do tempo de triagem de documentos de horas para menos de 30 segundos, mitigando o risco de erro humano na análise de cláusulas restritivas.")
st.markdown("[Ver código no GitHub](https://github.com/Alexandre11021998/licitai-triagem-editais)")
# Ferramentas na mão
st.subheader("5. Ferramentas na Mão - Aplicativo de Aluguel de Ferramentas")
st.write(
    "Aplicativo de aluguel de ferramentas que conecta usuários a uma rede de prestadores de serviços, permitindo o aluguel rápido e seguro de ferramentas."
)
st.write("Tecnologias: Next.js, Node.js, PostgreSQL, Prisma")
st.markdown("[Ver código no GitHub](https://github.com/Alexandre11021998/ferramentas-na-mao)")
st.markdown("[Acesse o site aqui ](https://ferramenta-na-m-o.vercel.app/?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQMMjU2MjgxMDQwNTU4AAGngKOYbZ8cKrPZkQQoPfi625amgQWCiYU0imwO-OS_hmpSNkoRL66D6GpXdbA_aem_ld0Z08M3kckLDZK39cfGdQ)")

# CONTATO
st.header("Vamos nos conectar?")
st.write("Sinta-se à vontade para entrar em contato através de qualquer uma das redes abaixo:")

col_linkedin, col_github, col_email = st.columns(3)

with col_linkedin:
    st.markdown("[LinkedIn](https://www.linkedin.com/in/alexandre-vinicius-costa-0a6422405/)")

with col_github:
    st.markdown("[GitHub](https://github.com/Alexandre11021998)")

with col_email:
    st.write("costav.alexandre@gmail.com")
        
