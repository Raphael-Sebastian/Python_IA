import numpy as np
import matplotlib.pyplot as plt

np.random.seed()

n = 10000
lancamentos = np.random.choice([0, 1], size=n, p=[0.5, 0.5])
medias = np.cumsum(lancamentos) / np.arange(1, n + 1)

X = np.arange(1, n + 1)
expodencial = 1 / (2 **(np.log10(X)))


plt.figure(figsize=(10,6))
plt.plot(medias, color ="blue",label ="Média acumulada (lei dos Grandes Números)")
plt.axhline(0.5, color="red", label="valor esperado (0.5)")
plt.xlabel("Número de lançamentos")
plt.ylabel("Valor")
plt.title("Lei dos Grandes Números e função exponencial")
plt.legend()
plt.grid(True)
plt.show()