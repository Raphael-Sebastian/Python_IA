#carregue o arquivo dados_nomes em um Dataframe, garantindo que a coluna data seja interpretada como datas. exiba: dimensao do dataframe (linhas, colunas) tipo de dados de cada coluna primeiras 5 linhas verifique se existem valores nulos dica usar a relacao de comandos df pandas use o metodos como .groupby(), sum(), mean() quantile() e value_counts() para graficos explore sns.histplot(), sns.boxplot(), sns.barplot(), sns.scatterplot() e sns.heatmap

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("estatica_matematica/dados_produtos_vendas.csv", parse_dates=["Data"])
print(df)

# print("Dimensão:", df.shape)

# print("Tipos de dados", df.dtypes)

# print("\nPrimeiras 5 linhas:")
# print(df.head())

# print("\nValores nulos por colunas:")
# print(df.isnull().sum())

#calcule, para as colunas vendas, preço unitario e receita total: media, mediana, desvio padrao, variancia e calcule os percentis 25%, 50% e 75% da coluna receita total

colunas = ["Vendas","Preço Unitário","Receita Total"]

estaticas = df[colunas].agg(["mean", "median", "std", "var"])

print("Estatísticas principais")
print(estaticas)

percentis = df["Receita Total"].quantile([0.25, 0.5, 0.75])

print("\n Percentis de receita total")
print(percentis)


#descubra o produto com maior receita total usando df.groupby

receita_produto = df.groupby("Produto")["Receita Total"].sum()

produto_maior = receita_produto.idxmax()
maior_receita = receita_produto.max()

print(f"O produto com maior receita total é: {produto_maior}")
print(f"Receita total: R$ {maior_receita:.2f}")