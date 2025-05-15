lista = []

while True: # inicia um laço infinito para manter o programa a correr até o utilizador escolher sair;
    print("\nMenu :") # Inicia um laço infinito para manter o programa a correr até o utilizador escolher sair;
    print("1. Adicionar")
    print("2. Inserir em posição")
    print("3. Adicionar vários")
    print("4. Remover")
    print("5. Remover por posição")
    print("6. Limpar lista")
    print("7. Ver posição de item")
    print("8. Contar item")
    print("9. Ordenar")
    print("10. Inverter")
    print("0. Sair")

    op = input("Opção: ") #lê a opção escolhida pelo utilizador;

    if op == "0": #caso de problema la em baixo por causa dos if pode ser aqui! 00:10;
        break #Encerra o programa com break;

    if op == "1":
        lista.append(input("Item: ")) #Usa append() para adicionar o item ao final da lista;
    elif op == "2":
        lista.insert(int(input("Posição: ")), input("Item: ")) #Usa insert(pos, item):Primeiro lê a posição como int, depois o conteúdo do item, insere na posição indicada;
    elif op == "3":
        lista.extend(input("Itens separados por vírgula: ").split(",")) # Usa split(",") para separar os itens inseridos com vírgulas, e depois extend() para adicionar todos à lista;
        #split bonus: O método split() em Python divide uma string em uma lista de substrings, usando um delimitador (ou separador) como parâmetro. Se o delimitador não for especificado, a string é dividida nos espaços em branco. O método split() retorna a lista de substrings;
    elif op == "4":
        item = input("Item a remover: ")
        if item in lista:
            lista.remove(item)  #Se o item existir na lista, é removido com remove() ; 
    elif op == "5":
        i = int(input("Índice: "))
        if 0 <= i < len(lista): #A função len() em Python é usada para retornar o número de itens de um objeto iterável, como strings, listas, tuplas, dicionários, etc. Ela é uma função interna que facilita a contagem de elementos em diversas estruturas de dados;
            lista.pop(i)
    elif op == "6":
        lista.clear() #Usa clear() para esvaziar a lista completamente;
    elif op == "7":
        item = input("Item: ")
        if item in lista:
            print("Posição:", lista.index(item)) #Procura o índice do item com index(), se ele existir;
    elif op == "8":
        print("Quantidade:", lista.count(input("Item: "))) #Usa count() para contar quantas vezes o item aparece na lista;
    elif op == "9":
        lista.sort() #Ordena os itens por ordem alfabética (ou numérica);
    elif op == "10":
        lista.reverse() #Inverte a ordem atual dos itens da lista

    print("Lista:", lista)

#fim de trabalho 04:23

#exemplo de len


# # Strings
# texto = "Olá, mundo!"
# print(len(texto))  # Saída: 11

# # Listas
# numeros = [1, 2, 3, 4, 5]
# print(len(numeros))  # Saída: 5

# # Tuplas = estrutura de dados que armazena uma sequência ordenada de elementos imutáveis;
# coordenadas = (10, 20, 30)
# print(len(coordenadas))  # Saída: 3

# # Dicionários
# pessoa = {"nome": "João", "idade": 30}
# print(len(pessoa))  # Saída: 2