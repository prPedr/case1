tarefas = []

while True:
    print("|---- Menu de Opções ----|")
    print("| 1 - Adicionar tarefa   |")
    print("| 2 - Remover tarefa     |")
    print("| 3 - Ver tarefas        |")
    print("| 4 - Sair               |")
    print("|------------------------|")

    opcao = input("Escolha uma opcão: ")
    if opcao == "1":
        adicionar_tarefa = input("Digite a tarefa que deseja adicionar: ")
        adicionar_prioridade = input("Digite a prioridade da tarefa (Alta, Média, Baixa): ")
        
        tarefa = {
            "tarefa": adicionar_tarefa,
            "prioridade": adicionar_prioridade
        }

        tarefas.append(tarefa)
        print(f"Tarefa '{adicionar_tarefa}' com prioridade '{adicionar_prioridade}' adicionada com sucesso!")

    elif opcao == "2":
        print("Lista de tarefas:")
        for tarefa in tarefas:
            print(f"- {tarefa['tarefa']} (Prioridade: {tarefa['prioridade']})")
    
    elif opcao == "3":
        remover_tarefa = input("Digite a tarefa que deseja remover: ")
        for tarefa in tarefas:
            if tarefa["tarefa"] == remover_tarefa:
                tarefas.remove(tarefa)
                print(f"Tarefa '{remover_tarefa}' removida com sucesso!")
                break

    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")