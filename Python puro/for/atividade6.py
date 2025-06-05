#escreva uma função chmada sem_vogal, que recebe um argumento string. A função retorna uma nova string, que deve ser a mesma que a original, mas com todas as vogais removidas, você pode assumir que a sequência conterá apenas caracteres do alfabeto inglês minúsculo de a a z.

# def sem_vogal(texto):
#     vogais = "aeiou"
#     resultado = ""
#     for letra in texto:
#         if letra in "bcdfghjklmnpqrstvwxyz":
#             resultado += letra
#     return resultado

# print(sem_vogal("Exemplo"))

#professor

def sem_vogal(texto):
    vogais = "aeiou"
    nova_string = ""
    
    for letra in texto:
        if letra not in vogais:
            nova_string += letra
    return nova_string

print(sem_vogal("banana"))