def triangulo(x):
    contador = 0
    while contador < x:
        elementos = "#" * (x - contador)
        print(elementos)
        contador += 1
        
triangulo(5)