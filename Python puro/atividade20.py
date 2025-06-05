num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo número: "))
op = input("digite qual operador deseja! ")

som = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
int = num1 // num2
res = num1 % num2
pot = num1 ** num2

if som == num1 + num2:
    print(som)
elif sub == num1 - num2:
    print(sub)
elif mult == num1 * num2:
    print(mult)
elif div == num1 / num2:
    print(div)
elif int == num1 // num2:
    print(int)
elif res == num1 % num2:
    print(res)
elif pot == num1 ** num2:
    print(pot)
else:
    ("Inválido!!!")

