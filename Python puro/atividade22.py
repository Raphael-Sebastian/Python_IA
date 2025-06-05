salario = float(input("Digite seu salário por hora: "))

horas = float(input("Digite quantas horas de trabalho: "))

semana = int(input("Digite quantos dias você trabalha: "))

calculo = salario * horas

if semana == 7:
    domingo = salario * horas *2
    print(domingo)
else: 
     print(f"Seu salario seria = {calculo:.2f}")