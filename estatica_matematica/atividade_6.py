import random

pares = [x for x in range(1,7) if x % 2==0 or x > 4]

n_lancamentos = 10000

resultado = [random.randint(1,6) for _ in range(n_lancamentos)] #random.randint ele e uma roleta para que fazer uma simulação de dados 

pares_n = [x for x in resultado if x in pares]

frequencia_par = len(pares_n) / n_lancamentos

# print(f"Probabilidade teórica de obter um número par: {resultado} ")
print(f"Probabilidade simulada após {n_lancamentos} lançamentos: {frequencia_par:.4f}")


