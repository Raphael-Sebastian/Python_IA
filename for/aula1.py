# #for
# # lista = ["Rafael","Brunno","Ana","Carlos","Gabriel"] #lista
# # for nome in lista: #criar para puxar os nome dentro da lista
# #     print(nome) #printar o nome(variavel criada no for *nome*
    
# lista = ["Rafael","Brunno","Ana","Carlos","Gabriel","A"] #lista
# for nome in lista:
#     if len(nome) > 2: #usado para comparação usando IF
#         print(f"O {nome} tem mais de 2 caracteres")
#     else:
#         print(f"{nome} tem menos de 2 caracter") 
    
# #range no for

# #aqui com 2 argumento são quantas iterações quero que o código execute
# for i in range(5,10): #usando o range para digitar o tanto que queremos 
#     print(i)

# #repete o bloco de código pulando de 2 em 2
# for j in range(0,10,2): #e usando 3 argumentos pulando de 2 em 2
#     print(j)
    
#criando uma lista apartir do Range

numero = list(range(3,15)) #assim ele ja cria automatico uma lista, que serve para uso geral
print(numero)

for i in numero:
    print(i)