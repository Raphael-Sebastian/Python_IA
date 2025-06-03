#o arquivo numeros.txt contém números inteiros, um número por linha. O conteúdo pode ser parecido com este: escreva uma função chamada Maior, que leia o arquivo e retorne o maior número do arquivo. observe que a função não recebe argumentos. o arquivo com o qual você está trabalhando é sempre nomeado numeros.txt

# def maior():
#     with open("arquivos/numeros.txt") as arquivo:
#         numeros = [int(linha) for linha in arquivo]
#     return max(numeros)

# print(maior())


try:
    with open("arquivos/numeros.txt") as arquivos:
        maior = 0
        for linha in arquivos:
            numero = int(linha)
            if numero > maior:
                maior = numero
        print("Maior número:", maior)
except FileNotFoundError:
    print("Arquivo 'numeros.txt' não encontrado")
except ValueError:
    print("Erro: o arquivo contém dados que não são números inteiros. ")