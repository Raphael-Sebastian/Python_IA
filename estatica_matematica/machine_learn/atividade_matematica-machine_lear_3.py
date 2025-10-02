import numpy as np
import matplotlib.pyplot as plt

# a = 1
# b = 2
# c = -1

# delta = b**2 - 4*a*c
# raiz1 = (-b + np.sqrt(delta)) / (2*a)
# raiz2 = (-b - np.sqrt(delta)) / (2*a)

# x = np.linspace(-3, 2, 100)
# y = a * x**2 + b * x + c


# plt.axhline(0, color="black")
# plt.axvline(0, color="black")
# plt.plot(x, y, label="f(x) = x² + 2x - 1")
# plt.scatter([raiz1, raiz2], [0, 0], color="red", label="Raízes")
# plt.legend()
# plt.grid(True)
# plt.show()

def funcao_quadratica(x):
    return 2*x**2 + 2*x - 1

valores = np.array ([-3,-2,-1,0,1,2,3])
resultados = funcao_quadratica(valores)

print("Valores de x:", valores)
print("Resultados f(x):", resultados)

plt.plot(valores, resultados, marker="o", linestyle="-", color="purple")
plt.title("Gráfico da função f(x) = 2x^2 + 2x - 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()