#função quadrática (específica) y = x**2 +3x + 5

import math
import numpy as np
def funcao_especifica(x):
    return (x**2 + 3*x + 5)

valores = np.array([0,1,2,3,4,5])
resultados = funcao_especifica(valores)

print("Valores de x:", valores)
print("Resultados f(x):", resultados)

#criar a funcao quadratica generica em python e repasssar os parametros na chamada exemplo: grafico_quadratica(1,-3,2)

