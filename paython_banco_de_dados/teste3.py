import pymysql

def buscar_alunos(nome=None, email=None, status=None, curso=None):
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="sistema_escolar",
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conexao.cursor() as cursor:
            # Monta a query base
            query = """
                SELECT 
                    a.aluno_id,
                    a.nome,
                    a.email,
                    a.status_aluno,
                    c.nome_curso
                FROM alunos a
                LEFT JOIN cursos c ON a.curso_id = c.curso_id
                WHERE 1 = 1
            """

            params = []

            # Filtros opcionais
            if nome:
                query += " AND a.nome LIKE %s"
                params.append(f"%{nome}%")

            if email:
                query += " AND a.email = %s"
                params.append(email)

            if status:
                query += " AND a.status_aluno = %s"
                params.append(status)

            if curso:
                query += " AND c.nome_curso LIKE %s"
                params.append(f"%{curso}%")

            cursor.execute(query, params)
            resultados = cursor.fetchall()

            if resultados:
                for aluno in resultados:
                    print(f"ID: {aluno['aluno_id']} | Nome: {aluno['nome']} | Email: {aluno['email']} | "
                          f"Status: {aluno['status_aluno']} | Curso: {aluno['nome_curso']}")
            else:
                print("Nenhum aluno encontrado com os critérios fornecidos.")

    finally:
        conexao.close()

# Exemplos de uso:
buscar_alunos(nome="joão")               # Busca por nome parcial
# buscar_alunos(email="joao@email.com")  # Busca por e-mail exato
# buscar_alunos(status="Ativo")          # Busca por status
# buscar_alunos(curso="Engenharia")     # Busca por curso (parcial)
