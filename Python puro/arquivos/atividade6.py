#criar uma função que permita ao usuário adicionar entradas em um arquivo de diário diario.txt. Cada entrada deve contera data e uma descrição, armazenadas como dicionário antes de serem escritas no arquivo.


def adicionar_entrada_diario():
    try:
        data = input("Digite a data (ex: 05/06/2025): ").strip()
        descricao = input("Digite uma anotação do dia: ").strip()
    
        entrada = {
            "Data":data,
            "Descrição":descricao
        }
    
        with open("arquivos/diario.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{entrada}\n")
        
        print("Entrada adicionada com sucesso!")
        
    except KeyboardInterrupt:
        print("\nEntrada cancelada")
        
adicionar_entrada_diario()