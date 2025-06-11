#1. Crie uma nova coluna chamada "Rating_Metascore_Diff" que seja a diferença absoluta entre "IMDB_Rating" e ("Metascore"/10). (Divida metascore por 10 para colocá-lo numa escala similar ao Rating)

import pandas as pd

url_filmes = "Pandas/IMDB-Movie-Data.csv"

df_filmes = pd.read_csv(url_filmes)
# print(df_filmes)
# print("dados carregados com sucesso!!!")

# df_filmes["Rating_Metascore_Diff"] = df_filmes["IMDB_Rating"] - (df_filmes["Meta_score"] / 10)
# print(df_filmes.head())

# #2. Mostrar as colunas "Series_Title","IMDB_Rating","Meta_score", e a nova "Rating_Metascore_Diff" para os primeiros 5 filmes

# print(df_filmes[['Series_Title', 'IMDB_Rating', 'Meta_score', 'Rating_Metascore_Diff']].head(5))

# #3. Remova a coluna "Overview" do df_filmes.Crie um novo DataFrame para isso, não altere o original.

# df_filmes_sem_overview = df_filmes.drop(columns=["Overview"])
# print(df_filmes_sem_overview.head())

# #4. Renomei a coluna "No_of_Votes" para "Numero_Votos".Faça isso no DataFrame original usando inplace=True. Verifique se a coluna foi renomeada.

# df_filmes.rename(columns={"No_of_Votes": "Numero_Votos"}, inplace=True)
# print("Deu certo")
# print(df_filmes.columns.tolist())

#Converter "Meta_score" para numérico se necessário
df_filmes["Meta_score"] = pd.to_numeric(df_filmes["Meta_score"], errors="coerce")

#Criar a nova coluna com a diferença absoluta
df_filmes["Rating_Metascore_Diff"] = df_filmes["IMDB_Rating"] - (df_filmes ["Meta_score"] / 10)

#Printar somente
print("\nDiferença entre nota do IMDB e Metascore (primeiros 5 filmes):")
print(df_filmes[['Series_Title', 'IMDB_Rating', 'Meta_score', 'Rating_Metascore_Diff']].head(5))

#Criar um novo DataFrame sem a coluna "Overview"
df_filmes_sem_overview = df_filmes.drop(columns=["Overview"])

print("\nColunas após remoção da descrição:")
print(df_filmes_sem_overview.columns.tolist())

#Renomeando com inplace=True
df_filmes.rename(columns={"No_of_votes": "Numero_Votos"}, inplace=True)

#Verificar se foi renomeada
print("\nVerificação das colunas após renomear 'No_of_votes':")
print(df_filmes.columns.tolist())