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
                    t.turma_id, 
                    d.nome_disciplina, 
                    p.nome AS nome_professor, 
                    t.semestre, 
                    t.ano, 
                    COUNT(m.matricula_id) AS alunos_matriculados, 
                    AVG(n.nota) AS media_geral 
                FROM turmas t
                JOIN disciplinas d ON t.disciplina_id = d.disciplina_id
                JOIN professores p ON t.professor_id = p.professor_id
                JOIN matriculas m ON t.turma_id = m.turma_id AND m.status_matricula = 'Matriculado'
                JOIN notas n ON m.matricula_id = n.matricula_id
                GROUP BY 
                    t.turma_id, d.nome_disciplina, p.nome, t.semestre, t.ano
                ORDER BY 
                    t.ano DESC, t.semestre;
            """)
            disciplinas = cursor.fetchall()

        # Mostra os dados
        for disciplina in disciplinas:
            print(f"Turma ID: {disciplina['turma_id']} - Disciplina: {disciplina['nome_disciplina']} - "
                  f"Professor: {disciplina['nome_professor']} - Semestre: {disciplina['semestre']} - Ano: {disciplina['ano']} - "
                  f"Alunos matriculados: {disciplina['alunos_matriculados']} - Média geral: {disciplina['media_geral']:.2f}")

    finally:
        conexao.close()

listar_disciplinas()
