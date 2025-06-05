#1.1
#Crie um programa que exiba a seguinte mensagem na tela:

#resposta

# variavel = "Bem-vindo ao mundo da programação!"
# print (variavel)

#2.1
#Declare variáveis para armazenar:
# Seu nome
# Sua idade
# Sua altura
# Se você está estudando Python (valor booleano)
# Depois, exiba essas informações usando o comando print().

# resposta

# nome = "Rafael"  
# idade = 22  
# altura = 1.79  
# aprendendo = True
# print (nome,idade, altura, aprendendo)

#2.2
#Crie duas variáveis com números inteiros, some-as e mostre o resultado.

#resposta

# a = 10
# b = 3
# print (a + b)

#3.1
#Solicite ao usuário que informe seu nome e idade. Em seguida, mostre a mensagem: Olá, [nome]! Você tem [idade] anos.
# Olá, [nome]! Você tem [idade] anos.

#resposta

# nome = input("Qual é o seu nome? ")
# print("Olá,", nome)

# idade = int(input("Qual é a sua idade? "))
# print("Sua idade é,", idade)

# print (f"{nome}, você tem {idade} anos" )
#3.2
#Peça dois números ao usuário, some-os e exiba o resultado na tela.

#resposta

# numero1 = int(input("Digite o primeiro número: "))

# numero2 = int(input("Digite o segundo número: "))

# print( numero1 + numero2)

#4.1
# Peça um número ao usuário e exiba:
# O dobro
# O triplo
# A raiz quadrada

#resposta

# numero = float(input("Digite um número: "))


# dobro = numero * 2
# triplo = numero * 3
# raiz_quadrada = numero ** 0.5


# print("O dobro de", numero, "é", dobro)
# print("O triplo de", numero, "é", triplo)
# print("A raiz quadrada de", numero, "é", raiz_quadrada)

#4.2
# Crie um programa que calcule o IMC (Índice de Massa Corporal).
# Fórmula: IMC = peso / altura ** 2

#resposta

# peso = float(input("Digite seu peso em kg: "))
# altura = float(input("Digite sua altura em metros: "))

# imc = peso / altura ** 2

# print("Seu IMC é:", imc)

#5.1
# Peça a idade do usuário e classifique conforme a faixa etária:
# Criança (até 12 anos)
# Adolescente (13 a 17 anos)
# Adulto (18 a 59 anos)
# Idoso (60 anos ou mais)

#resposta

# idade = int(input("Digite sua idade: "))

# if idade <= 12:
#     print("Você é uma criança.")
# elif 13 <= idade <= 17:
#     print("Você é um adolescente.")
# elif 18 <= idade <= 59:
#     print("Você é um adulto.")
# else:
#     print("Você é um idoso.")


#5.2
# Peça uma nota entre 0 e 10 e informe:
# Aprovado (nota maior ou igual a 7)
# Recuperação (nota entre 5 e 6.9)
# Reprovado (nota menor que 5)

# nota = float(input("Digite sua nota: "))

# if nota <= 5:
#     print("reprovado.")
# elif nota >=7:
#     print("Aprovado.")
# elif 5 <= nota <= 6.9:
#     print("Você está de recuperação.")



#6.1
#Faça um programa que conte de 1 a 10 utilizando o laço while.

#resposta

# contador = 1
# while contador <= 10:
#     print("Contando", contador)
#     contador += 1

#6.2
#Solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando o laço for.

#resposta

# num = int(input("Digite o número: "))


# for i in range(1, 11):
#     print(num * i)