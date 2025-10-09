#5. Média, mediana e moda Com o conjunto de dados: [10, 15, 20, 20, 25, 30, 35], calcule média, mediana e moda utilizando numpy, pandas.

import pandas as pd
import numpy as np
import statistics

dados = [10, 15, 20, 20, 25, 30, 35]

print("Média:", statistics.mean(dados))
print("Médiana:", statistics.median(dados))
print("Moda:", statistics.mode(dados))
print("Desvio padrão:", np.std(dados))
print("Variância:", np.var(dados))

#Variância e desvio padrão Calcule a variância e o desvio padrão do conjunto: [2, 4, 4, 4, 5, 5, 7, 9], usando pandas

dados_1 = [2,4,4,4,5,5,7,9]

print("Desvio padrão:", np.std(dados_1))
print("Variância:", np.var(dados_1))

# 7. Medidas resumo Para os dados [5, 7, 8, 5, 10, 12, 15], calcule:
# o Média
# o Mediana
# o Valor mínimo
# o Valor máximo
# o Amplitude

dados_2 = [5,6,8,5,10,12,15]

media = np.mean(dados_2)
mediana = np.median(dados_2)
valor_minimo = np.min(dados_2)
valor_maximo = np.max(dados_2)
amplitude = valor_maximo - valor_minimo

print("Média:", media)
print("Mediana:", mediana)
print("Valor mínimo:", valor_minimo)
print("Valor máximo:", valor_maximo)
print("Amplitude:", amplitude)