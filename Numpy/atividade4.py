#gerar array de valores entr dois números, escreva uma função chamada gerar_array_intervalo que receba dois inteiros e retorne um array contendo todos os inteiros entre eles.

# def gerar_array_intervalo(inicio, fim):
#     if inicio < fim:
#         return list(range(inicio + 1, fim))
#     elif inicio > fim:
#         return list(range(fim - 1, inicio, -1))
#     else:
#         return []
    
# print(gerar_array_intervalo(3,7))

#professor

import numpy as np

def gerar_array_intervalo(inicio, fim):
    if inicio <= fim:
        return np.arange(inicio, fim + 1)
    
print(gerar_array_intervalo(3,7))