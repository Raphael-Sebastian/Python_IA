from math import sqrt

while True:
    
    numero = int(input("Digite um número inteiro (0 para sair) "))
    
    if numero < 0:
        print("Número inválido ")
        break
    elif numero > 0:
        print(sqrt(numero))
    else:
        print("Fim!!!")
        break
        