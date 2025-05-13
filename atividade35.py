pontos = int(input("Digite o tanto de pontos que você fez: "))

if pontos == 0:
    print("Impossível")
elif pontos >= 0 and pontos <= 49:
    print("Falha")
elif pontos >= 50  and pontos < 59:
    print("Nota: 1")
elif pontos >= 60 and pontos < 69:
    print("Nota: 2")
elif pontos >= 70 and pontos < 79:
    print("Nota: 3")
elif pontos >= 80 and pontos < 89:
    print("Nota: 4")
elif pontos >= 90 and pontos < 100:
    print("Nota: 5")
elif pontos >= 100:
    print("Impossível!")
    
    