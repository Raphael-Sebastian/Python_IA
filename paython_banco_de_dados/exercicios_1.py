import pymysql 

def listar_disciplinas():
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="sistema_escolar",
        cursorclass=pymysql.cursors.DictCursor
)

    try:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    d.disciplina_id,
                    d.nome_disciplina,
                    d.carga_horaria,
                    COUNT(m.matricula_id) AS num_alunos_matriculados
                FROM disciplinas d
                JOIN turmas t ON d.disciplina_id = t.disciplina_id
                JOIN matriculas m ON t.turma_id = m.turma_id AND m.status_matricula = 'Matriculado'
                GROUP BY d.disciplina_id, d.nome_disciplina, d.carga_horaria;
                """)
            disciplinas = cursor.fetchall()
    
    # Mostra os dados
        for disciplina in disciplinas:
            print(f"ID_disciplina: {disciplina['disciplina_id']} - Nome_disciplina: {disciplina['nome_disciplina']} - Carga_horaria: {disciplina['carga_horaria']} - Alunos matriculados: {disciplina['num_alunos_matriculados']}")
    finally:
        conexao.close()

listar_disciplinas()