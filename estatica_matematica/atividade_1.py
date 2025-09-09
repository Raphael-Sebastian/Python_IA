import pandas as np
import matplotlib.pyplot as plt
import numpy as np


#Horas dormidas por noite (exemplo)
horas_dormidas = np.array([4,5,6,7,8,9])

#desempemho em um teste (notas fictícias)
desempenho = np.array([50, 55, 65, 75, 80, 85])

correlacao = np.corrcoef(desempenho, horas_dormidas)[0,1]
print("A correlação seria: ", correlacao)

plt.scatter(horas_dormidas, desempenho) #comando scatter uso especifico para correlação
plt.plot(horas_dormidas, desempenho, color="red")
plt.xlabel("Horas Dormidas")
plt.xlabel("Nota no Teste")
plt.title("Correlação Sono x Desempenho")
plt.show()