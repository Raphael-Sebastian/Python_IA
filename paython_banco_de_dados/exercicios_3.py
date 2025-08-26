import pymysql

def buscar_alunos(nome, email, status, curso):
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
                    a.aluno_id,
                    a.nome,
                    a.email,
                    a.status_aluno,
                    c.nome_curso
                FROM alunos a
                JOIN cursos c ON a.curso_id = c.curso_id
                WHERE 1 = 1"""
                
            parametro= []
            
            if nome:
                sql += "AND a.nome LIKE %s"
                parametro.append(f"%{nome}%")
                
            if email:
                sql += "AND a.email = %s"
                parametro.append(email)
                
            if status:
                sql += "AND a.status_aluno = %s"
                parametro.append(status)
                
                
            if curso:
                sql += "AND c.nome_curso LIKE %s"
                parametro.append(f"%{curso}%")
                
            cursor.execute(sql, parametro)
            resultados = cursor.fetchall()
            
            if resultados:
                for aluno in resultados:
                    print(f"ID: {aluno['aluno_id']} - Nome: {aluno['nome']} - Email: {aluno['email']} -" f"Status: {aluno["status_aluno"]} - Curso: {aluno['nome_curso']}")
                else:
                    print("Nenhum aluno encontrado com os critérios fornecidos. ")
                    
    finally:
        conexao.close()
        
        buscar_alunos(nome="joão")