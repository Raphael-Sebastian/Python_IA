#identificação de outliers descricao:detecte valores fora da distribuição comum. tarefa: use a lista [10,12,12,15,18,20,22,100]. calcule o desvio padrao e identifique numeros que estao a mais de 2 desvios padrao da média.


import numpy as np
import matplotlib.pyplot as plt

numeros = [10,12,12,15,18,20,22,100]

media = np.mean(numeros)
desvio_padrao = np.std(numeros)

limite_inferior = media - 2 * desvio_padrao
limite_superior = media + 2 * desvio_padrao

outliers = [x for x in numeros if x < limite_inferior or x > limite_superior]

print(f"Média: {media:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"outliers: {outliers}")

plt.boxplot(numeros, vert=False)
plt.title("Boxplot dos Dados com Outlier")
plt.xlabel("Valores")
plt.grid(True)
plt.show()