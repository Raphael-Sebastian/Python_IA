# 1 - variaveis

nome = "Rafael"  #- `str` (string): texto, como "Rafael"
idade = 22  #- `int` : números inteiros, como `22`
altura = 1.79  #- `float` : números com vírgula, como `1.75`
aprendendo = True  #- `bool` : verdadeiro ou falso, como "True"

# 2 - Variaveis e tipos de dados

# - `str` (string): texto, como "Rafael"
# - `int` : números inteiros, como `22`
# - `float` : números com vírgula, como `1.75`
# - `bool` : verdadeiro ou falso, como "True"

# visualizador

print (nome, idade, altura, aprendendo)

# 3 entrada de dados

nome = input("Qual é o seu nome?")
print("Olá,", nome)

idade = int(input("Qual é a sua idade?"))
print("Sua idade é,", idade)

altura = float(input("Qual é a sua altura?"))
print ("Sua altura é,", altura)

# 4 Operadores Matemáticos

a = 10
b = 3
print (a + b) #Soma
print (a - b) #Subtração
print (a * b) #Multiplicação
print (a / b) #Divisão
print (a // b) #Divisão inteira
print (a % b) #Resto da divisão
print (a ** b) #Potência

# 5 Condicionais (if, elif, else)

idade = int(input("Digite sua idade: ?"))

if idade >= 18:
    print("Você é maior de idade.")
elif idade > 12:
    print ("Você é adolescente.")
else:
    print ("Você é uma criança")

# 6 Laços de repetição (while e for)

contador = 0
while contador <= 8000:
    print("Contando", contador)
    contador += 1

for i in range(5):
    print ("Repetição", i)

# 7 Listas

# Frutas = ["maçâ", "banana", "laranja"]
# print(Frutas[0]) #maçâ

# for frutas in frutas:
#     print("Fruta", fruta)