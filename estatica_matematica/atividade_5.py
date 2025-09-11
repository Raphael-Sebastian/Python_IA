import random

pares = [x for x in range(1,7) if x % 2==0]

n_lancamentos = 10000

resultado = [random.randint(1,6) for _ in range(n_lancamentos)]

pares_n = [x for x in resultado if x in pares]

frequencia_par = len(pares_n) / n_lancamentos

print(f"Probabilidade teórica de obter um número par: ")
print(f"Probabilidade simulada após {n_lancamentos} lançamentos: {frequencia_par:.4f}")


#calcule a probabilidade de obter um número par no lançamento de um dado. compare a probabilidade teórica com a simulada o que faz x for x in range(1,7) é uma forma elegante de pesquisar os números pares dentro de uma lista com os valores de um dado? eu posso, ainda, acrescentar uma condição dentro da instrução