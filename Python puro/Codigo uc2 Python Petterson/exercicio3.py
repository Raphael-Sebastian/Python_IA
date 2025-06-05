senha_certa = "python123"
tentativas = 3

while tentativas > 0:
    senha_cadastro = input(" Digite sua senha: ")
    if senha_cadastro == senha_certa:

        print("Acesso positivo: ")
        break
    else:   
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta, tentativas restantes {tentativas}")
        else:
            print("Acesso bloqueado! tentativas esgotadas ")

 