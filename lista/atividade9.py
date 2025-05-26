# valores = []
# while True:
#     numero = int(input("Digite um número (0 para sair): "))
#     if numero == 0:
#         print("Programa ecerrado.")
#         break
#     valores.append(numero)
#     print("Lista (ordem de inserção):", valores)
#     print("Lista (ordenada):", sorted(valores))

def lista_crescente():
    valores = []

    while True:
        numero = int(input("Digite um número: "))
        valores.append(numero)

        if len(valores) > 1 and valores[-1] < valores[-2]:
            print("Número menor que o anterior detectado. Encerrando.")
            break

    print("\nNúmeros digitados em ordem crescente:")
    print(sorted(valores))

lista_crescente()

#peça ao usuário para digitar números até que a lista esteja em ordem decrescente (isto é, o ultimo número for menor que o anteriror). ao final, imprima todos os números digitados em ordem crescente