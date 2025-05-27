#escreva uma função chamada numeros_pares, que recebe uma lista de inteiros como argumentos. A função retorna uma nova lista contendo os números pares da lista original.

numero = [2,4,6,8]

def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print(numeros_pares(numero))
