#1.	Urna com bolas coloridas​
# Uma urna contém 5 bolas vermelhas e 7 azuis. Qual a probabilidade de retirar uma bola vermelha?

import numpy as np

bolas = ['R','R','R','R','R','B','B','B','B','B','B','B']
n_sim = 10000
resultados = []

for _ in range(n_sim):
    np.random.shuffle(bolas)
    sorteio = bolas[0]
    resultados.append(sorteio)
    
resultados = np.array(resultados)
porcetagem_vermelha = np.mean(resultados == "R")

print(f"Probabilidade de sair bola vermelha: {porcetagem_vermelha:.4%}")

#1.1 calcular a probabilidade de sair 2 vermelhas na sequência (com e sem reposição)

bolas_calcular = np.array(['R','R','R','R','R','B','B','B','B','B','B','B'])

#sem reposição

sucessos_sem = 0
for _ in range(n_sim):
    np.random.shuffle(bolas_calcular)
    if bolas[0] == "R" and bolas[1] == "R":
        sucessos_sem += 1
    
prob_sem = sucessos_sem / n_sim

#com reposição

sucessos_com = 0
for _ in range(n_sim):
    primeira_saida = np.random.choice(bolas_calcular)
    segunda_saida = np.random.choice(bolas_calcular)
    if primeira_saida == "R" and segunda_saida == "R":
        sucessos_com += 1
        
prob_com = sucessos_com / n_sim

print(f"Probabilidade (2 vermelhas sem reposição): {prob_sem:.4f}")
print(f"Probabilidade (2 vermelhas com reposição): {prob_com:.4f}")

#2. .	Lançamento de um dado. Qual a probabilidade de sair um número maior que 3 ao lançar um dado de 6 lados?

import numpy as np
lancamentos = np.random.randint(1, 7, size=5000)
prob_estimada = np.mean(lancamentos > 3)
print(f"Probabilidade estimada de sair número maior que 3: {prob_estimada:.4%}")

#3.	Lançamento de duas moedas​. Qual a probabilidade de sair exatamente uma cara ao lançar duas moedas?

import random


opcoes = ["A","B"]
contagem = 0

for _ in range(10000):
    moeda1 = random.choice(opcoes)
    moeda2 = random.choice(opcoes)
    
    if(moeda1, moeda2).count("A") == 1:
        contagem +=1
        
probabilidade_cara = contagem / 10000
print(f"Probabilidade estimada de sair exatamente cara: {probabilidade_cara:.4%}")

#4.	Probabilidade condicional​. Uma urna tem 3 bolas vermelhas e 2 verdes. Se uma bola é retirada sem reposição e sai vermelha, qual a probabilidade da próxima ser verde?

import numpy as np

bolas = np.array(['R', 'R', 'R', 'G', 'G'])
sucessos = 0
total = 0

for _ in range(n_sim):
    np.random.shuffle(bolas)          
    primeira = bolas[0]               
    segunda = bolas[1]                

    if primeira == 'R':
        total += 1                    
        if segunda == 'G':
            sucessos += 1             

P_sim = sucessos / total
print(f"Probabilidade estimada de depo : {P_sim:.4%}")