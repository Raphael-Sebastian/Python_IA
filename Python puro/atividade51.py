# import re 

# senha = (input(("Digite uma senha de 7 letras é um número: ")))
# while True:
#     # digite = input(("Digite uma senha de 8 letras "))
#     # senha = print(re.search("[A-Z-0-9]",senha))
#     len(senha) <= 8 and re.search("[A-Z]", senha)
#     if senha >= 8:
#         print("Senha invalida")
#     else:
#         print("Senha valida!!!")
    
   
# import re

# while True:
#     senha = input("Digite uma senha de 7 caracteres, incluindo uma letra maiúscula e um número: ")

#     if len(senha) != 7 or re.search("[A-Z]", senha) or  re.search("[0-9]", senha):
#         print("Senha inválida! A senha deve ter 7 caracteres, incluir uma letra maiúscula e um número.")
#     else:
#         print("Senha válida!!!")
#         break

import re

while True:
    senha = input("Digite uma senha: ")
    temMaiscula = re.search("[A-Z]",senha)
    temMinuscula = re.search("[a-z]",senha)
    temNumero = re.search("[0-9]",senha)
    if len(senha) <8:
        print("Senha Precisa ter 8 Caracteres")
        
    elif temMaiscula == None:
        print(" 1 Letra maiúscula")
        
    elif temMinuscula == None:
        print(" 1 Letra minúscula")
        
    elif temNumero == None:
        print(" 1 número")
    else:
        print("Senha compatível")
        break
        