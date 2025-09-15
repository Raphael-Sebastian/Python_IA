#meu

# import numpy as np
# bolas = ["R","R","R","B","B"]
# sorteios = 10000

# resultados = [np.random.choice(bolas) for _ in range(sorteios)]
# resultados = np.array(resultados)

# evento_a = resultados == "R"
# evento_b = np.arange(sorteios) % 2 == 1

# probabilidade = np.mean(evento_a | evento_b)
# print(f"probabilidade: {probabilidade:.2f}")

#professor

#jogue dado 10000 mill vezs em array, iremos jogar de novo 10000 entre a soma desses dois dar 7

import numpy as np
bolas = ['R','R','R','B','B']
n_sim = 10000
resultados = []

for _ in range(n_sim):
    np.random.shuffle(bolas)
    sorteio = bolas[0]
    resultados.append(sorteio)

resultados = np.array(resultados)
A = resultados == 'B'
B = np.arange(n_sim) % 5 == 0

P_sim = np.mean(A | B)
# P_sim = np.mean(A & B)
print(f"Exercício - Probabilidade (bola azul ou índice múltiplico de 5) ~ {P_sim:.2f}")