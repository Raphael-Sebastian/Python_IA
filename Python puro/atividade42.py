pin_correto = "4321"
tentativas = 0

while True:
    pin = (input("Digite o código PIN: "))
    if pin == pin_correto:
        print(f"PIN correto! Você errou {tentativas} vez(es) a senha")
        break
    else:
        print("PIN incorreto. Tente novamente.")
        tentativas += 1

# while True:
#     tentativas += 1
#     codigo = input("Digite o seu Pin")
#     tentativas = (codigo)
    
#     if codigo == "12345":
#         sucesso = True
#         break
    
#     if tentativas == codigo:
#         sucesso = False
#         break
    
#     print("Tente novamente!!!")
    
# if sucesso:
#         print("Pin acerto")
# elif tentativas:
#     print (f"contagem de vezes {tentativas}")

