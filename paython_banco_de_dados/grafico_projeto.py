# 1-conecta ao banco
# 2-coleta os dados de venas
# 3-treina um modelo de regressão linear
# 4-avaliar o modelo com r2
# 5-faz uma previsão com novos dados(entrada do usuário)







import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:123456@localhost/sistema_vendas")

query = """
SELECT
    p.nome_produto,
    SUM(i.quantidade) AS total_vendido,
    AVG(i.preco_unitario) AS preco_medio,
    SUM(i.quantidade * i.preco_unitario) AS faturamento
FROM itens_pedido i
JOIN produtos p ON p.produto_id = i.produto_id
GROUP BY p.produto_id
"""

df = pd.read_sql(query, engine)


X = df[["total_vendido", "preco_medio"]]
y = df["faturamento"]

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

previsao = modelo.predict(X_teste)

erro = mean_squared_error(y_teste, previsao)
r2 = r2_score(y_teste, previsao)

print(f"\nModelo treinado com sucesso!")
print(f"Erro médio quadrático (MSE): {erro:.2f}")
print(f"Coeficiente R²: {r2:.2f}")
print(f"Raiz do erro médio quadrático (RMSE): R$ {math.sqrt(erro):.2f}")

plt.scatter(y_teste, previsao)
plt.xlabel("Faturamento Real")
plt.ylabel("Faturamento Previsto")
plt.title("Previsão vs Real")
plt.grid(True)
plt.show()

try:
    print("\n Previsão de faturamento")
    unidades = int(input("Digite a quantidade vendida: "))
    preco = float(input("Digite o preço médio por unidade (R$): "))
    
    novo_dado = pd.DataFrame([[unidades,preco]], columns=["total_vendido", "preco_medio"])
    previsao2 = modelo.predict(novo_dado)
    
    print(f"Faturamento estimado para {unidades} unidades a R$ {preco:.2f}: R$ {previsao2[0].item():.2f}")
    
except Exception as e:
    print(f"Erro ao prever: {e}")