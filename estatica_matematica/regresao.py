import numpy as np
from sklearn.linear_model import LinearRegression

#Dados ficiticios
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) #variavel independente
y = np.array([2, 4, 5, 4, 5]) #variavel dependente

#Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(x, y)

#Coeficientes
a = modelo.coef_[0]   #inclinação
b = modelo.intercept_ #intercepto
print(f"Equação da reta: y = {a:.2f}x + {b:.2f}")

#Previsão
x_novo = np.array([[6]])
y_previsto = modelo.predict(x_novo)
print(f"Para x=6, y previsto é {y_previsto[0]:.2f}")