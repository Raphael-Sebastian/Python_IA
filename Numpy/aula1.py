import numpy as np #sempre colocar np para apreviar o numpy 

#Saída o array as dimensões pelo método (ndim)
arr1d = np.array([1,2,3])
print(f"Array 1D: {arr1d}, Dimensões: {arr1d.ndim}") #ndim e uma função para exibir quantas dimensões tem no arranjo(array)

arr2d = np.array([[1,2,3,4,5],[5,6,8,9,6]]) #duas dimensões
print(f"Array 2d: {arr2d}, Dimensões: {arr2d.ndim}")

arr3d = np.array([[[0,5,6],[5,8,9]],[[4,5,6],[5,9,8]]]) #tres dimensões
print(f"Array 3d: {arr3d}, Dimensões: {arr3d.ndim}")

#shape
#indica o tamanho do array
print(f"Shape do arr1d {arr1d.shape}")
print(f"Shape do arr1d {arr2d.shape}")
print(f"Shape do arr1d {arr3d.shape}")


#Dtype
#ele pega os tipos de dados dos arranjos/array
array_float = np.array([1.5,1.8,9.5])
print(f"O dtype dessa array é: {array_float.dtype}") 
print(f"O dtype da arr1d é: {arr1d.dtype}")

#Itemsize
#retorna o comprimento de cada elemento da matriz em bytes
print(f"O temsize do arr1d é: {arr1d.itemsize}")
print(f"O temsize do arr3d é: {arr3d.itemsize}")
print(f"O temsize do array_float é: {array_float.itemsize}")