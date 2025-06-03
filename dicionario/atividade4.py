#peça ao usuário o nome de um arquivo para abrir. Use try e except para lidar com o erro caso o arquivo não exista, monstrando uma mensagem "Arquivo não encontrado."

# nome_arquivo = input("Digite o nome do arquivo que você deseja: ")

# try:
#     with open(nome_arquivo, "r") as arquivo:
#         conteudo = arquivo.read()
#         print("Conteudo do arquivo")
#         print(conteudo)
# except FileNotFoundError:
#     print("Arquivo não encontrado.")

arquivo = None

try:
    arquivo = open("dicionario/dados.txt")
    conteudo = arquivo.read()
    print("Arquivo lido com sucesso")
    
except FileNotFoundError:
    print("Arquivo não encontrado.")