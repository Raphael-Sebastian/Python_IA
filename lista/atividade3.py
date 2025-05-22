# quantidade = input("Vamos digitar nomes: ")
# lista = []
# contador = 0

# while contador < quantidade:
#     nomes = input(f"Digito {contador + 1}° nome: ")
#     lista.append(nomes)
#     contador +=1
    
#     print("Lista final:", lista)
    
lista_nomes = []

while len(lista_nomes) < 5:
    nome = input("Qual nome: ")
    
    if nome in lista_nomes:
        print("Nome já existe")
        
    else:
        lista_nomes.append(nome)
        
    print(lista_nomes)
    