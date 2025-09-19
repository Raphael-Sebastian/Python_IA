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

sns.scatterplot(x="Idade", y="Salário", hue="Departamento", data=df)
plt.title("Idade x Salário")
plt.show()

#matriz dre correlação
correlacao = df.corr(numeric_only=True)
print("Correlação entre variáveis:")
print(correlacao)

#heatmap para visualização
sns.heatmap(correlacao, annot=True, cmap="coolwarm")
plt.title("Mapa de correlação")
plt.show()

plt.figure(figsize=(8,6))
sns.violinplot(x="Departamento", y="Salário", data=df)
plt.title("Distribuição do Salário por Departamento")
plt.show()