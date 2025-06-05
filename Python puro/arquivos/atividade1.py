#o arquivo frutas.csv contém nomes de frutas e seus preços. escreva uma função chamada frutas, que leia o arquivo e retorne um dicionário com base no conteúdo. No dicionário, o nome da fruta deve ser a chave, e o valor deve ser seu preço. Os preços devem ser do tipo float.



# def frutas():
#     dici_frutas = {}
#     with open("arquivos/frutas.csv") as arquivo:
#         for linha in arquivo:
#             # print(f"Linha: {linha.strip()}")
#             partes = linha.strip().split(";") #strip ele tira o \n no final da linha 
#             nome = partes
#             preco = partes
#             dici_frutas[nome[0]] = float(preco[1])
#     return dici_frutas
# print(frutas())

#professor

def frutas():
    dicionario_frutas = {}
    
    try:
        with open("arquivos/frutas.csv") as arquivo:
            for linha in arquivo:
                linha = linha.replace("\n","")
                if linha:
                    dados = linha.split(";")
                    dicionario_frutas[dados[0]] = float(dados[1])
                    
    except FileNotFoundError:
        print("Arquivo 'frutas.csv' não encontrado.")
        
    except ValueError:
        print("Erro ao converter o preço para float.")
        
    return dicionario_frutas

print(frutas())
