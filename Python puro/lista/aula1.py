#Criar uma lista
minha_lista = [10,30,15]

#Acessando elementos por índice
print(minha_lista(0))
print(minha_lista(1))
print(minha_lista(2))

#Trabalhando com elementos da lista
resultado = minha_lista[0] + minha_lista[2]
print(resultado)

#Tamanho da lista
tamanho_lista = len(minha_lista)
print(f"Minha lista tem {tamanho_lista} de tamanho")

#Fatia listas
letras = ["a","b","c","d","e","f"]
print(letras[1:4]) # ele corta de 1 ao elemento de indice 4
print(letras[:3]) #corta do início até o 3-1
print(letras[3:]) #do índice 3 até o final
print(letras[::2]) #todos, com passo 2 (pula de 2 em 2 nesse caso por ser o número 2)
print(letras[::-1]) #lista invertida

#adicionar itens a lista
numeros =  []
numeros.append(5) 
numeros.append(3) 
numeros.append(10)

# print(numeros) 

#adicionar itens em lugar específico
numeros.insert(10,50)
numeros.insert(0,20)
numeros.insert(3,200)
print(numeros)

#Remover ites
numeros.pop(2) #remove pelo indice 
numero_deletado = numeros.pop(0)
print(numeros)

#Remover o valor de um elemento de uma lista
numeros.remove(50) #remove pelo que tem dentro dela
numeros.insert(10,"Rafa")
print(numeros)
numeros.remove("Rafa")
print(numeros)

#Sort - Classificação
lista = [0,45,68,98,78,65,23,35,54,47,89]
lista.sort()
#Sorted cria uma cópia da lista original em outra variavel
lista_v2 = sorted(lista)

print(lista_v2)

#Máximo, mínimo e a soma
lista_numeros = [0,45,78,6,32,15]
print(max(lista_numeros))#Máximo
print(min(lista_numeros))#mínimo
print(sum(lista_numeros))#soma

#mediana == pegar o numero do meio

lista_mediana = [15,48,79,36,56,89,74,15,32]

def mediana(minha_lista: list): #list obriga que seja uma lista, caso o contrario não funciona
    ordenada = sorted(minha_lista)
    centro_lista = len(ordenada) // 2
    return ordenada[centro_lista]

print(f"A mediana é {mediana(lista_mediana)}")