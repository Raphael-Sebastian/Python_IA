#correlação simples descricao:amalise a relacao entre duas variaveis tarefa: crie duas listas de 10 numeros aleatorios repesentando altura e peso. 2 calcule a correlação de pearson entre elas usando numpy e analise os resultados. usar: altura=[160,165,170,175,180,185,160,170,175,180] peso=[55,60,65,70,75,80,58,68,72,77]

import numpy as np

altura=[160,165,170,175,180,185,160,170,175,180]
peso=[55,60,65,70,75,80,58,68,72,77]

correlacao = np.corrcoef(altura, peso)[0,1]
print(f"Coeficiente de correlação de Pearson: {correlacao:.2f}")