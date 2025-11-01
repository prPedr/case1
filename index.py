tarefas = []

def adicionar_tarefa():
    try:
        input_adicionar_tarefa = input("Informe a tarefa que deseja adicionar: ")
        input_adicionar_prioridade = input("Informe a prioridade da tarefa: ")

        tarefa = {
            "tarefa": input_adicionar_tarefa,
            "prioridade": input_adicionar_prioridade
        }

        tarefas.append(tarefa)
        print(f"Tarefa '{input_adicionar_tarefa}' com prioridade '{input_adicionar_prioridade}' adicionada.")
    except:
        print("Erro ao adicionar a tarefa. Tente novamente.")

def listar_tarefas():
    try:
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("=== Lista de Tarefas ===")
            for tarefa in tarefas:
                print(f"Tarefa: {tarefa["tarefa"]} - Prioridade: {tarefa["prioridade"]}")
    except:
        print("Erro ao listar as tarefas. Tente novamente.")

def remover_tarefa():
    try:
        input_remover_tarefa = input("Informe a tarefa que deseja remover: ")
        tarefa_encontrada = False

        for tarefa in tarefas:
            if tarefa["tarefa"] == input_remover_tarefa:
                tarefas.remove(tarefa)
                tarefa_encontrada = True
                print(f"Tarefa '{input_remover_tarefa}' removida.")
                break

        if not tarefa_encontrada:
            print(f"Tarefa '{input_remover_tarefa}' não encontrada.")
    except:
        print("Erro ao remover a tarefa. Tente novamente.")

while True:
    print("=== Menu de Tarefas ===")
    print("| 1. Adicionar Tarefa |")
    print("| 2. Listar Tarefas   |")
    print("| 3. Remover Tarefa   |")
    print("| 4. Sair             |")
    print("=======================\n")
    
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            remover_tarefa()
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")