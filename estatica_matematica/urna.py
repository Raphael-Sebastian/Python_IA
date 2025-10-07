import numpy as np
bolas = ['R','R','R','R','R','B','B','B','B','B','B','B']
n_sim = 10000
resultados = []

for _ in range(n_sim):
    np.random.shuffle(bolas)
    sorteio = bolas[0]
    resultados.append(sorteio)

resultados = np.array(resultados)
A = resultados == 'R'
B = np.arange(n_sim) % 2 == 1

P_sim = np.mean(A | B)
print(f"Exercício - Probabilidade (bola vermelha ou índice ímpar) ~ {P_sim:.2f}")

# 

# import numpy as np

# bolas = ['R','R','R','R','R','B','B','B','B','B','B','B']
# n_sim = 10000
# resultados = []

# for _ in range(n_sim):
#     np.random.shuffle(bolas)
#     sorteio = bolas[0]  # Retira a primeira bola após embaralhar
#     resultados.append(sorteio)

# resultados = np.array(resultados)
# P_vermelha = np.mean(resultados == 'R')

# print(f"Probabilidade simulada de sair bola vermelha: {P_vermelha:.4f}")

# import random

# urna_original = ['V', 'V', 'V', 'G', 'G']
# simulacoes = 10000
# casos_favoraveis = 0

# for _ in range(simulacoes):
#     urna = urna_original.copy()
#     random.shuffle(urna)

#     primeira = urna.pop(0)  # Retira a primeira bola

#     if primeira == 'V':
#         segunda = urna.pop(0)  # Retira a segunda bola
#         if segunda == 'G':
#             casos_favoraveis += 1

# # Cálculo da probabilidade condicional: P(segunda = verde | primeira = vermelha)
# prob = casos_favoraveis / simulacoes
# print(f"Probabilidade estimada: {prob:.4f}")




# import numpy as np

# bolas = np.array(['R','R','R','R','R','B','B','B','B','B','B','B'])
# n_sim = 10000

# # --- Sem reposição ---
# sucessos_sem = 0
# for _ in range(n_sim):
#     np.random.shuffle(bolas)
#     if bolas[0] == 'R' and bolas[1] == 'R':
#         sucessos_sem += 1

# prob_sem = sucessos_sem / n_sim

# # --- Com reposição ---
# sucessos_com = 0
# for _ in range(n_sim):
#     primeira = np.random.choice(bolas)
#     segunda = np.random.choice(bolas)
#     if primeira == 'R' and segunda == 'R':
#         sucessos_com += 1

# prob_com = sucessos_com / n_sim

# # --- Resultados ---
# print(f"Probabilidade (2 vermelhas sem reposição): {prob_sem:.4f}")
# print(f"Probabilidade (2 vermelhas com reposição):  {prob_com:.4f}")
