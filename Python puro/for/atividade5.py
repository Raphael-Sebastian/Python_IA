#escreva uma função chamada lista_soma que recebe duas listas de inteiros como argumentos. a função retorna uma nova lista que contém as somas dos itens em cada índice nas duas listas originais. Você pode assumir que ambas as listas têm o mesmo número de itens.


lista1 = [10, 20, 30]
lista2 = [1, 2, 3]
def lista_soma(lista1,lista2):
    resultado = []
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        resultado.append(soma)
    return resultado

print(lista_soma(lista1, lista2))