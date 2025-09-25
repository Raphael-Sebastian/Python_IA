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

#exiba a quantidade de registros por produto, calcule a receita media por produto e por região

quantidade_produto = df["Produto"].value_counts()
print("\nQuantidade de registro por produto:")
print(quantidade_produto)

receita_media = df.groupby("Produto")["Receita Total"].mean()
print("\nReceita média por produto")
print(receita_media)

receita_regiao = df.groupby("Região")["Receita Total"].mean()
print("\nReceita média por região:")
print(receita_regiao)

#10.histograma da coluna vendas (com kde=True). 11 boxplot da receita total por região

# plt.figure(figsize=(10,6))
# sns.histplot(data=df, x="Vendas", kde=True, bins=30, color="skyblue")
# plt.title("Histograma da coluna Vendas")
# plt.xlabel("Vendas")
# plt.ylabel("Frequência")
# plt.tight_layout()
# plt.show(block=False)

# # 11 boxplot da receita total por região

# plt.figure(figsize=(10,6))
# sns.boxplot(data=df, x="Região", y="Receita Total")
# plt.title("Boxplot da Receita Total por Região")
# plt.xlabel("Região")
# plt.ylabel("Receita Total (R$)")
# plt.tight_layout()
# plt.show(block=False)

# #12. grafico de barras com a receita média por produto. 13. scatterplot mostrando a relação entre vendas e receita total, colorindo por produto. 14.heatmap de correlação entre as variaveis numericas(vendas, preco  unitario, receita)

# #12. grafico de barras com a receita média por produto.

# plt.figure(figsize=(12,6))
# sns.barplot(x=receita_media.index, y=receita_media.values)
# plt.title("Receita Média por Produto")
# plt.xlabel("Produto")
# plt.ylabel("Receita Média (R$)")
# plt.tight_layout()
# plt.show(block=False)

# # 13. scatterplot mostrando a relação entre vendas e receita total, colorindo por produto.

# plt.figure(figsize=(12,8))
# sns.scatterplot(data=df, x="Vendas", y="Receita Total", hue="Produto", alpha=0.7)
# plt.title("Relação Entre Vendas e Receita Total por Produto")
# plt.xlabel("Vendas")
# plt.ylabel("Receita Total (R$)")
# plt.tight_layout()
# plt.show(block=False)

# # 14.heatmap de correlação entre as variaveis numericas(vendas, preco  unitario, receita)

# plt.figure(figsize=(8,6))

# colunas_heat =["Vendas","Preço Unitário","Receita Total"]
# corr = df[colunas_heat].corr()

# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.title("Heatmap de correlação entre Variáveis Númericas")
# plt.show(block=False)
# input("Presione Enter para fechar tudo...")
# plt.close("all")

# #15. um grafico aonde mostra as vendas por mês crie uma coluna Mes a partir da coluna Data.

# df["Mes"] = df["Data"].dt.to_period("M")

# vendas_mes = df.groupby("Mes")["Vendas"].sum()
# print("\n Vendas por mês")
# print(vendas_mes)

# #faça um grafico de linha mostrando a evolução mensal das vendas

# plt.figure(figsize=(8,4))
# vendas_mes.plot(kind="line", marker="o")
# plt.title("Vendas por Mês")
# plt.ylabel("Unidades")
# plt.show()

#16.media movel: calcule a media movel de 7 dias da receita total e plote em um grafico de linha para detectar tendencia.

# df = df.sort_values("Data")

# receita_diaria = df.groupby("Data")["Receita Total"].sum().reset_index()
# receita_diaria["Média Móvel 7 Dias"] = receita_diaria["Receita Total"].rolling(7).mean()

# plt.figure(figsize=(12,6))
# plt.plot(receita_diaria["Data"], receita_diaria["Receita Total"], label="Receita Diária", marker="o", linestyle="-", alpha=0.6)

# plt.plot(receita_diaria["Data"], receita_diaria["Média Móvel 7 Dias"], label="Média Móvel (7 dias)", color="red", linewidth=2)

# plt.title("Tendência da Receita Total com Média Móvel de 7 dias")
# plt.xlabel("Data")
# plt.ylabel("Receita Total (R$)")
# plt.grid()
# plt.tight_layout()
# plt.show()

#17. produto mais vendido por região

vendas_regiao = df.groupby(["Região", "Produto"])["Vendas"].sum().reset_index()

produto_regiao = vendas_regiao.loc[vendas_regiao.groupby("Região")["Vendas"].idxmax()]

print("\n===Produto mais Vendido por Região===")
print(produto_regiao)

preco_medio = df.groupby(["Região", "Produto"])["Preço Unitário"].mean().reset_index()
print(preco_medio)

pivot = preco_medio.pivot(index="Produto", columns="Região", values="Preço Unitário")