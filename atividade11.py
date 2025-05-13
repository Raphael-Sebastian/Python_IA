capital = int(input("Qual o seu capital inicial? "))
taxa = int(input("Qual taxa de juros? "))
tempo = int(input("Quantos anos? "))

juros = capital * (taxa / 100) * tempo
montante = capital + juros
print(f"Resultado: {montante}")