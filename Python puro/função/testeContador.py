numero = int(input("Qual número: "))
contador = 0

while contador < numero:
    elemento = ""
    coluna = 0
    while coluna < numero:
        if (coluna + contador) % 2 == 0:
            elemento += "0"
    else:
        elemento += "1"
        coluna +=1

    contador += 1    
    print(elemento)
    
    
# frase = ""
# palavra1 = "Rafa"
# palavra2 = "VAI DORMIR!!!"

# print (palavra1 + palavra2)