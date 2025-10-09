# Capítulo 3 – Funções Trigonométricas e Logarítmicas
# 8. Enunciado: Usando numpy, gere uma série de valores x (100 números entre 0.1 e 10) e calcule y = sin(x) + log(x). Plote o gráfico.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)

y =np.sin(x) + np.log(x)

plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

