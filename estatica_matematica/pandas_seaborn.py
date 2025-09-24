#  Gráfico de Barras (Barplot) 

# Mostra a média (ou soma) de vendas por categoria. 

import seaborn as sns 

import matplotlib.pyplot as plt 

import pandas as pd 

df = pd.read_csv("estatica_matematica/dados_produtos_vendas.csv") 

# Soma das vendas por produto 

plt.figure(figsize=(6, 4)) 

sns.barplot(x="Produto", y="Vendas", data=df, estimator=sum) 

plt.title("Vendas Totais por Produto") 

plt.xticks(rotation=45) 

plt.tight_layout() 

plt.show() 

# 💡 Dica: você pode usar estimator=len, sum, mean ou até criar sua própria função. 

# Forma 

# 2️ Gráfico de Linhas (Lineplot) 

# Mostra a evolução das vendas ao longo do tempo. 

plt.figure(figsize=(8, 4)) 

sns.lineplot(x="Data", y="Vendas", data=df, ci=None) 

plt.title("Evolução das Vendas ao Longo do Tempo") 

plt.xticks(rotation=45) 

plt.tight_layout() 

plt.show() 

# 🔍 Ótimo para detectar tendências sazonais ou períodos de queda/aumento. 

# Forma 

# 3️ Gráfico de Dispersão (Scatterplot) 

# Relaciona duas variáveis (ex.: preço x quantidade). 

plt.figure(figsize=(6, 4)) 

sns.scatterplot(x="Preço Unitário", y="Vendas", hue="Produto", data=df) 

plt.title("Preço x Quantidade Vendida") 

plt.tight_layout() 

plt.show() 

# 💡 Ajuda a identificar padrões, clusters ou correlações. 

# Forma 

# 4️ Violin Plot 

# Mostra a distribuição de vendas, semelhante ao boxplot, mas mais informativo. 

plt.figure(figsize=(6, 4)) 

sns.violinplot(x="Produto", y="Vendas", data=df) 

plt.title("Distribuição de Vendas por Produto") 

plt.xticks(rotation=45) 

plt.tight_layout() 

plt.show() 

# 5⃣Pairplot (Matriz de Dispersão) 

# Mostra todas as combinações possíveis de variáveis numéricas em gráficos de dispersão. 

sns.pairplot(df[["Vendas", "Preço Unitário", "Receita Total"]]) 

plt.suptitle("Relação entre Variáveis Numéricas", y=1.02) 

plt.show() 

# 💡 Excelente para entender o relacionamento geral entre variáveis de forma rápida. 

#6️ Countplot (Frequência de Categorias) 

# Mostra a frequência de cada categoria em uma coluna. 

plt.figure(figsize=(6, 4)) 

sns.countplot(x="Região", data=df) 

plt.title("Número de Vendas por Região") 

plt.tight_layout() 

plt.show() 

 