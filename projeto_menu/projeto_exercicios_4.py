#Capítulo 4 – Regressão Linear
# 9. Horas de estudo vs. notas Considere os dados:
# o Horas de estudo: [1, 2, 3, 4, 5]
# o Notas: [2, 4, 5, 4, 6] Ajuste uma regressão linear simples e interprete o coeficiente angular.

import numpy as np
from sklearn.linear_model import LinearRegression

x1 = np.array([1,2,3,4,5]).reshape(-1,1)
y1 = np.array([2,4,5,4,6])
modelo1 = LinearRegression()
modelo1.fit(x1,y1)
print("Coeficiente angular:", modelo1.coef_[0])
print("Intercepto:", modelo1.intercept_)
#10. Preço vs. tamanho de imóveis Considere os dados:
# o Tamanho (m²): [50, 60, 70, 80, 90]
# o Preço (mil reais): [150, 200, 210, 240, 280] Ajuste um modelo de regressão linear e estime o preço para um imóvel de 100 m²

tamanho = np.array([50,60,70,80,90])
preco = np.array([150,200,210,240,280])

a_1, b_1 = np.polyfit(tamanho, preco, 1)

preco_100 = a_1 * 100 + b_1

print(f"Coeficiente angular (a): `{a_1:.2f}")
print(f"Coeficiente linear (b): `{b_1:.2f}")
print(f"Preço estimado para 100 m²: {preco_100:.2f} mill reais")

