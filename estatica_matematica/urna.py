import numpy as np
bolas = ['R','R','R','B','B']
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

import numpy as np

bolas = ["R", "R", "R", "B", "B"]
sorteios = 10000

resultados = [np.random.choice(bolas) for _ in range(sorteios)]
resultados = np.array(resultados)

evento_A = resultados == "R"
evento_B = np.arange(sorteios) % 2 == 1

probabilidade = np.mean(evento_A | evento_B)
print(f"Probabilidade: {probabilidade:.2f}")
