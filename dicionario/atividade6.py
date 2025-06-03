#Escolha 3 except que você ainda não usou nas atividades anteriores e tente aplicar em um código.

#importError
#atributeError
#runtimeError

try:
    
    import nao_tem
except ImportError:
    print("Erro: não foi possivel importar, verifique se ele existe.")
    
try:
    texto = "exemplo"
    texto.naotem()
except AttributeError:
    print("Erro: o atributo ou método não existe.")
    
try:
    dados = {
        "nome": "Rafael",
        "idade": 25
    }
    
    print("Profissão:", dados ["profissao"])
    
except KeyError:
    print("Erro: A chave 'profissao' não existe no dicionario.")