import os

caminho_pdf = "C:/Users/sebastian.8908/Documents/Codigos uc2 Python Petterson, John/Codigo uc2 Python John/projeto_menu/Diagrama_hard.pdf"

def quiz_estatistica_ia():
    perguntas = [
        {
            "pergunta": "1. Qual é a distribuição mais usada para modelar erro em regressão linear?", "opcoes": ["A) Distribuição Uniforme", "B) Distribuição Exponencial", "C) Distribuição Normal", "D) Distribuição Binomial"], "resposta": "C"
        },
        {
            "pergunta": "2. Qual medida representa a média dos quadrados dos desvios?", "opcoes": ["A) Variância", "B) Desvio padrão", "C) Moda", "D) Mediana"], "resposta": "A"
        },
        {
            "pergunta": "3. Qual é a distribuição mais usada para modelar erro em regressão linear?", "opcoes": ["A) Distribuição Uniforme", "B) Distribuição Exponencial", "C) Distribuição Normal", "D) Distribuição Binomial"], "resposta": "C"
        },
        {
            "pergunta": "4. Qual é a distribuição mais usada para modelar erro em regressão linear?", "opcoes": ["A) Distribuição Uniforme", "B) Distribuição Exponencial", "C) Distribuição Normal", "D) Distribuição Binomial"], "resposta": "C"
        },
    ]

    print("\nQuiz: Estatística em IA")
    pontuacao = 0
    
    for q in perguntas:
        print("\n" + q["pergunta"])
        for opcao in q["opcoes"]:
            print(opcao)
        resposta_usuario = input("Sua resposta (A, B, C ou D): ").strip().upper()
        
        if resposta_usuario == q["resposta"]:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto. A resposta certa é: {q["resposta"]}")
            
    print(f"\n Resultado Final: {pontuacao} de {len(perguntas)} acertos.")
    input("\nPressione Entr para voltar ao menu")

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
    elif opcao == "1":
        os.startfile(caminho_pdf)    
    elif opcao == "2":
        quiz_estatistica_ia()
    elif opcao == "3":
        print("\nQuiz em desenvolvimento de machine learning...")
    elif opcao == "4":
        print("\nPDF da pesquisa sobre IA ainda não feita.")
    else:
        print("Opção inválida. tente novamente.")