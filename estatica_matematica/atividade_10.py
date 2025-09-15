#simule tirar as 3 de uma vez e qual seria a probabilidade de tirar 3 bolas vermelhas em sequencia

import numpy as np

bolas = ['R','R','R','B','B']
numero_jogadas = 10000

vermelhas_tiradas = 0

for _ in range(numero_jogadas):
    sorteio = np.random.choice(bolas, size=3, replace=True)
    if np.all(sorteio == "R"):  
        vermelhas_tiradas += 1
        
probabilidade = vermelhas_tiradas / numero_jogadas

print(f"Probabilidade de tirar 3 bolas vermelhas em sequência: {probabilidade:.4f}")