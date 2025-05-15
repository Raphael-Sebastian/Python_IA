entrada = input("Digite uma string: ")

if len(entrada) < 20:
    preenchido = "*" * (20 - len(entrada))
    resultado = preenchido + entrada
else:
    resultado = entrada[:20]
    

print("Resultado formatado:",resultado)