#criar a funcao quadratica generica em python e repasssar os parametros na chamada exemplo: grafico_quadratica(1,-3,2)

import numpy as np
import matplotlib.pyplot as plt

def grafico_quadratica(a, b, c):
    x = np.linspace(-10,10,400)
    
    y = a * x**2 + b*x+c

    plt.figure(figsize=(8,6))
    plt.plot(x,y, label=f"{a}x**2 + {b}x + {c} ")
    plt.title("Gráfico da função")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
    
grafico_quadratica(1,-3,2)