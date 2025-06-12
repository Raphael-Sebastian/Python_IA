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

# Garantindo que as colunas estão numéricas

df_filmes_completo['Gross'] = df_filmes_completo['Gross'].str.replace(',','.')
df_filmes_completo['Gross'] = pd.to_numeric(df_filmes_completo['Gross'], errors='coerce')
df_filmes_completo['Meta_score'] = pd.to_numeric(df_filmes_completo['Meta_score'], errors='coerce')
print(df_filmes_completo['Gross'])

# Criando uma cópia do DataFrame original
df_filmes_preenchido_media = df_filmes_completo.copy()
 
# Preenchendo os NaNs
df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media['Gross'].fillna(df_filmes_preenchido_media['Gross'].mean())
df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media['Meta_score'].fillna(df_filmes_preenchido_media['Meta_score'].mean())
 
# Verificando se ainda existem NaNs nessas colunas
print("\nValores ausentes após preenchimento:")
print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum())

#Professor

# import pandas as pd
 
# url_filmes = "IMDB-Movie-Data.csv"
 
# df_filmes = pd.read_csv(url_filmes)
 
# print("Valores ausentes por coluna:")
# print(df_filmes[['Gross', 'Meta_score']].isna().sum())
 
# df_filmes_completo = df_filmes.dropna()
 
# print(f"\nNúmero de linhas no DataFrame original: {len(df_filmes)}")
# print(f"Número de linhas após remover todas com NaN: {len(df_filmes_completo)}")
 
# # Garantindo que as colunas estão numéricas
# df_filmes_completo['Gross'] = df_filmes_completo['Gross'].str.replace(',','.')
# df_filmes_completo['Gross'] = pd.to_numeric(df_filmes_completo['Gross'], errors='coerce')
# df_filmes_completo['Meta_score'] = pd.to_numeric(df_filmes_completo['Meta_score'], errors='coerce')
# print(df_filmes_completo['Gross'])
# # Criando uma cópia do DataFrame original
# df_filmes_preenchido_media = df_filmes_completo.copy()
 
# # Preenchendo os NaNs
# df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media['Gross'].fillna(df_filmes_preenchido_media['Gross'].mean())
# df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media['Meta_score'].fillna(df_filmes_preenchido_media['Meta_score'].mean())
 
# # Verificando se ainda existem NaNs nessas colunas
# print("\nValores ausentes após preenchimento:")
# print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum())