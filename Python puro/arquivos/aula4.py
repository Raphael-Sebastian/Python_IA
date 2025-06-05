import os

# os.remove("arquivos/dados2.txt") #usado os.remove para remover um arquivo

if os.path.exists("apagar"): #os.path usado para ver se a pasta existe
    print("Sim a pasta existe")
    os.rmdir("apagar") #os.rmdir para apagar o diretorio/pasta
else:
    print("Pasta não existe")
    os.mkdir("CriaApaga") #os.mkdir usado para criar uma nova pasta 