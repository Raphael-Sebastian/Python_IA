#simule tirar as 3 de uma vez e qual seria a probabilidade de tirar 3 bolas vermelhas em sequencia

import numpy as np

numeros_jogadas = 10000

dado1 = np.random.randint(1, 7, size=numeros_jogadas)

dado2 = np.random.randint(1, 7, size=numeros_jogadas)

dado3 = np.random.randint(1, 7, size=numeros_jogadas)

somar_jogadas = dado1 + dado2 + dado3

soma_dos_eventos = somar_jogadas >= 10

partidas_jogadas = np.mean(soma_dos_eventos)

print(f"Probabilidade (soma dos 3 dados >= 10):{partidas_jogadas:.4f}" )