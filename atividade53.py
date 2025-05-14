saldo = 500

print(f"Seu saldo atual é R$ {saldo}")
while True:
    saque = int(input("Digite o valor que deseja sacar, deve ser múltiplo de 10: "))
    
    if saque % 10 != 0:
        print("O valor deve seer múltiplo de 10.")
    elif saque > saldo:
        print("Saldo insuficiente.")
    elif saque <= 0:
        print("Valor inválido.")
    else:
        saldo -= saque
        print(f"Saque de R$ {saque} realizado com sucesso!")
        print(f"Saldo restante: R$ {saldo}")
        break
