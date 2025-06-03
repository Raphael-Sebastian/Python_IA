#crie uma lista com 5 frutas. Peça ao usuário um índice para exibir a fruta correspondente. Use try e except para capturar índices inválidos e exibir "índice fora do alcance"

lista = ["banana","maçã","laranja","uva","abacaxi"]

try:
    fruta = int(input("Digite de 0 a 4 para ver a fruta correspondente: "))
    print(f"A fruta no índice é {lista[fruta]}")
except (IndexError):
    print("Erro: Índice fora do alcance") 
    
except (ValueError):
    print("Erro: Não aceita letra")