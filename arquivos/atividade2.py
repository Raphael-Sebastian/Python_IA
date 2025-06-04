#crie um programa em Python que peça ao usuário para digitar um texto e salve esse texto em um arquivo chamado "saida.txt". Se o arquivo não existir, ele deve ser criado.

texto = input("Digite um texto: ")
with open("arquivos/saida.txt", "w") as arquivo:
    arquivo.write(texto)
    
print("Texto salvo aqui 'saida.txt' ALELUIA!!!")