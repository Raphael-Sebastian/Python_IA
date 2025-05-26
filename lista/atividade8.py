#crie uma função que peça ao usuário para cadastrar 5 senhas. Cada senha deve ter pelo menos 8 caracteres e conter um número. Senhas inválidas devem ser rejeitadas com mensagem de erro. Ao final, imprima todas as senhas válidas.
# import re
# senhas = []
# def cadastrar_senha():
#     while len(senhas) <5:
#         senha = input ("Digite uma senha (mínimo 8 caracteres e conter um número) ")
        
#         if len(senha) <8:
#             print("Erro: A senha deve ter pelo menos 8 caracteres.")
#         else:
#             tem_numero = False
#             i = 0
#             while i < len(senha):
#                 if senha[i].isdigit():
#                     tem_numero = True
#                     break
#                 i = i + 1
                
#                 if tem_numero ==False:
#                     print("Erro: A senha deve conter pelo menos um número.")
#                 else:
#                     senhas.append(senha)
                    
#                 i = 0
#                 print("\nSenha válidas cadastradas:")
#                 while i < len(senhas):
#                     print(senhas[i])
#                     i = i + 1
#                 break
                    
# cadastrar_senha()

# senhas = []

# def cadastrar_senha():
#     while len(senhas) < 5:
#         senha = input("Digite uma senha (mínimo 8 caracteres e conter um número): ")

#         if len(senha) < 8:
#             print("Erro: A senha deve ter pelo menos 8 caracteres.")
#         else:
#             tem_numero = False
#             i = 0
#             while i < len(senha):
#                 if senha[i].isdigit():
#                     tem_numero = True
#                     break
#                 i = i + 1

#             if tem_numero == False:
#                 print("Erro: A senha deve conter pelo menos um número.")
#             else:
#                 senhas.append(senha)

#     print("\nSenhas válidas cadastradas:")
#     i = 0
#     while i < len(senhas):
#         print(senhas[i])
#         i = i + 1

# cadastrar_senha()


# professor

import re #importar biblioteca

def cadastrar_senhas():
    senhas = []
    #while de repetição para digitar as senhas
    while len(senhas) <5:
        senha = input(f"Digite a {len(senhas)+1}° senha: ") #feito para pedir ao usario 5 senhas
        
        if len(senha) >= 8 and re.search("[0-9]",senha) != None:
            senhas.append(senha) #verificar se a senha tem numero e se ela tem 8 caracteres e pelo menos um número
        else: #else para caso não cumpra os requisitos de 8 caracteres e um número
            print("Senha inválida! Deve ter pelo menos 8 caracteres E conter um número.")
            
    print("Senhas válidas:") #print para valídar as senhas
    
    i = 0
    while i < len(senhas):
        print(senhas[i])
        i += 1 #while para contar as senhas 
        
cadastrar_senhas()