import numpy as np
from scipy import stats

notas_iniciais = [82, 76, 88, 91, 69, 73, 85, 79, 90, 77, 84, 80]

media_inicial = np.mean(notas_iniciais)
desvio_inicial = np.std(notas_iniciais, ddof=1)
print("Média inicial:", media_inicial)
print("Desvio padrão inicial:", desvio_inicial)

t_statitica, p_valor = stats.ttest_1samp(notas_iniciais, popmean=75)
print("t =", t_statitica, "p =", p_valor)