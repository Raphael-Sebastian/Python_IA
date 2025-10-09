# Capítulo 5 – Visualizações com Matplotlib e Seaborn

# 11.Histograma (Matplotlib e Seaborn) Gere 1000 números aleatórios com distribuição normal (média 60, desvio padrão 15).

# o Plote um histograma com matplotlib.

# o Plote o mesmo histograma com seabor

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dados = np.random.normal(loc=60, scale=15, size=1000)

plt.hist(dados, bins=30, color="blue", edgecolor = "black")
plt.title("Histograma com Matplotlib")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()

sns.histplot(dados, bins=30, color="green", kde=False)
plt.title("Histograma com Seaborn")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()

#12.Gráfico de dispersão (Seaborn) Considere os dados:
# o X = [1, 2, 3, 4, 5]
# o Y = [2, 4, 5, 4, 6] Plote o gráfico de dispersão (scatter plot) usando seaborn.


dados_1 = pd.DataFrame({
    "X": [1,2,3,4,5],
    "Y": [2,4,5,4,6],
})

sns.scatterplot(data=dados_1, x="X", y="Y")
plt.title("Gráfico de Dispersão com Seaborn")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#13.Boxplot (Seaborn) Construa um boxplot para os dados: [7, 8, 5, 6, 12, 14, 15, 8, 9, 10] com seaborn

dados_2 = [7,8,5,6,12,14,15,8,9,10]

sns.boxplot(data=dados)
plt.title("Boxplot com Seaborn")
plt.xlabel("Valaros")
plt.show()

