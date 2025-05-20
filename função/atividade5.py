# def quadradoString(string1, string2, tamanho):
#     linha = 0
#     while linha < tamanho:
#         elemento = ""
#         coluna = 0
#         while coluna < tamanho:
#             if (linha + coluna) % 2 == 0:
#                 elemento += string1
#             else:
#                 elemento += string2
#             coluna += 1
#         print(elemento)
#         linha += 1
        
# quadradoString("A", "B", 2)



# def quadradoString(nome, tamanho):
#     linha = 0
#     while linha < tamanho:
#         elemento = ""
#         coluna = 0
#         while coluna < tamanho:
#             pos = (linha + coluna) % len(nome)
#             elemento += nome[pos]
#             coluna += 1
#         print(elemento)
#         linha += 1

# nome = input("Digite um nome: ")
# tamanho = int(input("Digite o tamanho do quadrado: "))

# quadradoString(nome, tamanho)

#Professor

def Repetir(palavra, numero): #definir variavel função que multiplica a string pelo numero passado como parametro
    stringTotal = (palavra * numero) #definir variavel stringTotal que inicia em zero e depois ser usado como controle
    linha = 0
    while linha < numero:
        coluna = 0
        letras = " "
        while coluna < numero:
            posicao = linha * numero + coluna
            letras += stringTotal[posicao]
            coluna +=1
        print(letras)
        linha +=1
            
Repetir("Jumanji",3)