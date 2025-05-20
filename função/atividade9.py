def o_maior_numero (a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior
print(o_maior_numero(10,20,5))

def o_maior_numero(a, b, c):
    return max(a, b, c)
print(o_maior_numero(10, 9, 17)) 

