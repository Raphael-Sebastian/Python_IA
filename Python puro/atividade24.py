tempo = int(input("Digite o tempo de amanhã: "))
chuva = (input("Vai ocorrer chuva amanhã? "))
roupa = "Jeans e camiseta"
roupa_frio = "Jeans e camiseta é um suéter"

if tempo > 20:
    print(f"vai chover: {chuva}\nrecomendamos que use {roupa}")
elif tempo >= 10 and tempo < 20:
    print(f"vai chover: {chuva}\nrecomendamos que use {roupa_frio}")
elif tempo >= 5 and tempo < 10:
    print("recomendamos ficar em casa! ")
else:
    print("sem chance!!! ")
    