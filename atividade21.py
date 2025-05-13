graus = int(input("Digite ps graus F: "))

celsius = (graus -32) * 5/9

if celsius < 0:
    print(f"{celsius} - Brrrrrr!!!")
else:
    print(f"{celsius} Ta safe!")
