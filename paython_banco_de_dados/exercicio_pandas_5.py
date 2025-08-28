import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

df_menor_margem = pd.read_sql("""SELECT nome_produto, preco_custo, preco_venda, (preco_venda - preco_custo) AS margem_lucro FROM produtos ORDER BY margem_lucro ASC LIMIT 5""", con=engine )

print(df_menor_margem)