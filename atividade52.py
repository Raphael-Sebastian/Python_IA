
# numero = 42
# print("Tente advinhar o número!!!")

# while True:
#     digite = int(input("Digite um número de 0 a 50: "))
    
#     if digite >= 0 and digite <=10:
#         print("Tá longe")
#     elif digite >= 20 and digite <=30:
#         print("Tá meio frio ainda")
#     elif digite >= 30 and digite <=40:
#         print("Tá ficando quente")
#     elif digite >=43 and digite <=50:
#         print("Já passou!!!") 
#     else:
#         print("Acertou!!!")
    
    
import random
print("Tente advinhar o número!!!")
numero_secreto = random.randint(0,100)
numeroDeVezes = 0

while True:
    digite = int(input("Digite um número de 0 a 100: "))
    numeroDeVezes += 1
    
    if numero_secreto < digite:
        print("O número é menor")
    elif numero_secreto > digite:
        print("O número é maior")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {numeroDeVezes} Tentativa(s).")
        break