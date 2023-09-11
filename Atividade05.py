tarefas = []
while True:
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

    print("\nOpções:")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Remover tarefa")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
    elif escolha == "2":
        if tarefas:
            indice = int(input("Digite o número da tarefa concluída: "))
            if 1 <= indice <= len(tarefas):
                tarefas.pop(indice - 1)
            else:
                print("Número de tarefa inválido.")
        else:
            print("A lista de tarefas está vazia.")
    elif escolha == "3":
        if tarefas:
            indice = int(input("Digite o número da tarefa a ser removida: "))
            if 1 <= indice <= len(tarefas):
                tarefas.pop(indice - 1)
            else:
                print("Número de tarefa inválido.")
        else:
            print("A lista de tarefas está vazia.")
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
