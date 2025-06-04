#crie um programa que leia um arquivo de texto chamado "texto.txt" e conte quantas linhas ele contém. Ao final, exiba o número de linhas

# with open("arquivos/texto.txt", "r", encoding="utf=8") as arquivo:
#     linhas = arquivo.readlines()
#     print("Número de linhas:", len(linhas))

try:
    with open("arquivos/texto.txt", "r") as arquivo:
        total_linhas = 0
        for linha in arquivo:
            total_linhas += 1
    print(f"O arquivo contém {total_linhas} linhas(s).")
    
except FileNotFoundError:
    print("O arquivo 'texto.txt' não foi encontrado.")