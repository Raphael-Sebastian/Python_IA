#crie uma função que recebe uma lista de produtos e permitido que o usuário digite um nome. O programa informar se o produto está ou não na lista, e repetir até o usuário digitar "sair"

lista = ["Sonic", "Mario", "PacMan", "Kirby"]
def jogos(Lista):
    while True:
        nome = input("Digite um nome de personagem de video game (Digite sair para parar o programa): ")
        if nome in lista:
            print("Nome ja está na lista.")
        
        elif nome == "sair":
            print("Saíndo")
            break
        
        else:
            print("Nome não está listado!!!")
            
jogos(lista)