#crie uma função para resolver ax^2 + bx + c =0 def bhaskara(a,b,c):

import math

def bhaskara(a,b,c):
    if a == 0:
        return ("Não é uma equação do segundo grau.")
    

    delta = b**2 - 4*a*c
    
    if delta < 0:
        return ("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        return (f"A equação possui uma raiz real: x = {x}")
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)
        return (f"A equação possui duas raizes reais: x1 = {x1}, x2 = {x2}")
    
print(bhaskara(1, -3, 2))
print(bhaskara(1, -2, 1))
print(bhaskara(1, 2, 5))