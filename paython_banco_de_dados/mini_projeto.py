import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

df = pd.read_sql("SELECT preco_custo, preco_venda, estoque_atual from produtos", con=engine)

preco_custo = df["preco_custo"].to_numpy()
preco_venda = df["preco_venda"].to_numpy()
estoque = df["estoque_atual"].to_numpy()
lucro_unitario = preco_venda - preco_custo

indice_rentabilidade = (lucro_unitario / preco_custo) * 100
df["rentabilidade"] = np.round(indice_rentabilidade,2)

rentabilidade_media = df["rentabilidade"].mean()

abaixo_da_media = df[df["rentabilidade"] < rentabilidade_media]

print(abaixo_da_media)
