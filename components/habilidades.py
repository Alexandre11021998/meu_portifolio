import streamlit as st

def render_habilidades():
    # --- ÂNCORA HABILIDADES ---
    st.markdown('<div id="habilidades"></div>', unsafe_allow_html=True)

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