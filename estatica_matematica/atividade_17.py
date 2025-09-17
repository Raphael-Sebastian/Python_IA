#criando dados aleatorios descrição: simule dados para treinamento de IA. tarefa: gere 100 números aleatórios com distribuição normal (numpy.random.normal) com média 50 e desvio padrao 10. 2. plote o histograma desses dados.

import numpy as np
import matplotlib.pyplot as plt

dados = np.random.normal(loc=50, scale=10, size=100)

plt.figure(figsize=(8,5))
plt.hist(dados, bins=10, color="skyblue", edgecolor="black")
plt.title("Histograma de dados Distribuição Normal (media:50, escala:10)")
plt.xlabel("Valor")
plt.xlabel("Frequência")
plt.show()