# lista = []

# while True:
#     print("\nMenu :") 
#     print("1. Adicionar")
#     print("2. Remover")
#     print("0. Sair")

#     op = input("Opção: ") 

#     if op == "0": 
#         break 

#     if op == "1":
#         lista.append(input("Item: ")) 
#     elif op == "2":
#         item = input("Item a remover: ")
#         if item in lista:
#             lista.remove(item)

def lista_compras():
    lista = []

    while True:
        print("\nMenu:")
        print("1. Adicionar")
        print("2. Remover")
        print("0. Sair")

        op = input("Opção: ")

        if op == "0":
            break
        
        elif op == "1":  
            item = input("Item: ")
            lista.append(item)
            
        elif op == "2":
            
            item = input("Item a remover: ")
            if item in lista:
                lista.remove(item)
                
            else:
                print("Item não está na lista.")
        else:
            print("Opção inválida.")

    print("\nLista final de compras (ordenada):")
    for item in sorted(lista):
        print(f"- {item}")

lista_compras()



#implemente uma função chamada lista_compras() que: use while para permitir ao usuário adicionar itens a lista, remova itens se o usuário digitar remover:<item>, termine quando o usuário digitar sair e mostre a lista final organizada em ordem alfabética