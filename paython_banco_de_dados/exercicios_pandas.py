import pandas as pd
from sqlalchemy import create_engine

#1 Liste os produtos com status "Descontinuado". 
engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)

ativos = df_produtos[df_produtos["status_produto"] == "Descontinuado"]
print(ativos)
#-----------------------------------------------------------------------------------------------------
#2 Calcule o valor total do estoque (preço_venda * estoque_atual). 
# engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)

# df_produtos["valor_estoque"] = df_produtos["preco_venda"] * df_produtos["estoque_atual"]

# valor_total_estoque = df_produtos["valor_estoque"].sum()

# print(valor_total_estoque)
#-----------------------------------------------------------------------------------------------------
#3 Filtre os fornecedores da cidade de "Maringá" e status "Ativo". 
# engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# df_cidade = pd.read_sql("""select * from fornecedores where cidade = "Maringá" and status_fornecedor = "Ativo" """, con=engine)

# print(df_cidade)
#-----------------------------------------------------------------------------------------------------
#4 Agrupe os pedidos por forma de pagamento e calcule o valor médio de frete. 
# engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# df_frete_medio = pd.read_sql("""SELECT forma_pagamento, AVG(valor_frete) AS frete_medio from pedidos GROUP by forma_pagamento""", con=engine)
 
# print(df_frete_medio)
#-----------------------------------------------------------------------------------------------------
#5 Liste os 5 produtos com menor margem de lucro (preco_venda - preco_custo)
# engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

# df_menor_margem = pd.read_sql("""SELECT nome_produto, preco_custo, preco_venda, (preco_venda - preco_custo) AS margem_lucro FROM produtos ORDER BY margem_lucro ASC LIMIT 5""", con=engine )

# print(df_menor_margem)