import pymysql 

# conexao = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="123456",
#     database="sistema_escolar",
#     cursorclass=pymysql.cursors.DictCursor
# )

conexao = pymysql.connect(
    host="localhost", #endereço do banco
    user="root", #usuário
    password="123456", # senhado seu MySQL
    database="sistema_escolar", #nome do banco
    cursorclass=pymysql.cursors.DictCursor #retornar linhas como dicionário (chave:coluna)
)

# print("Conectando com sucesso!")
# conexao.close()

#codigo para consulta e puxar os dados dos alunos

#enviando um select para o banco de dados
# with conexao.cursor() as cursor:
#     cursor.execute("SELECT * FROM alunos")
#     alunos = cursor.fetchall() #retorna todos os alunos
    
#     #Mostra os dados
#     for aluno in alunos:
#         print(f"Aluno: {aluno["nome"]} - Email{aluno["email"]} - Semestre: {aluno["semestre_atual"]}")

#esse codigo é para inserir um novo usuário

# with conexao.cursor() as cursor:
#     sql = "INSERT INTO alunos (nome, email, telefone, data_nascimento, curso_id, semestre_atual, status_aluno, data_matricula) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
#     #se usar o %s no values a gente previne o inject
    
#     valores = ("Luciana Souza","Luciana@melo.com","499999999","2001-03-12",1,2,"Ativo","2024-08-01")
#     cursor.execute(sql,valores)
#     conexao.commit() #salvando no banco de dados

#atualizar um usuario
# with conexao.cursor() as cursor:
#     sql = "UPDATE alunos SET telefone = %s WHERE aluno_id = %s"
#     valores = ("(49) 9999-4587",601)
#     cursor.execute(sql,valores)
#     conexao.commit()

#Deletar dados do banco de dados
try:
    #cursor serve para a gente consegui utilizar o MySQL
    with conexao.cursor() as cursor:
        sql = "DELETE FROM alunos WHERE aluno_id = %s"
        valores = (601)
        cursor.execute(sql,(601))
        conexao.commit()
except Exception as erro:
    print("Deu um erro no banco:", erro)
finally:
    conexao.close()