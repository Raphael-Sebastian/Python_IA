import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

df = pd.read_sql("SELECT preco_custo, preco_venda, estoque_atual from produtos", con=engine)

