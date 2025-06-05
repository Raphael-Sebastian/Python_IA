with open("arquivos/pessoas.csv") as novo_arquivo:
    for linha in novo_arquivo:
        linha = linha.replace("\n","") #replace para substituir
        partes = linha.split(";") #split para identificar pontos e virgulas e vai tranformar numa lista
        nome = partes[0]
        notas = partes[1:]
        print("Nome: ", nome)
        print("Nota: ", notas)