#2️ Operações básicas com pandas

import pandas as pd


dados = {

"Nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],

"Idade": [23, 31, 29, 35, 28],

"Salário": [2500, 4000, 3700, 5200, 3300],

"Departamento": ["TI", "RH", "TI", "Financeiro", "RH"]

}


df = pd.DataFrame(dados)

# Ver primeiras linhas
print(df.head())


# Estatísticas descritivas (média, desvio padrão, etc.)

print(df.describe())


# Filtrar pessoas com salário acima de 3500

print(df[df["Salário"] > 3500])


# Agrupar por departamento e calcular média salarial

print(df.groupby("Departamento")["Salário"].mean())