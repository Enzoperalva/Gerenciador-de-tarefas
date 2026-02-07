# Gerenciador-de-tarefas
Trio gerenciamento

while True:
    print(" GERENCIADOR DE TAREFAS ")
    print("1 → Adicionar uma tarefa")
    print("2 → Listar uma tarefas")
    print("3 → Remover uma tarefa")
    print("4 → Limpar lista")
    print("5 → Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nova_tarefa = input("Digite a tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        print("\nSUA LISTA DE TAREFAS:")
        if not tarefas:
            print("A lista está vazia.")
        else:
            for i in range(len(tarefas)):
                print(f"{i + 1}. {tarefas[i]}")

    elif opcao == "3":
        if not tarefas:
            print("Não há nada para remover.")
        else:
            try:
                indice = int(input("Digite o número da tarefa para remover: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "4":
        tarefas.clear()
        print("Lista limpa!")

    elif opcao == "5":
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida, tente novamente.") 
