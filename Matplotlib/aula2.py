import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

#usando metodo de seno do numpy
y_linha = np.sin(x)

categorias = ["Ação","Comédia","Drama","Terror"]

valores = [20,40,50,20]

#dados por gráfico de dispersão
x_scatter = np.random.rand(50)

y_scatter = x_scatter + np.random.randn(50)*0.1

#Histograma

hist_data = np.random.randn(1000)

fig, axs = plt.subplots(2,2, figsize=(10,8))

axs[0,0].plot(x,y_linha, color="blue", linestyle= "--", label="sin(x)")

axs[0,0].set_title("Gráfico de linha")
axs[0,0].legend()

axs[0,1].bar(categorias, valores, color=["green","red","blue","purple"])
axs[0,1].set_title("Grafico de barras")

axs[1,0].scatter(x_scatter,y_scatter, alpha=0.6,color="red")
axs[1,0].set_title("Gráfico de Dispersão")

axs[1,1].hist(hist_data,bins=30, color="blue", edgecolor="black")
axs[1,1].set_title("Histograma")

fig.tight_layout()

plt.show() 

