#distribuição de frequencia descricao:conte quantas vezes cada valor aparece. tarefa 1 crie um histograma dos números do exercicio 1 usando matplotlib. 2 mostre a frequencia de cada numero usando um dicionario

from collections import Counter
import matplotlib.pyplot as plt

numeros = [12,15,12,18,20,15,22,19,15,10]

frequencia = Counter(numeros)
print("Frequência:", frequencia)

plt.figure(figsize=(8,5))
plt.hist(numeros, bins=range(min(numeros), max(numeros)+2), edgecolor="black", align="left")
plt.title("Histograma dos números")
plt.show()