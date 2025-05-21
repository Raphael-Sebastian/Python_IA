lista = [1, 2, 3, 4, 5]

while True:
    indice = int(input("Digite o índice que deseja alterar (ou -1 para sair): "))
    
    if indice == -1:
        print("Programa encerrado")
        break
    
    if 0 <= indice < len(lista):
        novo_valor = int(input("Digite o novo valor: "))
        lista[indice] = novo_valor
        print("Lista atualizada:", lista)
    else:
        print("Índice inválido. Tente novamente.")

    
#escreva um programa que inicialize uma lista com os valores [1,2,3,4,5]. então o programa deve pedir ao usuário um indice e um novo valor,substituir o valor no índice fornecido e imprimir a lista novamente. isso deve ser repetido até que o usuário forneça -1 para o índice.




    
    