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
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa adicionada {tarefa}")
  elif escolha == "2":
    for tarefa in tarefas:
      print(f"- {tarefa}")
  elif escolha == "3":
    remover = input("Digite a tarefa que deseja remover: ")
    if remover in tarefas:
      tarefas.remove(remover)
      print(f"Tarefa removida {remover}")
    else:
      print("Tarefa nao encontrada")
  elif escolha == "4":
      print("Saindo...")
      break
  else:
    print("Opcao invalida")