#escreva uma função chamada lista_estrelas, que recebe uma lista de inteiros como argumento. a função deve imprimir linhas de caraccteres de asterisco. Os números na lista especificam quantos asteriscos cada linha deve conter. por exemplo, com a chamada de função, lista_estrelas([3,7,1,1,2])o seguinte deve ser impresso:

# def lista_estrelas(lista):
#     for numero in lista:
#         print("*" * numero)
# lista_estrelas([3, 7, 1, 1, 2])


lista_estrela = [3,7,11,2]

def estrelasCaracter (lista: list):
    for i in lista:
        estrelas = "*" * i
        print(estrelas)
        
estrelasCaracter(lista_estrela)