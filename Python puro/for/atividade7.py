#o jogo da velha é jogado em uma grade 3 por 3, por dois jogadores que se revezam inserindo cruzes e círculos. Se qualquer jogador conseguir colocar três de seus próprios símbolos em qualquer linha, coluna ou diagonal, ele ganha.Se nenhum jogador conseguir isso, é um empate.Escreva uma função chamada jogue_o_jogo(mesa: list, x: int, y: int, caracter: str), que coloca o símbolo dado nas coordenadas dadas no tabuleir. Os valores das coordenadas no tabuleiro estão entre 0 e 2.


# def jogue_o_jogo(mesa: list, x: int, y: int, caracter: str):
#     if 0 <= 2 and 0 <= y <= 2:
#         if mesa[x][y] == "":
#             mesa[x][y] = caracter
#             return True
#         else:
#             return False
#     else:
#         return False

# lista_bidimensional = [
#     ["","x",""],
#     ["","",""],
#     ["","",""],
# ]

# resultado = jogue_o_jogo(lista_bidimensional,0,1,"X")
# print("Jogada válida", resultado)
# for linha in lista_bidimensional:
#     print(linha)

# def jogue_o_jogo(mesa: list, x: int, y: int, caracter: str):
#     if 0 <= 2 and 0 <= y <= 2:
#         if mesa[x][y] == "":
#             mesa[x][y] = caracter
#             return True
#         else:
#             return False
#     else:
#         return False

# lista_bidimensional = [
#     ["","x",""],
#     ["","",""],
#     ["","",""],
# ]

# while True:
#     x = int(input("Digite a linha (0,1 ou 2): "))
#     y = int(input("Digite a coluna (0,1 ou 2): "))
#     if 0 <= x <= 2 and 0 <= y <= 2:
#         break
#     else:
#         print("Por favor, digite um número entre 0 e 2.")
        
# resultado = jogue_o_jogo(lista_bidimensional, x, y, "X")

# if resultado:
#     print("Jogada válida!")
# else:
#     print("Jogada inválida!")
    
# for linha in lista_bidimensional:
#     print(linha)

#professor

mesa = [
    ["","",""],
    ["","",""],
    ["","",""]
    ]
contador = 0
print(F"Tempo: {contador} - Olá jogador 1, comece o jogo com X. BOA SORTE!")
 
def jogue_o_jogo(mesa,linha,coluna,caracter):
    mesa[linha][coluna] = caracter
    exibe_resultado()
    if contador % 2 != 0:
        jogador = "1 (x)"
    else:
        jogador = "2 (O)"
       
    print(f"Tempo {contador} - Ótimo jogada, agora é a vez do jogador {jogador}")
    print("")
 
def exibe_resultado():
    for linhas in mesa:
        for items in linhas:
            if items == "":
                print("_ ",end="")
            print(items,end=" ")
 
        print(" ")
   
while True:
    linha = int(input("Qual a linha: "))
    coluna = int(input("Qual a coluna: "))
    caracter = input("Qual o caracter: ")
    jogue_o_jogo(mesa,linha, coluna, caracter)
    contador += 1
    if contador == 9:
        exibe_resultado()
        break