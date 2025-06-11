import pandas as pd

url_filmes = "Pandas/IMDB-Movie-Data.csv"

df_filmes = pd.read_csv(url_filmes)
# print(df_filmes)
print("dados carregados com sucesso!!!")
#1
filmes_selecionados = df_filmes[["Series_Title","Director","Released_Year"]]
print(f"\nDataFrame com título, Gênero e nota")
print(filmes_selecionados.head())
#2
selecao_especifica = df_filmes.iloc[10:15, 0:3]
print("\n Printando uma seleção específica, linha 10 a 15 e coluna 0 a 3")
print(selecao_especifica)

#3 
df_coluna = df_filmes.set_index("IMDB_Rating")

top_5_rank = df_coluna.loc[1:5, ["Series_Title","Gross"]]
print("\n Filmes de rank 1 a 5 com Receita:")
print(df_coluna[["Series_Title", "Gross"]].head())

#4
# filmes_frentes = df_filmes[df_filmes["Released_Year"] >= "2016"]
# print("\n filmes acima de 2016 (primeiras linhas)")
# print(filmes_frentes[["Released_Year","Series_Title","Genre"]].head())

#professor

#Converter a coluna "Released_Year" para numérico, caso ainda não esteja
df_filmes["Released_Year"] = pd.to_numeric(df_filmes["Released_Year"], errors="coerce")
#pd.to_numeric ele e usado para coverter para numerico a string, funciona tanto com float quanto inteiro
#errors="coerce" usado para caso tenha numeros invalidos ou vazio, ele coloca como [num]

#Filtra os filmes com ano >= 2016
filmes_pos_2016 = df_filmes[df_filmes["Released_Year"] >= 2016]
[["Series_Title", "Released_Year"]]
print("\n4. Filmes lançados a partir de 2016:")
print(filmes_pos_2016)

