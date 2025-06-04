#Crie um programa que leia um arquivo CSV chamado "dados.csv" que contenha nomes e idades em cada linha (separados por vírgula). O programa deve criar um novo arquivo chamado "dados_maiores.csv" apenas com as linhas em que a idade seja maior ou igual a 18.


with open("arquivos/dados.csv", "r") as entrada, open("dados_maiores.csv","w") as saida:
    for linha in entrada:
        nome, idade = linha.strip().split(",")
        if int(idade) >= 18:
            saida.write(f"{nome},{idade}\n")