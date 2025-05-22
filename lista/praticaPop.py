lista = []

while True: 
    print("\nMenu:") 
    print("1. Adicionar")
    print("2. Remover por posição")
    print("0. Sair")

    op = input("Opção: ")

    if op == "0":
        break 

    if op == "1":
        lista.append(input("Item: ")) 
    elif op == "2":
        i = int(input("Índice: "))
        if 0 <= i < len(lista): 
            lista.pop(i)
  

    print("Lista:", lista)


#professor

# lista = []
# while True:
#     opcao = input("O que você quer fazer? + ou -: ")
#     if opcao == "+":
#         if len(lista) == 0:
#             lista.append(1)
#         else:
#             lista.append(lista[-1] + 1)
#     else:
#         if len(lista) == 0:
#             print("A lista está vazia")
#         else:
#             lista.pop(len(lista)-1)
#     print(lista)