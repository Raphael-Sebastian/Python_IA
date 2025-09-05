import statistics
import numpy as np

dados = [10, 20, 20, 30, 40, 50]

print("Média:", statistics.mean(dados))
print("Médiana:", statistics.median(dados))
print("Moda:", statistics.mode(dados))
print("Desvio padrão:", np.std(dados))
print("Variância:", np.var(dados))
