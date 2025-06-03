#crie um programa que: Peça ao usuário para digitar um número divisor e um índice para acessar em uma lista. a lista deve ter 3 números. use try e except para capturar divisão por zero, indice invalido e qualquer outro erro generico.

numero = [10,20,30]

try:
    divisor = int(input("Digite um número divisor: "))
    indice = int(input("Digite um índice (0 a 2): "))
    
    resultado =  numero[indice] / divisor
    print(f"Resultado da divisão: {resultado}")
    
except ZeroDivisionError:
    print("Erro: Divisão por zero não e permitida.")
    
except IndexError:
    print("Erro: Índice fora da lista")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    