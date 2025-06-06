#criar matriz identidade: Escreva uma função chamada matriz_identidade que recebe um número n e retorne uma matriz identidade n x n com numpy

import numpy as np

def matriz_identidade(n):
    return np.identity(n)
print(matriz_identidade(3))