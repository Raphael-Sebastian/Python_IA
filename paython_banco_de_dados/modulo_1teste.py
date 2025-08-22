import pymysql 
try:
    conexao = pymysql.connect(
    host="localhost", #endereço do banco
    user="root", #usuário
    password="123456", # senhado seu MySQL
    database="sistema_escolar", #nome do banco
    cursorclass=pymysql.cursors.DictCursor #retornar linhas como dicionário (chave:coluna)
)
    
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM alunos")
        print(cursor.fetchall())
except Exception as erro:
    print("Erro ao acessar o banco de dados:",erro)
finally:
    conexao.close()