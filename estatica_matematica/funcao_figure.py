import matplotlib.pyplot as plt 

import numpy as np 

#  Como mostrar vários gráficos em janelas separadas com matplotlib sem precisar fechar a anterior antes de abrir a próxima. 
# O segredo é usar figuras independentes (plt.figure()) e chamar plt.show(block=False) para que a execução continue sem "travar" esperando você fechar a janela. 

# Aqui vai um exemplo simples: 

x = np.linspace(0, 10, 100) 

 

# Primeiro gráfico 

plt.figure() 

plt.plot(x, np.sin(x)) 

plt.title("Seno") 

plt.show(block=False)  # NÃO bloqueia o código, janela fica aberta 

 

# Segundo gráfico 

plt.figure() 

plt.plot(x, np.cos(x)) 

plt.title("Cosseno") 

plt.show(block=False) 

 

# Terceiro gráfico 

plt.figure() 

plt.plot(x, np.tan(x)) 

plt.ylim(-10, 10) 

plt.title("Tangente") 

plt.show(block=False) 

 

input("Pressione Enter para fechar tudo...") 

plt.close('all') 


# 🔑 Explicação rápida: 

# plt.figure() → cria uma nova figura (senão o próximo plt.plot sobrescreve o anterior). 

# plt.show(block=False) → exibe o gráfico sem bloquear o código. 

# input() (ou time.sleep()) → serve apenas para evitar que o script feche tudo antes de você ver os gráficos. 

# plt.close('all') → fecha todas as janelas abertas no final (opcional). 

 