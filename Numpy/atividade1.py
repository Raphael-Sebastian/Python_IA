#criar array a partir da lista: escreva uma função chamada criar_array que receba uma lista de múmeros inteiros e retorne um array numPy

import numpy as np
#Criar a função que recebe uma lista como parametro
def criar_array(lista):
    #np.array converte a lista em array
    return np.array(lista)
#the list
lista = [1,2,3,4,5]

#printa e invoca a função passando a lista como argumento
print(criar_array(lista))
