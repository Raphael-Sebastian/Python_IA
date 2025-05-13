limite = int(input("Digite um número que seja o limite: "))
i = 1
base = int(input("Qual a base: "))
if limite < 2:
    print("Digite outro número")
else:
    
 while i <= limite:
    print(i)
    i *= base
print(f"limite era: {limite}")




