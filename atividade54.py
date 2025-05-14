
while True:
    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    
    if len(palavra1) == len(palavra2):
        print("São tamanhos iguais")
        break
    else:
        print("Tamanhos diferentes")
    
