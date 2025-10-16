import os

# Caminho do PDF para abrir com a opção 1 do menu
caminho_pdf = "C:/Users/sebastian.8908/Documents/Codigos uc2 Python Petterson, John/Codigo uc2 Python John/projeto_menu/projeto_pdf_menu.pdf"
caminho_projeto= "C:/Users/sebastian.8908/Documents/Codigos uc2 Python Petterson, John/Codigo uc2 Python John/projeto_menu/Inteligencia_Artificial_no_Games.pdf"

def quiz_estatistica_ia():
    perguntas = [
        {"pergunta": "Qual medida representa a média dos quadrados dos desvios?",
         "opcoes": ["A) Variância", "B) Desvio padrão", "C) Moda", "D) Mediana"],
         "correta": "A"},
        {"pergunta": "Distribuição mais usada para modelar eventos raros:",
         "opcoes": ["A) Normal", "B) Poisson", "C) Binomial", "D) Uniforme"],
         "correta": "B"},
        {"pergunta": "O valor que divide a amostra ao meio é chamado de:",
         "opcoes": ["A) Média", "B) Mediana", "C) Moda", "D) Variância"],
         "correta": "B"},
        {"pergunta": "Se todos os valores têm a mesma probabilidade de ocorrer, temos a distribuição:",
         "opcoes": ["A) Normal", "B) Uniforme", "C) Binomial", "D) Poisson"],
         "correta": "B"},
        {"pergunta": "O desvio padrão mede:",
         "opcoes": ["A) Tendência central", "B) Grau de dispersão", "C) Probabilidade", "D) Frequência"],
         "correta": "B"},
        {"pergunta": "Qual destas NÃO é uma medida de tendência central?",
         "opcoes": ["A) Média", "B) Moda", "C) Variância", "D) Mediana"],
         "correta": "C"},
        {"pergunta": "Em um histograma, a área total representa:",
         "opcoes": ["A) Média", "B) Frequência total", "C) Probabilidade total", "D) Mediana"],
         "correta": "C"},
        {"pergunta": "Quando a média é maior que a mediana, a distribuição tende a ser:",
         "opcoes": ["A) Simétrica", "B) Assimétrica à esquerda", "C) Assimétrica à direita", "D) Normal"],
         "correta": "C"},
        {"pergunta": "O Teorema Central do Limite afirma que:",
         "opcoes": ["A) Toda variável é normal", "B) Médias amostrais tendem à normalidade", "C) A variância é sempre constante", "D) A moda é igual à mediana"],
         "correta": "B"},
        {"pergunta": "Probabilidade de evento impossível é:",
         "opcoes": ["A) 1", "B) 0", "C) 0,5", "D) Depende da amostra"],
         "correta": "B"}
    ]

    print("\nQuiz: Estatística em IA")
    pontuacao = 0

    for q in perguntas:
        print("\n" + q["pergunta"])
        for opcao in q["opcoes"]:
            print(opcao)
        resposta_usuario = input("Sua resposta (A, B, C ou D): ").strip().upper()

        if resposta_usuario == q["correta"]:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto. A resposta certa é: {q['correta']}")

    print(f"\nResultado Final: {pontuacao} de {len(perguntas)} acertos.")
    input("\nPressione Enter para voltar ao menu")


def quiz_machine_learning():
    perguntas = [
        {"pergunta": "O que é overfitting?",
         "opcoes": ["A) Modelo que generaliza bem", "B) Modelo que aprende ruído do treino", "C) Modelo que não aprende nada", "D) Nenhuma das anteriores"],
         "correta": "B"},
        {"pergunta": "Qual algoritmo é usado em classificação?",
         "opcoes": ["A) KNN", "B) Regressão Linear", "C) PCA", "D) K-means"],
         "correta": "A"},
        {"pergunta": "O que significa 'supervisionado' em Machine Learning?",
         "opcoes": ["A) Sem rótulos", "B) Com rótulos", "C) Autoaprendizado", "D) Nenhuma das anteriores"],
         "correta": "B"},
        {"pergunta": "Qual técnica reduz dimensionalidade?",
         "opcoes": ["A) SVM", "B) PCA", "C) Regressão logística", "D) Árvore de decisão"],
         "correta": "B"},
        {"pergunta": "Na regressão linear, o erro é medido pela:",
         "opcoes": ["A) Soma dos quadrados dos resíduos", "B) Moda", "C) Desvio padrão", "D) Acurácia"],
         "correta": "A"},
        {"pergunta": "O que é regularização?",
         "opcoes": ["A) Técnica para aumentar overfitting", "B) Reduz complexidade do modelo", "C) Melhorar gráficos", "D) Aumentar dimensionalidade"],
         "correta": "B"},
        {"pergunta": "Qual destes é um algoritmo NÃO supervisionado?",
         "opcoes": ["A) Regressão logística", "B) SVM", "C) K-means", "D) Random Forest"],
         "correta": "C"},
        {"pergunta": "O que significa 'feature' em Machine Learning?",
         "opcoes": ["A) O alvo a ser previsto", "B) Uma variável de entrada", "C) O erro do modelo", "D) O parâmetro de ajuste"],
         "correta": "B"},
        {"pergunta": "Qual métrica é usada em classificação binária?",
         "opcoes": ["A) Acurácia", "B) R²", "C) Erro quadrático médio", "D) Nenhuma das anteriores"],
         "correta": "A"},
        {"pergunta": "Em redes neurais, a função que introduz não-linearidade é chamada de:",
         "opcoes": ["A) Função de ativação", "B) Função de perda", "C) Função de custo", "D) Função de otimização"],
         "correta": "A"}
    ]

    print("\nQuiz: Machine Learning")
    pontuacao = 0

    for q in perguntas:
        print("\n" + q["pergunta"])
        for opcao in q["opcoes"]:
            print(opcao)
        resposta_usuario = input("Sua resposta (A, B, C ou D): ").strip().upper()

        if resposta_usuario == q["correta"]:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto. A resposta certa é: {q['correta']}")

    print(f"\nResultado Final: {pontuacao} de {len(perguntas)} acertos.")
    input("\nPressione Enter para voltar ao menu")


while True:
    print("\n==============================")
    print("MENU PRINCIPAL")
    print("==============================")
    print("1. Exercícios resolvidos de Estatística (PDF)")
    print("2. Quiz: Estatística em IA")
    print("3. Quiz: Machine Learning")
    print("4. Pesquisa sobre uso de IA (PDF)")
    print("0. Sair")
    print("==============================")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "0":
        print("\nVolte sempre!")
        break
    elif opcao == "1":
        if os.path.exists(caminho_pdf):
            os.startfile(caminho_pdf)
        else:
            print("\nArquivo PDF não encontrado.")
    elif opcao == "2":
        quiz_estatistica_ia()
    elif opcao == "3":
        quiz_machine_learning()
    elif opcao == "4":
        if os.path.exists(caminho_projeto):
            os.startfile(caminho_projeto)
    else:
        print("\nOpção inválida. Tente novamente.")
