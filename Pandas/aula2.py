import pandas as pd

url_filmes = "Pandas/IMDB-Movie-Data.csv"

df_filmes = pd.read_csv(url_filmes)
# print(df_filmes)
print("dados carregados com sucesso!!!")

# #Head() e o Tail()

# print("primeiras 5 linhas do dataFrame de filmes")
# print(df_filmes.head())

# #Tail
# print("\n Últimas 5 linhas do DataqFrame de filmes:")
# print(df_filmes.tail())

# #Info

# print("\n Informações sobre o dataFrame")
# print(df_filmes.info())

# print(f"\n O dataframe de filmes tem {df_filmes.shape[0]} e colunas {df_filmes.shape[1]}")

# #Describe
# #Gera estatística do Data Frame

# print("estatítica descritiva do dataframe:")
# print(df_filmes.describe())

# #index
# #Traz informações sobre os índices das linhas

# print("Informações do índice")
# print(df_filmes.index)

#selecionando a coluna "title"
titulos_filmes = df_filmes["Series_Title"]
print("Primeiro 5 títulos")
print(titulos_filmes.head())

#Selecionando multiplas colunas
filmes_selecionados = df_filmes[["Series_Title","Genre","IMDB_Rating"]]
print(f"\nDataFrame com título, Gênero e nota")
print(filmes_selecionados.head())

#Selecionando a primeira linha
#Iloc é usado para selecionar linhas por indice numérico
primeiro_filme = df_filmes.iloc[0]
print("\n Primeiro filme (linha completa):")
print(primeiro_filme)

#Selecionando as 3 primeiras linhas
tres_primeiro_filmes = df_filmes.iloc[0:3]
print("\nTrês primeiros filmes (DataFrame):")
print(tres_primeiro_filmes)

#Selecionando linhas e colunas especificas
selecao_especifica = df_filmes.iloc[[0,3],[1,4]]
print("\n Printando uma seleção específica, linha 0 e 3 e coluna 1 e 4")
print(selecao_especifica)

#Selecionando dados com .loc
#Localiza os dados pelos rótulos.

df_filmes_idx = df_filmes.set_index("Series_Title")
print("\n Definimos o indice agora como Series Titles")
print(df_filmes_idx.head())

poderoso = df_filmes_idx.loc["The Godfather"]
print("\nDados do filme: the GodFather: ")
print(poderoso)

#filtrar os dados baseados em condições (Boolean indexing0)

df_filmes_bem_avaliados = df_filmes[df_filmes["IMDB_Rating"] >= 8.5]
print("\n Filmes com nota >= 8.5 (Primeira linhas)")
print(df_filmes_bem_avaliados[["Series_Title","Genre"]].head())

#Filmes que tem gênero "Action"
filmes_acao = df_filmes[df_filmes["Genre"].str.contains("Action", na=False)]
print("\n Filmes que contem o genero 'Action'")
print(filmes_acao[["Series_Title","Genre"]].head)

#Criar uma nova coluna
df_filmes["Rating_x_10"] = df_filmes["IMDB_Rating"] * 10
print("\n O DataFrame agora tem uma nova coluna: ")
print(df_filmes.head())

# #Conversão da coluna Gross para float e ignorando erros caso falhar
# df_filmes["Gross"] = pd.to_numeric(df_filmes["Gross"], errors="coerce")

# #Agora, convertido o numero Gross em numero, é mais seguro fazer a comparação
# df_filmes["Alta_receita"] = df_filmes["Gross"] > 1000
# print("\n DataFrame com nova coluna 'Alta Receita' (Primeiras linhas)")
# print(df_filmes.head())

#Drop
#Método drop remove uma linha (registro) ou coluna
#axis = 1 - Excluí a coluna
df_filmes = df_filmes.drop("Poster_Link", axis=1)
print(df_filmes.head())

#axis = 0 - exclí o registro
df_filmes = df_filmes.drop(4,axis=0)
print(df_filmes.head())

#Lidando com dados Ausentes
#Verificar dados ausentes com .isna() .sum():

print("\nContagem de valores ausentes por coluna: ")
print(df_filmes.isna().sum())

#Removendo linhas/colunas
#Criando uma cópia para não
df_sem_nan_linhas = df_filmes.copy()

#Removendo todas as linhas que contenham Qualquer valor Nan
#Dropna == ele vai deletar os números 
df_sem_nan_linhas.dropna(inplace=True)
print(f"\n Número de linhas original: {len(df_filmes)}")
print(f"\n Número de linha após drop: {len(df_sem_nan_linhas)}")

#Removendo colunas que tenha qualquer valor Nan
df_sem_nan_colunas = df_filmes.dropna(axis=1)
print(f"Colunas originais: {df_filmes.columns.tolist()}")
print(f"Colunas após dropna: {df_sem_nan_colunas.columns.tolist()}")