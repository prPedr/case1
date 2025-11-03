import json

tarefas = []

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo) # Salva a lista de tarefas em um arquivo JSON
    print("Tarefas salvas com sucesso.")

def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo) # Carrega a lista de tarefas do arquivo JSON
        print("Tarefas carregadas com sucesso.")
        return tarefas
    except:
        print("Nenhum arquivo de tarefas encontrado. Iniciando com uma lista vazia.")
        return []

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

tarefa = carregar_tarefas()

while True:
    print("=== Menu de Tarefas ===")
    print("| 1. Adicionar Tarefa |")
    print("| 2. Listar Tarefas   |")
    print("| 3. Remover Tarefa   |")
    print("| 4. Salvar Tarefas   |")
    print("| 5. Sair             |")
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
            salvar_tarefas()
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")