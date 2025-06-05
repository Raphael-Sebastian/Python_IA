#escreva um programa em python que abra um arquivo chamado "entrada.txt" (supondo que já exista no mesmo diretório) e imprima todo o seu conteúdo no terminal

def ler_arquivo():
    try:                                       #encoding="utf-8" = ele serve para palavras especial
                                      #"r" ele sempre e o padrão e serve para ler 
        with open("arquivos/entrada.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("O arquivo 'entrada.txt' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro a ler o arquivo: {e}")
    
ler_arquivo()