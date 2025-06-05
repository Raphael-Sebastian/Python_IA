# palavra1 = "ex"
# palavra2 = "emplo"
# palavraCompleta = palavra1 + palavra2

# print(palavraCompleta * 5)

# print("-" * len(palavraCompleta))

#pratica

# p1 = input("Palavra 1: ")
# p2 = input("Palavra 2: ")

# if len(p1) > len(p2):
#     print(p1)
# elif len(p1) == len(p2):
#     print("São iguais de tamnho")
# else:
#     print(p2)

# entrada = input("Digite um texto: ")

# ultimo = len(entrada) - 1
# print(f"O último caracter da palavra é {entrada[ultimo]}")

p1 = input("Digite uma string: ")

penultimo = len(p1) -2

if p1[penultimo] == p1[1]:
    print(f"São iguais letra 1: {p1[penultimo]} e o letra 2: {p1[1]}")
else:
    print("Não são iguais")