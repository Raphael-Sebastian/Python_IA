import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Criando um DF de exemplo (DF= DataFrame)

df = pd.DataFrame({
    "filme":["A","B","C","D","E"],
    "nota":[8.5,9.5,7,6.8,5],
    "Receita":[120,80,150,50,60]
})

#Gráfico de Barras com colunas do DataFrame

plt.bar(df["filme"],df["nota"]) #bar == criar um gráfico de barras
plt.title("Notas por filme") #title == titulo
plt.ylabel("Nota") #ylabel == rotulo da coluna 
plt.show() #mostrar o gráfico