import streamlit as st

# Configurações da aba do navegador
st.set_page_config(
    page_title="Calcular IRA",
    page_icon="icon.webp"
)

# Inicializa a lista de disciplinas no session_state se ainda não existir
if "disciplinas" not in st.session_state:
    st.session_state.disciplinas = []

# Cabeçalho
st.title("Calcule seu IRA")
st.text("O Índice de Rendimento Acadêmico (IRA) é uma média ponderada que avalia o desempenho do estudante ao longo de um curso. Ele considera as notas obtidas em cada disciplina e a carga horária (créditos) correspondente. Quanto maior o IRA, melhor o desempenho acadêmico. Esta ferramenta permite calcular o IRA de forma simples, inserindo as notas e os créditos das disciplinas cursadas.")

st.subheader("Adicionar Disciplinas: ")
# Inputs para o formulário
with st.form("inputs"):
    disciplina = st.text_input("Nome da disciplina: ")
    creditos = st.number_input("Créditos da disciplina:", min_value=1, step=1)
    nota = st.number_input("Nota da disciplina:", min_value=0.0, max_value=10.0, step=0.1)
    adicionar = st.form_submit_button("Adicionar")
    limpar_disciplinas = st.form_submit_button("Limpar disciplinas")

    # Adicionar disciplina
    if adicionar:
        if disciplina and nota >= 0 and creditos > 0:
            st.session_state.disciplinas.append((disciplina, creditos, nota))
            st.success(f"Disciplina '{disciplina}' adicionada com sucesso!")
        else:
            st.error("Preencha todos os campos corretamente.")

    # Limpar disciplinas
    if limpar_disciplinas:
        st.session_state.disciplinas = []
        st.success("Todas as disciplinas foram removidas.")

# Mostrar disciplinas adicionadas
st.subheader("Disciplinas Adicionadas")
if st.session_state.disciplinas:
    for i, (nome, creditos, nota) in enumerate(st.session_state.disciplinas, 1):
        st.write(f"{i}. Nome: {nome} | Créditos: {creditos} | Nota: {nota}")
else:
    st.write("Nenhuma disciplina adicionada ainda.")

# Função para calcular o IRA
def calcular_ira():
    total_nota_credito = 0
    total_creditos = 0
    for nome, creditos, nota in st.session_state.disciplinas:
        total_nota_credito += nota * creditos
        total_creditos += creditos
    if total_creditos > 0:
        ira = total_nota_credito / total_creditos
        st.success(f"O seu IRA é: {ira:.2f}")
    else:
        st.error("Não há disciplinas suficientes para calcular o IRA.")

calcular = st.button("Calcular IRA")
if calcular:
    calcular_ira()

# Rodapé da página
st.markdown("---")
st.markdown("Desenvolvido por: [Guilherme Wagner](https://www.linkedin.com/in/guilherme-wagner)")
