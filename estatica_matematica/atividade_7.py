import numpy as np
bolas = ["R","R","R","B","B"]
sorteios = 10000

resultados = [np.random.choice(bolas) for _ in range(sorteios)]
resultados = np.array(resultados)

evento_a = resultados == "R"
evento_b = np.arange(sorteios) % 2 == 1

probabilidade = np.mean(evento_a | evento_b)
print(f"probabilidade: {probabilidade:.2f}")