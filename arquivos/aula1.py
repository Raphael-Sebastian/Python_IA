conteudo = None
try:
    with open("arquivos/exemplo.txt") as novo_arquivo: #with para ele abrir o arquivo no caso estamos atrás do exemplo.txt
        
        # conteudo = novo_arquivo.read()
        # print(conteudo)
        for linha in novo_arquivo:
            print(linha)
            
except FileNotFoundError: #não foi encontrado o arquivo
    print("Não encontramos o arquivo")