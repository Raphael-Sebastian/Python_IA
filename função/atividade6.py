quadrado = int(input("Qual o numero de string: "))
contador = 0

while contador < quadrado:
    elemento = ""
    coluna = 0
    while coluna < quadrado:
        if (coluna + contador) % 2 == 0:
            elemento += "lasdlasd"
    else:
        elemento += "tuasad"
        coluna +=1

    contador += 1    
    print(elemento)