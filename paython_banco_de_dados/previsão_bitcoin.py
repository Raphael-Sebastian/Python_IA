import pandas as pd
import math 
from sklearn.model_selection import train_test_split # treino modelo
from sklearn.linear_model import LinearRegression # criar futuro
from sklearn.metrics import mean_squared_error, r2_score # medir o modelo para ver se está bom
from sqlalchemy import create_engine
import matplotlib.pyplot as plt # Para plotar gráficos

url_bitcoin = "paython_banco_de_dados/bitcoin_historico.csv" # Caminho para o arquivo CSV

# # ETAPA 1 ---------------------------------------------------------------------
# df_bitcoin = pd.read_csv(url_bitcoin) # eê o arquivo CSV com os dados históricos do Bitcoin
# print("\n conectado com sucesso!!! ")
# print(df_bitcoin) # exibe o DataFrame para confirmar que os dados foram carregados

# df_bitcoin = pd.DataFrame({"Data": ["2025-09-01", "2025-08-31", "2025-08-30"]}) # Cria um novo DataFrame com datas fictícias
# df_bitcoin["Data"] = pd.to_datetime(df_bitcoin["Data"]) # converte a coluna "Data" para datetime
# print(df_bitcoin["Data"].dtype) # verifica o tipo da coluna "Data"

# df_ordernar_recente_antiga = df_bitcoin.sort_values(by="Data", ascending=False) # Ordena da data mais recente para a mais antiga
# print("\n dados recentes/ antigos")
# print(df_ordernar_recente_antiga) # mostra os dados ordenados

# # ETAPA 2 ---------------------------------------------------------------------
# df_bitcoin = pd.read_csv(url_bitcoin) # recarrega o CSV com os dados reais
# print("\n conectado com sucesso!!! ")
# print(df_bitcoin) # exibe o DataFrame novamente

# # define as colunas que serão convertidas para formato numérico
# colunas_bitcoin = ["Último", "Abertura", "Máxima", "Mínima", "Var%"]

# # faz a limpeza e conversão das colunas numéricas
# for coluna in colunas_bitcoin:
#     df_bitcoin[coluna] = (
#         df_bitcoin[coluna]
#         .astype(str) #converte para string (caso ainda não seja)
#         .str.replace(".", "", regex=False) # remove pontos usados como separadores de milhar
#         .str.replace(",", ".", regex=False) # troca vírgulas por pontos (formato decimal)
#         .str.replace("%", "", regex=False) # remove o símbolo de porcentagem
#         .str.strip() # remove espaços em branco
#     )
#     df_bitcoin[coluna] = pd.to_numeric(df_bitcoin[coluna], errors="coerce") # converte para float
# print(df_bitcoin[["Data", "Último", "Abertura", "Máxima", "Mínima", "Vol.", "Var%"]].head()) # mostra as primeiras linhas

# # ETAPA 3 ---------------------------------------------------------------------
# df_bitcoin = pd.read_csv(url_bitcoin) # lê o CSV novamente
# print(df_bitcoin)
# df_bitcoin["Data"] = pd.to_datetime(df_bitcoin["Data"], dayfirst=True) # converte a coluna "Data" para datetime com dia primeiro

# # define intervalos de treino e teste
# treino_comeco = "2020-01-01"
# fim_treino = "2025-08-16"
# inicio_teste = "2025-08-17"
# fim_teste = "2025-09-01"

# # filtra os dados para o conjunto de treino
# df_treino = df_bitcoin[(df_bitcoin["Data"] >= treino_comeco) & (df_bitcoin["Data"] <= fim_treino)]
# # filtra os dados para o conjunto de teste
# df_teste = df_bitcoin[(df_bitcoin["Data"] >= inicio_teste) & (df_bitcoin["Data"] <= fim_teste)]

# print("Treino:")
# print(df_treino) # exibe os dados de treino

# print("Teste:")
# print(df_teste) # exibe os dados de teste

# # ETAPA 4/5 ---------------------------------------------------------------------
# df_bitcoin = pd.read_csv(url_bitcoin) # lê os dados novamente

# # converte a coluna "Data" para datetime
# df_bitcoin["Data"] = pd.to_datetime(df_bitcoin["Data"], dayfirst=True, errors="coerce")

