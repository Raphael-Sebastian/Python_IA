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