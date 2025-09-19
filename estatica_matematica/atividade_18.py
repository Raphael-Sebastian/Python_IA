#1️Criar um DataFrame com pandas
import pandas as pd


# Criando dados simples

dados = {

"Nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],

"Idade": [23, 31, 29, 35, 28],

"Salário": [2500, 4000, 3700, 5200, 3300],

"Departamento": ["TI", "RH", "TI", "Financeiro", "RH"]

}


df = pd.DataFrame(dados)


print(df)