# liste o espaço amostral de dois lançamentos de moedas. Depois, simule 10000 lançamentos e verifique se as frequencias empiricas se aproxiam das teoricas. Dica: usar 2 random.choice

import random
from collections import Counter

opcoes = ["A","B"]

resultados = [(random.choice(opcoes), random.choice(opcoes)) for _ in range(10000)]

frequencias = Counter(resultados)

total = sum(frequencias.values())
for resultado in sorted(frequencias):
    proporcao = frequencias[resultado] / total
    print(f"Resultado: {frequencias[resultado]} ({proporcao:.4f})")

#caso o print precise de espaço entre os dados utilizamos o \t exemplo: print("feijao\t arroz")