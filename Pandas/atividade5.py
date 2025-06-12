import pandas as pd

url_filmes = "Pandas/IMDB-Movie-Data.csv"

df_filmes = pd.read_csv(url_filmes)

#conte quantas vezes cada ator aparece na coluna "Director". mostre os 5 atores mais frequentes do DataFrame.

contagem_diretores = df_filmes["Director"].value_counts()
print("\n Os 10 dirretores mais frequentes: ")
print(contagem_diretores.head(5))

#ordene os filmes pelo tempo de duração (Runtime) em ordem decrescente e mostre os 10 filmes mais longos.

df_ordenando_por_tempo = df_filmes.sort_values(by="Runtime",ascending=False)
print("\n Top 5 Filmes por nota (Runtime):")
print(df_ordenando_por_tempo)

#Ordene os filmes por "Certificate" (ordem alfabética) e, em seguida, por "Meta_score" em ordem descrescente. Mostre os 5 filmes do resultado
df_filmes["Meta_score"] = pd.to_numeric(df_filmes ["Meta_score"], errors="coerce")
filmes_ordenados = df_filmes.sort_values(by=["Certificate","Meta_score"], ascending=[True,False])


#converta as colunas "Meta_score" e "Runtime" para tipo numérico, tratando valores inválidos com errors="coerce"
# df_filmes["Meta_score"] = df_filmes["Meta_score"].str.replace(",","")
df_filmes["Runtime"] = df_filmes["Runtime"].str.replace("min","")
df_filmes["Meta_score"] = pd.to_numeric(df_filmes["Meta_score"], errors="coerce")
df_filmes["Runtime"] = pd.to_numeric(df_filmes["Runtime"], errors="coerce")

#agrupe os dados por "Certificate", calculando: a média de "Runtime" (tempo de duração), a média de "Meta_score" e o total de folmes por centificado

calculando = df_filmes.groupby("Certificate").agg(
    Media_Runtime=("Runtime", "mean"),
    Media_Meta_score=("Meta_score", "mean"),
    Total_Filmes=("Series_Title", "count"),
)
print(calculando)

# #professor

# import pandas as pd
 
# # Carregar os dados
# df_filmes = pd.read_csv("IMDB-Movie-Data.csv")
 
# #Contar quantos filmes cada diretor dirigiu
# diretores_freq = df_filmes['Director'].value_counts().head(5)
# print("Diretores com mais filmes:")
# print(diretores_freq)
 
# # Ordenar os filmes pelo runtime e descrescente
# df_filmes['Runtime'] = df_filmes['Runtime'].str.replace(' min','')
# df_filmes['Runtime'] = pd.to_numeric(df_filmes['Runtime'], errors='coerce')
# filmes_mais_longos = df_filmes.sort_values(by='Runtime', ascending=False).head(10)
# print("\nTop 10 filmes mais longos:")
# print(filmes_mais_longos[['Series_Title', 'Runtime']])
 
# #Ordenar por 'Certificate' (ordem alfabética) e depois por 'Meta_score's
# df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')
# filmes_ordenados = df_filmes.sort_values(by=['Certificate', 'Meta_score'], ascending=[True, False])
# print("\nFilmes ordenados por Certificate e Meta_score:")
# print(filmes_ordenados[['Series_Title', 'Certificate', 'Meta_score']].head(5))
 
# #Agrupamento por 'Certificate'
# agrupado = df_filmes.groupby('Certificate').agg({
#     'Runtime': 'mean',
#     'Meta_score': 'mean',
#     'Series_Title': 'count'  # contar número de filmes
# }).rename(columns={'Title': 'Total_filmes'})
 
# print("\nEstatísticas por Certificate:")
# print(agrupado)