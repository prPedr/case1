tarefas = []

def adicionar_tarfa(adicionar_tarefa, adicionar_prioridade):
    tarefa = {
        "tarefa": adicionar_tarefa,
        "prioridade": adicionar_prioridade
    }

    tarefas.append(tarefa)
    print(f"Tarefa '{adicionar_tarefa}' com prioridade '{adicionar_prioridade}' adicionada com sucesso!")

def listar_tarefas():
    print("Lista de tarefas:")
    for tarefa in tarefas:
        print(f"- {tarefa['tarefa']} (Prioridade: {tarefa['prioridade']})")
        
def excluir_tarefa(remover_tarefa):
    for tarefa in tarefas:
        if tarefa["tarefa"] == remover_tarefa:
            tarefas.remove(tarefa)
            print(f"Tarefa '{remover_tarefa}' removida com sucesso!")
            break

while True:
    print("|---- Menu de Opções ----|")
    print("| 1 - Adicionar tarefa   |")
    print("| 2 - Listar tarefas     |")
    print("| 3 - Remover tarefa     |")
    print("| 4 - Sair               |")
    print("|------------------------|")

    opcao = input("Escolha uma opcão: ")
    if opcao == "1":
        adicionar_tarefa = input("Digite a tarefa que deseja adicionar: ")
        adicionar_prioridade = input("Digite a prioridade da tarefa (Alta, Média, Baixa): ")
        
        adicionar_tarfa(adicionar_tarefa, adicionar_prioridade)

    elif opcao == "2":
        listar_tarefas()
    
    elif opcao == "3":
        remover_tarefa = input("Digite a tarefa que deseja remover: ")
        excluir_tarefa(remover_tarefa)

    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")