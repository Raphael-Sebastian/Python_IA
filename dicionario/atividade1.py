#escreva um aplicativo de lista telefônica. Ele deve funcionar da seguinte forma: comando (1 buscar, 2 adiciona, 3 sai): 2 nome:peter número:040-5466745

# lista = {} 

# while True:
#     print("\nMenu :")
#     print("1. Busca")
#     print("2. Adicionar")
#     print("3. Sair")
    
#     op = input("Opção: ")
    
#     if op == "3":
#         print("Saindo")
#         break
    
#     elif op == "1":
#         nome_busca = input("Digite o nome para buscar: ")
    
lista = {}

while True:
    print("1 buscar, 2 adiciona, 3 sai")
    op = input("comando: ")
    
    if op == "3":
        break
    
    elif op == "1":
        nome = input("nome: ")
        if nome in lista:
            print(lista[nome])
        else:
            print("não encontrado")
    
    elif op == "2":
        entrada = input("Digite um nome:  ")
        numero = int(input("Digite número: "))
        lista[entrada] = numero
        print("")
        
    else:
        print("comando inválido")
