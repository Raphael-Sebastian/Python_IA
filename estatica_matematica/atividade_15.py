#percentis e quartis descricao: divida os dados em partes para anlise tarefa 1. utilize a lista do exercicio 2. numeros=[12,15,12,18,20,15,22,19,15,10] 2. calcule o 25, 50 e 75 percentil

import numpy as np

numeros = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]

q1 = np.percentile(numeros, 25)
q2 = np.percentile(numeros, 50)
q3 = np.percentile(numeros, 75)

print(f"25 percentil (Q1): {q1}")
print(f"50 percentil (Q1): {q2}")
print(f"75 percentil (Q1): {q3}")