import pandas as pd

url_filmes = "Pandas/netflix_titles.csv"

df_netflix = pd.read_csv(url_filmes)
# print(df_netflix)
print("Dados carregados com sucesso!!!")

print("Primeiras 7 linhas do dataFrame da netflix")
print(df_netflix.head(7))

print("\n Informações sobre o dataFrame")
print(df_netflix.info())

print(f"\n O dataFrame de filmes tem {df_netflix.shape[0]} e colunas {df_netflix.shape[1]}")

print("Estatítica descritiva do dataFrame:")
print(df_netflix.describe())