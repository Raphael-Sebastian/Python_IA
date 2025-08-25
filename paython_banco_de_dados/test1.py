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
            sql = """
                SELECT 
                    d.disciplina_id,
                    d.nome_disciplina,
                    d.carga_horaria,
                    COUNT(m.matricula_id) AS num_alunos_matriculados
                FROM disciplinas d
                LEFT JOIN turmas t ON d.disciplina_id = t.disciplina_id
                LEFT JOIN matriculas m ON t.turma_id = m.turma_id AND m.status_matricula = 'Matriculado'
                GROUP BY d.disciplina_id, d.nome_disciplina, d.carga_horaria
                ORDER BY d.disciplina_id;
            """
            cursor.execute(sql)
            disciplinas = cursor.fetchall()

            print("Lista de Disciplinas:")
            for disciplina in disciplinas:
                print(f"ID: {disciplina['disciplina_id']} - "
                      f"Nome: {disciplina['nome_disciplina']} - "
                      f"Carga Horária: {disciplina['carga_horaria']}h - "
                      f"Alunos Matriculados: {disciplina['num_alunos_matriculados']}")

    finally:
        conexao.close()

# Executa a função
listar_disciplinas()
