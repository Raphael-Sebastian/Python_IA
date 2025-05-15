
#tentativa

# texto = input("Digite uma string: ")

# if len(texto) < 30:
#     preenchido = "*" * (30 - len(texto))
#     resultado = preenchido + texto
    
#resultado
    
texto = input("Digite uma palavra ou frase: ")
#largura total
largura_total = 30
#linhas do topo e do rodapé
linha_borda = "*" * largura_total
#aqui é o espaço total disponivel tirando o tamanho da palavra
espacos_total = largura_total - len(texto)
#aqui é quanto de espaço para esquerda que é o espaco_total dividido por 2
espacos_esquerda = espacos_total // 2
#aqui é o espaço da direita
espacos_direita = espacos_total - espacos_esquerda-2
#aqui monta a linha central

if len(texto) % 2 == 0:
    linha_central = "*" + " " * espacos_esquerda + texto + " " * espacos_direita + "*"
else:
    linha_central = "*"+ texto + "*"
    
    print(linha_borda)
    print(linha_central)
    print(linha_borda)