#lista usando append()
#Adiciona um item ao final da lista.

# frutas = ["maça", "banana","tomate", 25, True]
# #Metodos de lista para adicionar um item ao final da lista
# frutas.append(Morango)
# print (frutas)

#Insere um item na posição especificada.
#array.insert(1, 10)

#insert(pos, item)
#Insere um item na posição (índice) desejada.

# numeros = [1, 2, 3]
# numeros.insert(1, 100)
# print(numeros)  # [1, 100, 2, 3]

#extend(iterável)
#Adiciona os itens de outro iterável (como lista, tupla, etc.) ao final da lista original.

# lista1 = [1, 2]
# lista1.extend([3, 4])
# print(lista1)  # [1, 2, 3, 4]

#remove(valor)
#Remove a primeira ocorrência do valor especificado.

# valores = [10, 20, 30, 20]
# valores.remove(20)
# print(valores)  # [10, 30, 20]

#pop([índice])
#Remove e retorna um item pelo índice. Se não informar, remove o último.

# itens = ['a', 'b', 'c']
# ultimo = itens.pop()
# print(ultimo)  # 'c'
# print(itens)   # ['a', 'b']

#clear()
#Remove todos os itens da lista, deixando-a vazia.

# nomes = ['Ana', 'Bruno', 'Carlos']
# nomes.clear()
# print(nomes)  # []

#index(valor)
#Retorna o índice (posição) da primeira vez que o valor aparece na lista.

# letras = ['x', 'y', 'z']
# print(letras.index('y'))  # 1

#count(valor)
#Conta quantas vezes o valor aparece na lista.

# nums = [1, 2, 2, 3, 2]
# print(nums.count(2))  # 3

#sort()
#Ordena a lista em ordem crescente por padrão. Use reverse=True para ordem decrescente.

# valores = [5, 1, 4]
# valores.sort()
# print(valores)  # [1, 4, 5]
# valores.sort(reverse=True)
# print(valores)  # [5, 4, 1]

#reverse()
#Inverte a ordem dos elementos da lista.

# dados = [1, 2, 3]
# dados.reverse()
# print(dados)  # [3, 2, 1]

#copy
#metodo para copiar

# dados = [1,2,3]
# dados.copy()
# print(dados)