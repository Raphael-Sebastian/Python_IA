#operações entre matrizes, escreva uma função chamada somar_matrizes que recebe duas matrizes do mesmo tamanho e retorne a soma delas. Se não forem do mesmo tamanho, a função deve retornar uma mensagem de erro.

import numpy as np

# def somar_matrizes(matriz1,matriz2):
#     arr1 = np.array(matriz1)
#     arr2 = np.array(matriz2)
    
#     if arr1.shape != arr2.shape:
#         return "Erro: As matrizes devem ter o mesmo tamanho."
    
#     return arr1 + arr2

# matriz_1 = [[1,2,3], [4,5,6]]
# matriz_2 = [[6,5,4], [3,2,1]]

# resultado = somar_matrizes(matriz_1, matriz_2)
# print(resultado)

#professor

def somar_matrizes(matriz1,matriz2):
    if np.shape(matriz1) == np.shape(matriz2):
        return matriz1 + matriz2
    else:
        return "Erro: As matrizes devem ter o mesmo tamanho."
    
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(somar_matrizes(m1,m2))