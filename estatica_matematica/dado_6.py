import numpy as np
lancamentos = np.random.randint(1, 7, size=5000)
prob_estimada = np.mean((lancamentos == 6) | (lancamentos == 4))
print(prob_estimada)