#escreva uma função chamada Soma_Positivos, que recebe uma lista de inteiros como argumento. A função retorna a soma dos valores positivos na lista.
numeros = [-5, 3, 7, -2, 0, 10]


def Soma_Positivos(lista):
    soma = 0
    for numero in lista:
        if numero > 0:
            soma += numero
    return soma

print(Soma_Positivos(numeros))