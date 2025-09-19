import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


dados = {

"Nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],

"Idade": [23, 31, 29, 35, 28],

"Salário": [2500, 4000, 3700, 5200, 3300],

"Departamento": ["TI", "RH", "TI", "Financeiro", "RH"]

}


df = pd.DataFrame(dados)



# Histograma da idade

sns.histplot(df["Idade"], kde=True)

plt.title("Distribuição de Idades")

plt.show()


# Boxplot do salário por departamento

sns.boxplot(x="Departamento", y="Salário", data=df)

plt.title("Salário por Departamento")

plt.show()

# Gráfico de barras da média salarial por departamento

sns.barplot(x="Departamento", y="Salário", data=df, estimator="mean")

plt.title("Média Salarial por Departamento")

plt.show()

#4️ Gráfico de dispersão (Scatterplot)

sns.scatterplot(x="Idade", y="Salário", hue="Departamento", data=df)

plt.title("Idade x Salário")

plt.show()