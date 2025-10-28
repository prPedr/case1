while True:
    opcao = input("Adicione uma tarefa ou digite 'sair' para finalizar: ")

    if opcao.lower() == "sair":
        break
    tarefa = opcao

    print(f"Nova tarefa adicionada: {tarefa}")

print(f"Ultima tarefa adicionada: {tarefa}")