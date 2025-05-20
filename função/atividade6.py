# def linha(comprimento, caractere):
#     if caractere == "":
#         caractere = "*"
#     else:
#         caractere = caractere[0]

#     contador = 0
#     while contador < comprimento:
#         print(caractere, acaba="")
#         contador += 1
#         print("a", 5)


# def linha():
#     comprimento = int(input("Digite o comprimento da linha (número inteiro): "))
#     caractere = input("Digite a string (será usado o primeiro caractere): ")
    
#     if len(caractere) > 0:
#         caractere = caractere[0]
#     else:
#         caractere = '*'
    
#     print(caractere * comprimento)

# linha()

#professor

def imprimir (n,texto):
    if texto[0] == "":
        print("*" * n)
    else:
        print(texto[0]*n)
        
imprimir(5,"")