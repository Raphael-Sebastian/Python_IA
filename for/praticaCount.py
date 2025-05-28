#escreva uma função chamada mais_caracteres, que recebe um argumento string. a função retorna o caractere que tem mais ocorrencias dentro da string.

minha_string = "Olá amigos, da rede globo, fique ligado que vai passar a seção da tarde" #definir a string
def mais_caracteres(texto): #definir função
    
    maior_caractere = "" #definir variaveis dentro da função
    maior_contagem = 0
    
    for caractere in texto: #for para achar os caractere dentro do texto
        contagem = texto.count(caractere) #usar o count para contar quantas vezes as letras dentro da variavel caractere existe
        if contagem > maior_contagem: #se for contagem for maior a maior_contagem ele executa a parte de baixo 
            maior_contagem = contagem 
            maior_caractere = caractere
            
    return maior_caractere #retornara o caracter

print(mais_caracteres(minha_string.replace(" ","")))
    