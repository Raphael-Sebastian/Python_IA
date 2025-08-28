import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)

df_produtos["valor_estoque"] = df_produtos["preco_venda"] * df_produtos["estoque_atual"]

valor_total_estoque = df_produtos["valor_estoque"].sum()

print(valor_total_estoque)