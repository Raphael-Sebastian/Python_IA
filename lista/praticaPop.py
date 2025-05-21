lista = []

while True:
    print("1. Adicionar")
    print("2. remoção")
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
    
    
    