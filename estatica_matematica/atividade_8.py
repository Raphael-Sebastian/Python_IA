import numpy as np

numeros_jogadas = 10000

dado1 = np.random.randint(1, 7, size=numeros_jogadas)

dado2 = np.random.randint(1, 7, size=numeros_jogadas)

somar_jogadas = dado1 + dado2

soma_dos_eventos = somar_jogadas == 7

partidas_jogadas = np.mean(soma_dos_eventos)

print(f"Probabilidade (soma dos dados == 7):{partidas_jogadas:.4f}" )