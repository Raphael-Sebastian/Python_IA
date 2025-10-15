#Carregue o arquivo industria.csv no Python usando pandas. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv("projeto_menu/industria.csv")

# print(df)

#Exercício 1 – Receita total por fábrica 

# Calcule a receita total de cada fábrica.

receita_frabrica = df.groupby("Fabrica")["Receita"].sum().reset_index()

print(f"Receita total por fábrica:",receita_frabrica)

#Gere um gráfico de barras mostrando a receita total por fábrica. 

plt.figure(figsize=(10,6))
plt.bar(receita_frabrica["Fabrica"], receita_frabrica["Receita"], color="skyblue")

plt.title("Receita Total por Fábrica")
plt.ylabel("Receita Total (R$)")
plt.tight_layout()
plt.show(block=False)

#Qual fábrica teve a maior receita? 

fabrica_maior = receita_frabrica.loc[receita_frabrica["Receita"].idxmax()]

print("Fábrica com maior receita:")
print(fabrica_maior)

#Qual a diferença entre a fábrica com maior receita e a de menor receita? 

maior_receita = receita_frabrica["Receita"].max()
menor_receita = receita_frabrica["Receita"].min()

receita_diferente = maior_receita - menor_receita

print(f"A diferença entre a maior e a menor receita é de R${receita_diferente:.2f}")

#Exercício 2 – Receita média por produto 

#Calcule a receita média de cada produto. 

receita_media_produto = df.groupby("Produto")["Receita"].mean().reset_index()

print(f"Receita média por produto: ", receita_media_produto)

#Gere um gráfico de barras mostrando a receita média por produto. 

plt.figure(figsize=(10,6))
plt.bar(receita_media_produto["Produto"], receita_media_produto["Receita"], color = "green")

plt.title("Receita Média por Produto")
plt.ylabel("Produto")
plt.ylabel("Receita Média")
plt.tight_layout()
plt.show(block=False)


#Qual produto tem a maior receita média? 

produto_maior_media = receita_media_produto.loc[receita_media_produto["Receita"].idxmax()]

print(f"Produto com a maior receita média é: ", produto_maior_media)

#Algum produto apresenta receita média significativamente menor? Qual? 

produto_menor_media = receita_media_produto.loc[receita_media_produto["Receita"].idxmin()]

print(f"O produto com a menor receita média é: ", produto_menor_media)

#Exercício 3 – Quantidade vendida total por mês 

#Crie uma coluna Mes a partir da data de cada registro. 

df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.month

print(df[["Data", "Mes"]].head())

#Calcule a quantidade total vendida por mês. 

quantidade_vendida_por_mes = df.groupby("Mes")["Quantidade_Vendida"].sum().reset_index()

print("Quantidade total vendida por mês: ")
print(quantidade_vendida_por_mes)

#Gere um gráfico de linha mostrando a evolução da quantidade vendida ao longo dos meses. 

plt.figure(figsize=(10,6))
plt.plot(quantidade_vendida_por_mes["Mes"], quantidade_vendida_por_mes["Quantidade_Vendida"])

plt.title("Evolução da Quantidade Vendida por Mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade Vendida")
plt.grid(True)
plt.tight_layout()
plt.show(block=False)


#Qual mês teve a maior quantidade vendida? 

mes_maior_venda = quantidade_vendida_por_mes.loc[quantidade_vendida_por_mes["Quantidade_Vendida"].idxmax()]

print(f"O mês com a maior quantidade vendida foi:")
print(mes_maior_venda)

#Existe tendência de aumento ou diminuição ao longo do período? 

primeiro_mes = quantidade_vendida_por_mes.iloc[0]["Quantidade_Vendida"]
ultimo_mes = quantidade_vendida_por_mes.iloc[-1]["Quantidade_Vendida"]

if ultimo_mes > primeiro_mes:
    print("Tendência de aumento na quantidade vendida.")
elif ultimo_mes < primeiro_mes:
    print("Tendência de diminuição na quantidade vendida.")
else:
    print("Sem tendência clara na quantidade vendida.")
    
#Exercício 4 – Lucro médio por fábrica 

#Crie uma coluna Lucro = Receita - Custo. 

df["Lucro"] = df["Receita"] - df["Custo"]
print(df[["Receita", "Custo", "Lucro"]].head())

#Calcule o lucro médio por fábrica usando groupby. 

lucro_medio_por_fabrica = df.groupby("Fabrica")["Lucro"].mean().reset_index()

print("Lucro médio por fábrica:")
print(lucro_medio_por_fabrica)

#Gere um gráfico de barras usando seaborn mostrando o lucro médio por fábrica. 

plt.figure(figsize=(10,6))
sns.barplot(x="Fabrica", y="Lucro", data=lucro_medio_por_fabrica)

plt.title("Lucro médio por fábrica")
plt.xlabel("Fábrica")
plt.ylabel("Lucro médio")

plt.tight_layout()
plt.show(bloSck=False)



#Qual fábrica é mais lucrativa em média? 

fabrica_mais_lucrativa = lucro_medio_por_fabrica.loc[lucro_medio_por_fabrica["Lucro"].idxmax()]

print("A fábrica mais lucrativa em média é:")
print(fabrica_mais_lucrativa)

#Alguma fábrica apresenta lucro negativo em algum registro? 

print("Existe lucro negativo? ", (df["Lucro"]< 0).any)

#Exercício 5 – Receita total por fábrica e produto 

#Use groupby ou pivot_table para calcular a receita total para cada combinação de fábrica e produto. 

receita_total = df.groupby(["Fabrica", "Produto"])["Receita"].sum().reset_index()
print(receita_total)

#Gere um heatmap com seaborn mostrando a receita por fábrica (linhas) e produto (colunas). 

receita_pivot = pd.pivot_table(df, values="Receita", index="Fabrica", columns="Produto", aggfunc="sum")


plt.figure(figsize=(12,8))
sns.heatmap(receita_pivot, annot=True, fmt=".0f")

plt.title("Receita total por fábrica e produto")
plt.xlabel("Produto")
plt.ylabel("Fábrica")

plt.tight_layout()
plt.show(block=False)
input("Presione Enter para fechar tudo...")
plt.close("all")

#Qual produto gera mais receita em cada fábrica? 

receita = df.groupby(["Fabrica", "Produto"])["Receita"].sum()

maior_receita_fabrica = receita.groupby(level=0).idxmax()

print(maior_receita_fabrica)

#Existe algum produto que não foi produzido ou vendido em alguma fábrica? 

fabricas = df["Fabrica"].unique()
produtos = df["Produto"].unique()

combinacoes_reais = df[["Fabrica", "Produto"]].drop_duplicates()

total_combinacoes = len(fabricas) * len(produtos)
combinacoes_existentes = len(combinacoes_reais)

if combinacoes_existentes < total_combinacoes:
    print("Existe pelo menos um produto que não foi produzido/vendido em alguma fábrica.")
else:
    print("Todos os produtos foram produzidos/vendidos em todas as fábricas.")
    
