senha = input("Crie uma senha: ")
while True:
    senha_certa = input("Digite sua senha novamente: ")
    if senha_certa == senha:
        print (f"Senha correta: {senha} ")
        break
    else:
        print("Senha diferente. Tente novamente")