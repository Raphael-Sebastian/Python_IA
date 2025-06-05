#função chamar outra função

# def cumprimentar(nome):
#     print(f"olá {nome}")
    
# def cumprimentar_vezes(nome, vezes):
#     while vezes > 0:
#         cumprimentar(nome)
#         vezes -= 1
        
#         cumprimentar_vezes("Maria",5)
        

def resultado():
    resultado = 25 + 25
    return resultado

def calculo(x):
    soma = x + resultado()
    print(soma)
    
calculo(50)