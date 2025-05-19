# numero = int(input("Digite qual tamanho da largura: "))

# def mesaXadrez(tamanho):
#     linha = 0
#     while linha < tamanho:
#         print("01" * tamanho)
#         linha += 1
#     while linha / tamanho:
#         print("01" * tamanho )
#         linha -=1
        
# mesaXadrez(numero)

#meu codigo
numero = int(input("Digite o tamanho do lado do tabuleiro: "))

def mesaXadrez(tamanho):
    linha = 0
    while linha < tamanho:
        if linha % 2 == 0:
            print(("01" * tamanho)[:tamanho])
        else:
            print(("10" * tamanho)[:tamanho])
        linha += 1

mesaXadrez(numero)

#professor

# def Xadrez(tamanho):
#     linha = 0
#     while linha < tamanho:
#         coluna = 0
#         linha_texto = ""
#         while coluna < tamanho:
#             if (linha + coluna) % 2 == 0:
#                 linha_texto += "x"
#             else:
#                 linha_texto += "0"
#                 coluna += 1
#                 print(linha_texto)
#                 linha += 1
                
# Xadrez(15)