import pymysql 
conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="sistema_escolar",
    cursorclass=pymysql.cursors.DictCursor
)
try:
    with conexao.cursor() as cursor:
        nome = input("Digite o nome do aluno: ")
        email = input("Digite o email do aluno: ")
        semestre_atual = input("Digite o semestre atual do aluno: ")
        
        sql = "INSERT INTO alunos (nome,email, semestre_atual) VALUES (%s,%s,%s)"
        cursor.execute(sql, (nome, email, semestre_atual))
        conexao.commit()
        print("Aluno cadastrado com sucesso!\n")

    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        
        for aluno in alunos:
            print(f"Aluno: {aluno["nome"]} - Email{aluno["email"]} - Semestre: {aluno["semestre_atual"]}")
finally:
    conexao.close()