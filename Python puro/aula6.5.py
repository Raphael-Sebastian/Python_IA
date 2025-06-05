tentativas = 0

while True:
    codigo = input("Digite o seu PIN")
    tentativas += 1
    
    if codigo == "12345":
        sucesso = True
        break

    if tentativas == 3:
        sucesso = False
        break

print("Incorreto...Tente novamente")

if sucesso:
    print("PIN correto inserido")
else:
    print("Muitas tentativas")
    
