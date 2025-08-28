import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

df_frete_medio = pd.read_sql("""SELECT forma_pagamento, AVG(valor_frete) AS frete_medio from pedidos GROUP by forma_pagamento""", con=engine)
 
print(df_frete_medio)