#escreva uma função chamda histogram, que recebe uma string como argumento. a função deve imprimir um histograma representando o número de vezes que cada letra ocorre na string. Cada ocorrência de uma letra deve ser representada por um asterico na linha específica para aquela letra. Por exemplo, a chamada de função histogram("abba") deve imprimir.

# def histogram(lista):
#     letra = {}
#     for letra in lista:
#         lista[letra] +=1
#     else:
#         lista[letra] = 1
        
#     ja_impresso = []
#     for letra in lista:
#         if letra not in ja_impresso:
#             print(letra + ": " + "*"[letra])
#             ja_impresso.append(letra)
            
# print(histogram("banana"))


def histogram(texto):
    frequencia = {}

    
    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

    
    for letra in frequencia:
        print(letra + ": " + "*" * frequencia[letra])


histogram("abba")
