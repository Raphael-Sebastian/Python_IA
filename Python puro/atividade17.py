nome = input("Digite o sue nome de usuário: ")


if nome != "Jerry":
    porcoes = int(input("Quantas porções vai querer? "))
    total = porcoes * 5.90
    
    print(f"total: {total}")
else:
    print("Você é o Jerry, ta tudo pago") 