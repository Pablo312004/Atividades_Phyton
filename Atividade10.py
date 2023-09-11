import json

def salvar_agenda(agenda):
    with open("agenda.json", "w") as arquivo:
        json.dump(agenda, arquivo)

def carregar_agenda():
    try:
        with open("agenda.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

agenda = carregar_agenda()

while True:
    print("\nAgenda Telefônica")
    print("1. Adicionar contato")
    print("2. Pesquisar contato")
    print("3. Editar contato")
    print("4. Excluir contato")
    print("5. Listar todos os contatos")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        salvar_agenda(agenda)
        print(f"Contato '{nome}' adicionado.")
    elif escolha == "2":
        nome = input("Digite o nome do contato a ser pesquisado: ")
        telefone = agenda.get(nome)
        if telefone:
            print(f"Telefone de '{nome}': {telefone}")
        else:
            print(f"Contato '{nome}' não encontrado.")
    elif escolha == "3":
        nome = input("Digite o nome do contato a ser editado: ")
        if nome in agenda:
            novo_telefone = input(f"Digite o novo telefone para '{nome}': ")
            agenda[nome] = novo_telefone
            salvar_agenda(agenda)
            print(f"Telefone de '{nome}' atualizado.")
        else:
            print(f"Contato '{nome}' não encontrado.")
    elif escolha == "4":
        nome = input("Digite o nome do contato a ser excluído: ")
        if nome in agenda:
            del agenda[nome]
            salvar_agenda(agenda)
            print(f"Contato '{nome}' excluído.")
        else:
            print(f"Contato '{nome}' não encontrado.")
    elif escolha == "5":
        print("\nLista de Contatos:")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    elif escolha == "6":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")