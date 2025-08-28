import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#conectando no banco
engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

#lendo dados de produtos
df = pd.read_sql("SELECT preco_custo, preco_venda, estoque_atual from produtos", con=engine)

#convertendo colunas em array
preco_custo = df["preco_custo"].to_numpy()
preco_venda = df["preco_venda"].to_numpy()
estoque = df["estoque_atual"].to_numpy()

print("Preço médio de venda:", np.mean(preco_venda))
print("Preço mediano de venda:", np.median(preco_venda))
print(f"Desvio padrão do preço de venda: {np.std(preco_venda):.2f}")
print("Produto mais caro:", np.max(preco_venda))

#Calcular lucro unitário
lucro_unitario = preco_venda - preco_custo
print(f"Lucros unitarios: {lucro_unitario}")

#Lucro total
lucro_total = lucro_unitario * estoque
print("Lucro total por produto em estoque:", lucro_total)

indices = lucro_unitario < 10
produto_com_lucro_baixo = df[indices]
print(produto_com_lucro_baixo[["preco_custo","preco_venda","estoque_atual"]])

#indice de rentabilidade
indice_rentabilidade = (lucro_unitario / preco_custo ) * 100
df["rentabilidade"] = np.round(indice_rentabilidade, 2) #round serve para arredondar 

print(df[["preco_custo", "preco_venda", "rentabilidade"]])