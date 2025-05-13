idade = int(input("Digite sua idade: "))

if idade >12:
    print(f"Ok, você tem {idade} ")
elif idade < 6:
    print(f"Suspeito você com {idade} anos não sabe escrever ")
elif idade < 0:
    print (f"Impossivel deve ser um erro ")