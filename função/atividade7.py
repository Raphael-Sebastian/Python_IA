# largura = int(input("Digite quantos hashtags você quer: "))

# def quadrado_hashtag(tamanho):
#     linha = 0
#     while linha < tamanho:
#         print("#" * tamanho)
#         linha += 1

# def linha():
#     comprimento = int(input("Digite o comprimento da linha (número inteiro): "))
#     caractere = input("Digite a string (será usado o primeiro caractere): ")
    
#     if len(caractere) > 0:
#         caractere = caractere[0]
#     else:
#         caractere = "#" * 20
    
#     print(caractere * comprimento)

# linha()

#resultado final

def linha (n,texto):
    if texto[0] == "":
        caractere = "*"
    else:
        caractere = texto[0]
        
    print(caractere * n)

def caixa_de_hashtag(altura):
    contador = 0
    while contador < altura:
        linha(10, "#")
        contador += 1
        
caixa_de_hashtag(7)