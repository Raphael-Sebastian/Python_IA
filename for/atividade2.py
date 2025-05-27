#escreva uma função chamada anagrams, que recebe duas strings como argumentos. A função retorna True se as strings são anagramas uma da outra. Duas palavras são anagramas se elas contêm exatamente os mesmos caracteres. dica: a função sorted também pode ser usada em strings. 

def anagramas(palavra1,palavra2):
    return sorted(palavra1) == sorted(palavra2)

print(anagramas("tame", "meta"))
print(anagramas("tame", "meta"))
print(anagramas("tame", "meta"))
print(anagramas("tabby", "batty"))
print(anagramas("python", "java"))