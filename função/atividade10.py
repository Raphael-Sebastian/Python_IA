#primeira tentativa

# def mesmo_caracter():
#     caracter = ""
#     argumento1 = 2
#     argumento2 = 2
#     if caracter == argumento1 == argumento2:
#         print(True)
#     else:
#         print(False)
#     mesmo_caracter()

#resultado final meu

# def mesmo_caracter(caracter, argumento1, argumento2):
#     if 0 <=argumento1 < len(caracter) and 0 <= argumento2 < len(caracter):
#         return caracter[argumento1] == caracter [argumento2]
#     else:
#         return False
# print(mesmo_caracter("Rafael", 1, 10))

#professor

def mesmo_caracter(texto, i, j): #defir as variaveis
    if i < 0 or j < 0 or i >=len(texto) or j >= len(texto): #aqui será feito a verificação caso a string não tenha os mesmo dados ela dara retorna false
        return False
    else:
        if texto[i] != texto[j]: #aqui sera verificado se as palavras são diferentes
            return False
        else:
            return True
        
print(mesmo_caracter("Marcelinha",1,9)) #aqui ele printa a função
            
    
#escreva uma função chamada mesmo_caracter, que recebe uma string e dois inteiros como argumentos. OS inteiros se referem a índices dentro da string. A função deve retornar True se os dois caracteres nos índices especificados forem os mesmos. caso contrário, e especialmente se qualquer um dos índices estiver fora do escopo da string, a função retorna false