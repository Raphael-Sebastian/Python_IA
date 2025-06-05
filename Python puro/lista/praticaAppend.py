quantidade = int(input("Quantos números deseja adicionar? "))
lista_numeros = []
contador = 0

while contador < quantidade:
    numero = int(input(f"Digite o {contador + 1}° número: "))
    lista_numeros.append(numero)
    contador +=1
    
    print("lista final:", lista_numeros)