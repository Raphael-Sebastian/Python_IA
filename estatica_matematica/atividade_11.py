#media, mediana e moda descricao calcule medidas de tendecias central tarefa crie uma lista de 10 numeros aleatorios entre 1 e 50 calcule a media, mediana e moda dica use numpy e statstics

import statistics 
import random

numeros = [random.randint(1,50) for _ in range(10)]
print(numeros)

media = statistics.mean(numeros)
print("Média:", media)

mediana = statistics.median(numeros)
print("Mediana:", mediana)

try:
    moda = statistics.mode(numeros)
    print("Moda:", moda)
except:
    print("Moda: Não tem moda (todos os números são unicos)")