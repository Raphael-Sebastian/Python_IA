import os

caminho_pdf = "C:/Users/sebastian.8908/Documents/Codigos uc2 Python Petterson, John/Codigo uc2 Python John/projeto_menu/Diagrama_hard.pdf"


while True:
    print("\nMenu :")
    print("1. Exercícios resolvidos de Estatística (PDF)")
    print("2. Quiz: Estatística em IA")
    print("3. Quiz: Machine Learning")
    print("4. Pesquisa sobre uso de IA (PDF)")
    print("0. Sair")
    

    opcao = input("Opção: ")
    
    if opcao == "0":
        print("Volte sempre!!! ")
        break 
    if opcao == "1":
        os.startfile(caminho_pdf)    
    if opcao == "2":
        print()