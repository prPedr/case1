tarefas = []

while True:
  print("|----------------------|")
  print("|    Menu de opcoes    |")
  print("|----------------------|")
  print("| 1 - Adicionar tarefa |")
  print("| 2 - Listar tarefas   |")
  print("| 3 - Remover tarefas  |")
  print("| 4 - Sair             |")
  print("|----------------------|")

  print()

  escolha = input("Escolha uma opcao: ")

  if escolha == "1":
    nome = input("Digite o nome da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa (Alta, Media, Baixa): ")

    tarefa = {
      "nome": nome,
      "prioridade": prioridade
    }

    tarefas.append(nome)
    print(f"Tarefa {nome} com prioridade {prioridade} adicionada")

  elif escolha == "2":
    for tarefa in tarefas:
      print(f"- {tarefa[nome]} (Prioridade: {tarefa[prioridade]})")

  elif escolha == "3":
    remover = input("Digite o nome da tarefa que deseja remover: ")
    for tarefa in tarefas:
      if tarefa["nome"] == remover:
        tarefas.remove(remover)
        print(f"Tarefa removida: {remover}")
        break
    else:
      print("Tarefa nao encontrada")

  elif escolha == "4":
      print("Saindo...")
      break
  else:
    print("Opcao invalida")