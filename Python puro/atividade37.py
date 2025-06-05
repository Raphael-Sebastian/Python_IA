ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto. ")
else:
    print(f"{ano} não é um ano bissexto. ")


        #primeira tentativa
    
 # if ano % 100 == 0 and ano % 400 == 0 :
#     print("Ano bissexto por 400")
# elif ano % 4 == 0:
#     print("Ano bissexto divido por 4")
# else:
#     print("ERRO!!!")