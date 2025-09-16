#exemplo de lista numeros = [12,15,12,18,20,15,22,19,15,10] 2 variancia e desvido padrao descrição meça a dospersão dos dados terefa utilize a lista acima calcule a varianca e o desvido padrao

import statistics
import numpy as np

numeros = [12,15,12,18,20,15,22,19,15,10]

# print("Média:", statistics.mean(numeros))
# print("Médiana:", statistics.median(numeros))
# print("Moda:", statistics.mode(numeros))
print("Desvio padrão:", np.std(numeros))
print("Variância:", np.var(numeros))
