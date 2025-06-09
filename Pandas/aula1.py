import pandas as pd

#criando uma série
# idade = pd.Series([1,2,3,4,5,6])
# print(idade)

# idade_nomes = pd.Series([1,2,3,4], index=["Rafael","Ana","Carlos","Gabriel"])
# print(idade_nomes)

#Data frames
dados_alunos = {
    "Nome":["Rafael","Ana","Carlos","Gabriel"],
    "Idade":[1,2,3,5],
    "Curso":["Engenharia","Medicina","Direito","Engenharia"]
}
#df igual data frame
df_alunos = pd.DataFrame(dados_alunos)
print(df_alunos)