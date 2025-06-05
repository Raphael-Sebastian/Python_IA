nome1 = input("Digite o primeiro nome: ")
idade1 = int(input("Digite a primeira idade: "))
nome2 = input("Digite o segundo nome: ")
idade2 = int(input("Digite a segunda idade: "))

if idade1 > idade2:
    print(f"Esse é o idoso: {nome1}")
elif idade1 < idade2:
    print(f"Esse é o idoso: {nome2}")
else:
    print("Digite novamente!!!")