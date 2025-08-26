import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")
#mysql+pymysql://: define que estamos usando mysql com driver PyMysql

#root:nome do usuario
#sua_senha: senha do banco
#localhost: onde está o servidor (se for remoto, muda)
#sistema_vendas: nome do banco de dados que vamos consumir.

df_produtos = pd.read_sql("SELECT * FROM produtos", con=engine)
print(df_produtos.head())

# print(df_produtos.shape)
# print(df_produtos.columns)
# print(df_produtos.info())
# print(df_produtos.describe())

#limpeza e transformação
print(df_produtos.isnull().sum()) #para verificar os numeros nulos 

df_produtos["dimensoes"] = df_produtos["dimensoes"].fillna(0)

print(df_produtos.isnull().sum())

print(df_produtos.info())
#limpeza e transformação

#filtros, seleção e agrupamentos

#estamos filtrando o dataframe para selecionar apenas os "Ativos"
ativos = df_produtos[df_produtos["status_produto"] == "Ativo"]

#Filtrar o dataframe para escolher somente os produtos estão abaixo do estoque minimo
abaixo_min = ativos[ativos["estoque_atual"] < ativos["estoque_minimo"]]

print(abaixo_min[['nome_produto','estoque_atual','estoque_minimo']])

df = pd.read_sql("""SELECT c.nome_categoria, p.preco_venda
                 from produtos p
                 join categorias c on p.categoria_id = c.
                 categoria_id""", con=engine)

media_por_categoria = df.groupby('nome_categoria')['preco_venda'].mean()
print(media_por_categoria)
