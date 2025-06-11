#1. verifique quantos valores ausentes existem nas colunas "Gross" e "Meta_Score" do df_filmes original

import pandas as pd

url_filmes = "Pandas/IMDB-Movie-Data.csv"

df_filmes = pd.read_csv(url_filmes)
# print(df_filmes)
print("dados carregados com sucesso!!!")

valores_ausentes = df_filmes[["Gross","Meta_score"]].isna().sum()
print("Funciono!!!")
print(valores_ausentes)

#2. Crie um novo DataFrame chamado df_filmes_completo removendo todas as linhas que tenham qualquer valor ausente. Quantas linhas restam?

df_filmes_completo = df_filmes.dropna()

num_linhas_restantes = len(df_filmes_completo)
print("Funciono!!!")
print(f"Números de linhas restantes: {num_linhas_restantes}")

#3. Crie outro DataFrame chamado df_filmes_prenchido_media. Nele, preencha os valores ausentes de "Gross" com a média dessa coluna e os valores ausentes de "Meta_score" com a mediana dessa coluna. Verifique se ainda há NaNs nessas colunas

df_filmes_preenchidos_media = df_filmes.copy