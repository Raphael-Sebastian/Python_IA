import matplotlib.pyplot as plt
from collections import Counter #biblioteca para contar numeros

dados = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
frequencias = Counter(dados)

plt.bar(frequencias.keys(), frequencias.values())
plt.title("Histograma dos Dados")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()