# # define intervalo a ser filtrado para o modelo
# inicio = pd.to_datetime("2020-01-01")
# fim = pd.to_datetime("2025-08-16")

# # filtra os dados apenas entre as datas de treino
# df_filtrado = df_bitcoin[(df_bitcoin["Data"] >= inicio) & (df_bitcoin["Data"] <= fim)]

# # define as colunas que serão usadas
# colunas_bitcoin = ["Último", "Abertura", "Máxima", "Mínima"]

# # limpa e converte essas colunas para float
# for coluna in colunas_bitcoin:
#     df_bitcoin[coluna] = (
#         df_bitcoin[coluna]
#         .astype(str)
#         .str.replace(".", "", regex=False)
#         .str.replace(",", ".", regex=False)
#         .str.strip()
#     )
#     df_bitcoin[coluna] = pd.to_numeric(df_bitcoin[coluna], errors="coerce")

# # define variáveis independentes (X) e dependente (y)
# X = df_bitcoin[["Abertura", "Máxima", "Mínima"]] # entradas
# y = df_bitcoin["Último"] # Saída

# # divide os dados em treino e teste (aleatoriamente)
# X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# # cria o modelo
# modelo = LinearRegression()
# modelo.fit(X_treino, y_treino) # treina o modelo com os dados

# # faz previsões no conjunto de teste
# previsao = modelo.predict(X_teste)
# df_teste["previsao_fechamento"] = modelo.predict(X_teste)



# # calcula métricas de erro
# erro = mean_squared_error(y_teste, previsao)
# r2 = r2_score(y_teste, previsao)

# # exibe os resultados
# print(f"Erro médio quadrático: {erro:.2f}")
# print(f"Coeficiente R2: {r2:.2f} ")
# print(f"Raiz de erro médio quadrático em R$: {math.sqrt(erro)}")

# ETAPA 6 ---------------------------------------------------------------------
df_bitcoin = pd.read_csv(url_bitcoin) # lê os dados novamente
df_bitcoin["Data"] = pd.to_datetime(df_bitcoin["Data"], dayfirst=True) # converte a coluna "Data"

# define novamente os intervalos de treino e teste
treino_comeco = "2020-01-01"
fim_treino = "2025-08-16"
inicio_teste = "2025-08-17"
fim_teste = "2025-09-01"

# separa os dados com base nas datas
df_treino = df_bitcoin[(df_bitcoin["Data"] >= treino_comeco) & (df_bitcoin["Data"] <= fim_treino)].copy()
df_teste = df_bitcoin[(df_bitcoin["Data"] >= inicio_teste) & (df_bitcoin["Data"] <= fim_teste)].copy()

# define as colunas numéricas a serem tratadas
colunas = ["Último", "Abertura", "Máxima", "Mínima"]

# limpa e converte para float os valores numéricos no treino e teste
for df in [df_treino, df_teste]:
    for coluna in colunas:
        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.strip()
        )
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce")
    df.dropna(subset=colunas, inplace=True) # remove linhas com valores ausentes

# treinar o modelo com os dados de treino
X_treino = df_treino[["Abertura", "Máxima", "Mínima"]]
y_treino = df_treino["Último"]
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

# fazer previsões com os dados de teste
X_teste = df_teste[["Abertura", "Máxima", "Mínima"]]
df_teste["previsao_fechamento"] = modelo.predict(X_teste)
# Comparação entre valor real e previsão
comparacao = pd.DataFrame({
    "Data": df_teste["Data"],
    "Valor Real (R$)": df_teste["Último"],
    "Previsão (R$)": df_teste["previsao_fechamento"]
})

# Exibe apenas as primeiras linhas
print("\nprevisões VS Valores Reais ")
print(comparacao.head(10))  # mostra as 10 primeiras previsões



# ordena os dados por data para o gráfico
df_teste = df_teste.sort_values("Data")

# cria o gráfico com os valores reais vs previstos
plt.figure(figsize=(10,6))
plt.plot(df_teste["Data"], df_teste["Último"], label="Valor Real", marker="o") # linha de valores reais
plt.plot(df_teste["Data"], df_teste["previsao_fechamento"], label="Previsão", marker="x") # linha de previsões
plt.title("Comparação entre valor real e previsão (fechamento bitcoin)")
plt.xlabel("Data")
plt.ylabel("Cotação (R$)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show() # mostra o gráfico




