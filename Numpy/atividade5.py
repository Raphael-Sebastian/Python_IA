#calcular média, soma escreva uma função chamada estatisticas_array que receba um array e retorne a soma, a média dos seus elementos

import numpy as np

# def estatisticas_array(array):
#     array = np.array(array)
#     soma = 0
#     for elemento in array:
#         soma += elemento
#     media = soma / len(array)
#     return soma, media

# numeros = [10,20,30,40]
# soma, media = estatisticas_array(numeros)
# print(f"Soma: {soma}, Média: {media}")


def estatisticas_array(array):
    soma = np.sum(array)
    media = np.mean(array)
    return soma, media

meu_array = np.array([10,20,30,40,50])
print(estatisticas_array(meu_array))