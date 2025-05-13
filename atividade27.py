produto = int(input("Digite o valor do produto: "))

if produto <=50:
    print("Produto da categoria econõmica. ")
elif produto >= 50 and produto <= 100:
    print("Produto da categoria intermediária. ")
else:
    print("Produto da categoria premium. ")