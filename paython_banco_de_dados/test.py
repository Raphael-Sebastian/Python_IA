import pymysql

def relatorio_turmas():
    try:
        conexao = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="sistema_escolar",
            cursorclass=pymysql.cursors.DictCursor
        )

        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM turmas")
            turmas = cursor.fetchall()

            for turma in turmas:
                turma_id = turma['turma_id']
                semestre = turma['semestre']

                cursor.execute("SELECT nome_disciplina FROM disciplinas WHERE disciplina_id = %s", (turma['disciplina_id'],))
                nome_disciplina = cursor.fetchone()['nome_disciplina']

                cursor.execute("SELECT nome_professor FROM professores WHERE professor_id = %s", (turma['professor_id'],))
                nome_professor = cursor.fetchone()['nome_professor']

                cursor.execute("SELECT COUNT(*) AS total FROM matriculas WHERE turma_id = %s", (turma_id,))
                num_alunos = cursor.fetchone()['total']

                cursor.execute("SELECT ROUND(AVG(nota_final), 2) AS media FROM matriculas WHERE turma_id = %s", (turma_id,))
                media = cursor.fetchone()['media']
                if media is None:
                    media = 0.0

                print(f"Turma: {turma_id} | Disciplina: {nome_disciplina} | Professor: {nome_professor} | Semestre: {semestre} | Alunos: {num_alunos} | Média: {media}")

    except Exception as e:
        print("Erro:", e)

    finally:
        conexao.close()
