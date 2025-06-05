#Crie um programa que leia um arquivo CSV chamado "dados.csv" que contenha nomes e idades em cada linha (separados por vírgula). O programa deve criar um novo arquivo chamado "dados_maiores.csv" apenas com as linhas em que a idade seja maior ou igual a 18.


# with open("arquivos/dados.csv", "r") as entrada, open("arquivos/dados_maiores.csv","w") as saida:
#     for linha in entrada:
#         nome, idade = linha.strip().split(",")
#         if int(idade) >= 18:
#             saida.write(f"{nome},{idade}\n")
#             print(f"{nome},{idade}")

#professor

try:
    with open("arquivos/dados.csv", "r") as arquivo_entrada:
        with open("arquivos/dados_maiores.csv", "w") as arquivo_saida:
            for linha in arquivo_entrada:
                linha = linha.replace("\n","")
                if linha:
                    partes = linha.split(",")
                    nome = partes[0]
                    idade = partes[1]
                    if len(idade) <= 3:
                        if int(idade) >= 18:
                            arquivo_saida.write(linha + "\n")
    print("Arquivo 'dados_maiores.csv' criado com sucesso.")
    
except FileNotFoundError:
    print("Arquivo 'dados.csv' não encontrado.")
    
except ValueError:
    print("Erro: Verifique se o arquivo está no formato 'nome,idade'.")
