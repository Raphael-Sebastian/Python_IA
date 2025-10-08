import os

caminho_pdf = "C:/Users/sebastian.8908/Documents/Codigos uc2 Python Petterson, John/Codigo uc2 Python John/projeto_menu/Diagrama_hard.pdf"

def quiz_estatistica_ia():
    perguntas = [
        {
            "pergunta": "1. Qual é a distribuição mais usada para modelar erro em regressão linear?",
            "opcoes": ["A) Distribuição Uniforme", "B) Distribuição Exponencial", "C) Distribuição Normal", "D) Distribuição Binomial"],
            "resposta": "C"
        },
        {
            "pergunta": "2. O que significa o p-valor em testes de hipótese?",
            "opcoes": [
                "A) A média da amostra",
                "B) A probabilidade de a hipótese nula ser verdadeira",
                "C) A probabilidade de obter um resultado tão extremo quanto o observado, assumindo a hipótese nula verdadeira",
                "D) A variância dos dados"
            ],
            "resposta": "C"
        },
        {
            "pergunta": "3. Qual métrica estatística mede a dispersão dos dados?",
            "opcoes": ["A) Média", "B) Mediana", "C) Moda", "D) Desvio Padrão"],
            "resposta": "D"
        },
        {
            "pergunta": "4. O que representa a correlação de Pearson?",
            "opcoes": [
                "A) A relação causal entre duas variáveis",
                "B) A tendência central dos dados",
                "C) A força e direção da relação linear entre duas variáveis",
                "D) A probabilidade conjunta entre duas variáveis"
            ],
            "resposta": "C"
        }
    ]
    
    print("\n--- Quiz: Estatística em IA ---")
    pontuacao = 0

    for q in perguntas:
        print("\n" + q["pergunta"])
        for opcao in q["opcoes"]:
            print(opcao)
        resposta_usuario = input("Sua resposta (A, B, C ou D): ").strip().upper()
        
        if resposta_usuario == q["resposta"]:
            print("✅ Correto!")
            pontuacao += 1
        else:
            print(f"❌ Incorreto. A resposta certa é: {q['resposta']}")
    
    print(f"\n📊 Resultado final: {pontuacao} de {len(perguntas)} acertos.")
    input("\nPressione Enter para voltar ao menu.")

# MENU PRINCIPAL
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
        print("\nQuiz de Machine Learning em desenvolvimento...")
    elif opcao == "4":
        print("\nPDF da pesquisa sobre IA ainda não implementado.")
    else:
        print("Opção inválida. Tente novamente.")
