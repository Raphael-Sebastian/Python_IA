import pandas as pd
# import math 
# from sklearn.model_selection import train_test_split #treino modelp
# from sklearn.linear_model import LinearRegression #cria futuro
# from sklearn.metrics import mean_squared_error, r2_score #medir o modelo para ver se está bom
# from sqlalchemy import create_engine
# import matplotlib.pyplot as plt

url_bitcoin = "paython_banco_de_dados/bitcoin_historico.csv" #conseguir puxar as inforamações do csv

#ETAPA 1 ---------------------------------------------------------------------
# df_bitcoin = pd.read_csv(url_bitcoin) #ler o csv
# print("\n conectado com sucesso!!! ")
# print(df_bitcoin) #print para verificar se esta correto

# df_bitcoin = pd.DataFrame({"Data": ["2025-09-01", "2025-08-31", "2025-08-30"]}) #pegamos os dados do csv, passamos a data como string 
# df_bitcoin["Data"] = pd.to_datetime(df_bitcoin["Data"]) #converter para datetime
# print(df_bitcoin["Data"].dtype) #verificar o tipo da coluna

# df_ordernar_recente_antiga = df_bitcoin.sort_values(by="Data", ascending=False) #usando o sort_values para ordernar os dados recentes
# print("\n dados recentes/ antigos")
# print(df_ordernar_recente_antiga) #print para mostrar em order
# ----------------------------------------------------------------------------

#ETAPA 2 ---------------------------------------------------------------------

df_bitcoin = pd.read_csv(url_bitcoin)
print("\n conectado com sucesso!!! ")
print(df_bitcoin) #print para verificar se esta correto

# df_bitcoin["Último"] = df_bitcoin["Último"].str.replace(".","")
# df_bitcoin["Abertura"] = df_bitcoin["Abertura"].str.replace(".","")
# df_bitcoin["Máxima"] = df_bitcoin["Máxima"].str.replace(".","")
# df_bitcoin["Mínima"] = df_bitcoin["Mínima"].str.replace(".","")
# df_bitcoin["Vol."] = df_bitcoin["Vol."].str.replace(",",".")
# df_bitcoin["Var%"] = df_bitcoin["Var%"].str.replace("%","")


# df_bitcoin["Último"] = pd.to_numeric(df_bitcoin["Último"], errors="coerce")
# df_bitcoin["Abertura"] = pd.to_numeric(df_bitcoin["Abertura"], errors="coerce")
# df_bitcoin["Máxima"] = pd.to_numeric(df_bitcoin["Máxima"], errors="coerce")
# df_bitcoin["Mínima"] = pd.to_numeric(df_bitcoin["Mínima"], errors="coerce")
# df_bitcoin["Vol."] = pd.to_numeric(df_bitcoin["Vol."], errors="coerce")
# df_bitcoin["Var%"] = pd.to_numeric(df_bitcoin["Var%"], errors="coerce")

# print(df_bitcoin) 



colunas_bitcoin = ["Último", "Abertura", "Máxima", "Mínima", "Var%"]

for coluna in colunas_bitcoin:
    df_bitcoin[coluna] = (
        df_bitcoin[coluna]
        .str.replace(".","", regex=False)
        .str.replace(",",".", regex=False)
        .str.replace("%","", regex=False)    
        .str.strip()
    )
df_bitcoin[coluna] = pd.to_numeric(df_bitcoin[coluna], errors="coerce")
print(df_bitcoin[["Data", "Último", "Abertura", "Máxima", "Mínima", "Vol.", "Var%"]].head())

#ETAPA 3 ---------------------------------------------------------------------

# df_bitcoin = pd.read_csv(url_bitcoin)
# print(df_bitcoin)
# df_bitcoin["Data"] = pd.to_datetime(df_bitcoin["Data"], dayfirst=True)

# treino_comeco = "2020-01-01"
# fim_treino = "2025-08-16"
# inicio_teste = "2025-08-17"
# fim_teste = "2025-09-01"

# df_treino = df_bitcoin[(df_bitcoin["Data"] >= treino_comeco) & (df_bitcoin["Data"] <= fim_treino)]
# df_teste = df_bitcoin[(df_bitcoin["Data"] >= inicio_teste) & (df_bitcoin["Data"] <= fim_teste)]

# print("Treino:")
# print(df_treino)

# print("Teste:")
# print(df_teste)

#ETAPA 4 ---------------------------------------------------------------------

