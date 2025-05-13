conta = int(input("Qual o valor da conta? "))
gorgeta = int(input("Qual percentual de gorjeta? "))

total_gorjeta = (conta * gorgeta) / 100

total_conta = conta + total_gorjeta

print(f"Gorjeta: {total_gorjeta} \n Total: {total_conta}")