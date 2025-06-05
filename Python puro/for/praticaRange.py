#escreva um programa que peça ao usúario um inteiro positivo N. O programa então imprime todos os números entre -N e N inclusive, mas deixa de fora o número 0. Cada número deve ser impresso em uma linha separada.

numero = int(input("Digite um número inteiro: "))
# if numero > 0:
for i in range(-numero, numero + 1):
        if i !=0:
            print(i,end=" ")
else:
    print("Por favor, Digite um número inteiro.")
