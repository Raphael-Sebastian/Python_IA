#A= Carregar e explorar dados
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("estatica_matematica/dados_transporte.csv")
print(df.info())
print(df.head(5))
print(df.isna().sum())

#B = Estatísticas Descritivas
#1 calcular usando pandas e numpy: Média, mediana, desvio-padrao e variancia de passageiros, distanciam ocupacao e receita
colunas = ["Passageiros","Distância (km)", "Ocupação (%)","Receita (R$)"]

for coluna in colunas:
    print(f" Média: {np.mean(df[coluna])}")
    print(f" Mediana: {np.median(df[coluna])}")
    print(f" Desvio-padrão: {np.std(df[coluna], ddof=1)}")
    print(f" Variãncia: {np.var(df[coluna], ddof=1)}")

#2 calcular o percentil 25%, 50%, 75% da receita

receita = df["Receita (R$)"]

q1 = np.percentile(receita, 25)
q2 = np.percentile(receita, 50)
q3 = np.percentile(receita, 75)

print("Percetil 25%", q1)
print("Percetil 50%", q2)
print("Percetil 75%", q3)

# 3.Encontrar a companhia com maior receita total e com maior número de passageiros.

companhia_agrupamento = df.groupby("Companhia")[["Receita (R$)", "Passageiros"]].sum()

companhia_maior = companhia_agrupamento["Receita (R$)"].idxmax()
maior_receita = companhia_agrupamento["Receita (R$)"].max()

companhia_passageiros = companhia_agrupamento["Passageiros"].idxmax()
maior_passageiros = companhia_agrupamento["Passageiros"].max()


print(f"Companhia com maior receita total: {companhia_maior} (R$) {maior_receita:,.2f})")
print(f"Companhia com maior número de passageiros:{companhia_passageiros}({maior_passageiros:,} Passageiros)")

#4.	Contagem de voos por companhia.

contagem_voos = df["Companhia"].value_counts()

print("Contagem de voos por companhia: ")
print(contagem_voos)

#5.	Receita média por companhia e por aeroporto de origem.

receita_media_companhia = df.groupby(["Companhia", "Aeroporto Origem"])["Receita (R$)"].mean()

print("Receita média por companhia e por aeroportos de origem: ")
print(receita_media_companhia)

#C. Visualizações com Seaborn

#1.	Histograma da distribuição de passageiros.
plt.figure(figsize=(10,6))
sns.histplot(df["Passageiros"], bins=30, kde=True, color="skyblue")
plt.title("Distribuição de Passageiros por Voo")
plt.xlabel("Número de Passageiros")
plt.ylabel("Frequências")
plt.tight_layout()
plt.show(block=False)

#2.	Boxplot da ocupação (%) separada por companhia aérea.

plt.figure(figsize=(10,6))
sns.boxplot(x="Companhia", y="Ocupação (%)", data=df)

plt.title("Boxplot da Ocupação (%) por Companhia Aérea")
plt.xlabel("Companhia")
plt.ylabel("Ocupação (%)")
plt.tight_layout()
plt.show(block=False)

#3.	Gráfico de barras da receita média por companhia.

receita_media_df = receita_media_companhia.reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x="Companhia", y="Receita (R$)", data=receita_media_df)
plt.title("Receita Média por Companhia")
plt.ylabel("Receita Média (R$)")
plt.grid(True)
plt.tight_layout()
plt.show(block=False)


#4.	Scatterplot de distância x receita para verificar relação.
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Distância (km)", y="Receita (R$)", hue="Companhia")

plt.title("Scatterplot: Distância x Receita")
plt.xlabel("Distãncia (km)")
plt.ylabel("Receita (R$)")
plt.grid(True)
plt.tight_layout()
plt.show(block=False)


#5.	(Desafio) Heatmap de correlação entre variáveis numéricas (Passageiros, Distância (km), Ocupação (%), Receita (R$)).

colunas_numericas = ["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]
df_corr = df[colunas_numericas]

matriz_corr = df_corr.corr()

plt.figure(figsize=(8,6))
sns.heatmap(matriz_corr, annot=True, cmap="coolwarm")
plt.title("Heatmap de Correlação entre Variáveis Numéricas")
plt.tight_layout()
plt.show(block=False)

#D. Perguntas Analíticas.

#Qual companhia tem maior participação em número de voos?

voos_companhia = df["Companhia"].value_counts()
participacao_percentual = (voos_companhia / voos_companhia.sum()) 
companhia_maior_participacao = participacao_percentual.idxmax()
percentual_maior = participacao_percentual.max()

print(f"Companhia com maior participação em números de voos: {companhia_maior_participacao} ({percentual_maior:.2f}%)")

#A distância influencia a receita?

correlacao = df[["Distância (km)", "Receita (R$)"]].corr()
print("Correlação entre Distância e Receita:")
print(correlacao)

#Os voos com maior ocupação são necessariamente os de maior receita?

correlacao_ocupacao = df["Ocupação (%)"].corr(df["Receita (R$)"])
print(f"Correlação entre ocupação (%) e receita (R$): {correlacao_ocupacao:.2f} ")

#Quais aeroportos de origem concentram mais voos?

voos_aeropotos = df["Aeroporto Origem"].value_counts()

print(voos_aeropotos.head(10))

#E. Extensão 

# Usar groupby para analisar:


# Receita média por mês.
# df["Data"] = pd.to_datetime(df["Data"], errors="coerce", dayfirst=True)
# print(df["Data"].head(10))
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M")
print("\nReceita média por mês:")
print(df.groupby("Mes")["Receita (R$)"].mean())


# Ocupação média por companhia.
ocupacao_media = df.groupby("Companhia")["Ocupação (%)"].mean()

print("Ocupação média por companhia: ")
print(ocupacao_media)

#1)Qual a Rota mais eficiente por companhia (baseado em Ocupação média ou Receita por passageiro)? Mostrar as 5 melhores em ordem decrescente

df["Receita por Passageiro"] = df["Receita (R$)"] / df["Passageiros"]

eficiencia_receita = df.groupby(["Companhia", "Aeroporto Origem", "Aeroporto Destino"])["Receita por Passageiro"].mean()

top5_receita = eficiencia_receita.sort_values(ascending=False).head(5)
print("Top 5 rotas mais eficientes (receita por passageiro):")
print(top5_receita)

#2)Calcular e mostrar graficamente a Evolução mensal do total de passageiros por companhia

df["Data"] = pd.to_datetime(df["Data"], errors="coerce")

df["AnoMes"] = df["Data"].dt.to_period("M")
evolucao = df.groupby(["AnoMes", "Companhia"])["Passageiros"].sum().reset_index()
evolucao_pivot = evolucao.pivot(index="AnoMes", columns="Companhia", values="Passageiros")

plt.figure(figsize=(12, 6))
evolucao_pivot.plot(marker="o")

plt.title("Evolução Mensal do Total de Passageiros por Companhia")
plt.xlabel("Ano-Mês")
plt.ylabel("Total de Passageiros")
plt.grid(True)
plt.legend(title="Companhia")
plt.tight_layout()
plt.show(block=False)
input("Pressione Enter para fechar tudo...")
plt.close("all")

