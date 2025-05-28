#escreva uma função chamada conta_elementos_match(minha_matriz: list, elemento: int), que recebe um array bidimensional de inteiros e um único valor inteiro como seus argumentos. A função então conta quantos elementos dentro da matriz correspondem ao valor do argumento




def conta_elementos_match(minha_matriz: list, elemento: int):
    contador = 0
    for linha in minha_matriz:
        for valor in linha:
            if valor == elemento:
               contador += 1
    return contador

lista_bidimensional = [

    [1,2,3],
    [4,2,2],
    [7,8,2],
    ]


resultado = conta_elementos_match(lista_bidimensional, 8)
print("Elemento:", resultado)