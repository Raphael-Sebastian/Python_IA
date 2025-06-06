#crie os seguintes arrays:um array 1d com 5 números inteiros, um array 2d com 2 linhas e 3 colunas de numeros float. Para cada array, imprima: o numero de dimensoes(ndim), a forma (shape), o numero total de elementos (size), o tipo de dados (dtype), o tamanho de cada elemento em byteos (itemsize)


import numpy as np

arr1d = np.array([10,20,30,40,50])

print("Array 1D:")
print(arr1d)
print("Número de dimensão (ndim):", arr1d.ndim)
print("Forma (shape):", arr1d.shape)
print("Número total de elementos (size):", arr1d.size)
print("Tipo de dados (dtype):", arr1d.dtype)
print("Tamanho de cada elemento em bytes (itemsize):", arr1d.itemsize)

arr2d = np.array([[1.1, 2.2, 3.3],[4.4, 5.5, 6.6]])

print("Array 2D:")
print(arr2d)
print("Número de dimensão (ndim):", arr2d.ndim)
print("Forma (shape):", arr2d.shape)
print("Número total de elementos (size):", arr2d.size)
print("Tipo de dados (dtype):", arr2d.dtype)
print("Tamanho de cada elemento em bytes (itemsize):", arr2d.itemsize)