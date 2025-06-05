# with open("arquivos/dados.txt") as arquivo:
#     f = arquivo.readlines() #.read() le todo o arquivo, readline() le uma linha apenas, realines() ele vem em formato de uma lista
#     print(f)
                               #"a" esse modo adiciona uma nova linha a == append
# with open("arquivos/dados.txt", "a") as arquivo:
#     f = arquivo
#     f.write("Nova linha, ALELUAI!!!")
            
                               #"w" esse metodo ele apaga tudo e cria uma nova linha
# with open("arquivos/dados.txt", "w") as arquivo:
#     f = arquivo
#     f.write("Nova linha, ALELUAI!!!")
                                #"x" esse metodo ele cria um novo arquivo, em casa de ja existir ele da erro!!!
with open("arquivos/dados2.txt", "x") as arquivo:
    f = arquivo
    f.write("Nova linha, ALELUAI!!!")
    
