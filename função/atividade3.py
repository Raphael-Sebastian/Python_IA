# largura = int((input("Digite quantos hashs vai querer" )))

# def quadrado_hashtag(tamanho):
    
#     tamanho = "#" * largura
#     while True:
#         # tamanho = (input("Digite quantos hashs vai querer"))
#         print(tamanho * largura)

largura = int(input("Digite quantos hashtags você quer: "))

def quadrado_hashtag(tamanho):
    linha = 0
    while linha < tamanho:
        print("#" * tamanho)
        linha += 1

quadrado_hashtag(largura)
