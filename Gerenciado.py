import time

adicionar_tarefa = []

while True:
    opcoes = 1, 2, 3, 4, 5
    print('=-' * 20)
    print(f'\033[36m{"GERENCIADOR DE TAREFAS":^48}\033[m')
    print('=-' * 20)
    print('\033[34m[ 1 ]\033[m Adicionar tarefa\n'
          '\033[34m[ 2 ]\033[m Lista de tarefas\n'
          '\033[34m[ 3 ]\033[m Remover tarefa\n'
          '\033[34m[ 4 ]\033[m Limpar lista\n'
          '\033[34m[ 5 ]\033[m Sair')
    opcao = int(input('Opção:'))
    while opcao not in opcoes:
        print('\033[31mTENTE NOVAMENTE!\033[m')
        time.sleep(0.5)
        opcao = int(input('Opção:'))

    if opcao == 1:
        while True:
            adicionar_nova_tarefa = str(input('Adicione alguma tarefa:'))
            adicionar_tarefa.append(adicionar_nova_tarefa)
            time.sleep(0.1)
            print('\033[32mTAREFA ADICIONADA <3\033[m')
            time.sleep(0.6)
            continuar = str(input('Deseja continuar adicionando tarefas? [S/N]')).upper().strip()[0]
            while continuar not in 'SN':
                continuar = str(input('\033[31mTENTE NOVAMENTE!\033[m\n'
                                      'Deseja continuar adicionando tarefas? [S/N]')).upper().strip()[0]
            if continuar == 'N':
                break

    elif opcao == 2:
        if not adicionar_tarefa:
            print('\033[31mLISTA VAZIA\033[m')
            time.sleep(1)
        else:
            while True:
                print('=-' * 20)
                print(f'\033[36m{"LISTA DE TAREFAS":^40}\033[m')
                print('=-' * 20)
                for c in range(len(adicionar_tarefa)):
                    print(f'Tarefa {c + 1}: {adicionar_tarefa[0 + c].capitalize()}')
                continuar = str(input('Deseja sair da lista? [S/N]')).upper().strip()[0]
                while continuar not in 'SN':
                    continuar = str(input('\033[31mTENTE NOVAMENTE!\033[m\n'
                                          'Deseja sair? [S/N ]')).upper().strip()[0]
                if continuar == 'S':
                    break

    elif opcao == 3:
        while True:
            if not adicionar_tarefa:
                print('\033[31mLISTA VAZIA\033[m')
                time.sleep(1)
                break
            else:
                print('=-' * 18)
                print(f'\033[36m{"REMOVER TAREFAS":^40}\033[m')
                print('=-' * 17)
                for c in range(len(adicionar_tarefa)):
                    print(f'\033[34mTarefa [ {c + 1} ]:\033[m {adicionar_tarefa[c].capitalize()}')
                remover = int(input('Qual tarefa você quer remover?'))
                remover = remover - 1
                while remover not in range(len(adicionar_tarefa)):
                    print('__' * 20)
                    print('\033[31mTAREFA NÃO ENCONTRADA\033[m')
                    time.sleep(1)
                    print('=-' * 18)
                    print(f'\033[36m{"REMOVER TAREFAS":^40}\033[m')
                    print('=-' * 18)
                    for c in range(len(adicionar_tarefa)):
                        print(f'\033[34mTarefa [ {c + 1} ]:\033[m {adicionar_tarefa[c].capitalize()}')
                    remover = int(input('Qual tarefa você quer remover?'))
                    remover = remover - 1
                print(f'\033[31mTAREFA {adicionar_tarefa[remover].upper()} REMOVIDA \033[m')
                adicionar_tarefa.pop(remover)
                continuar = str(input('Deseja continuar removendo [S/N]')).upper().strip()[0]
                while continuar not in 'SN':
                    continuar = str(input('\033[31mTENTE NOVAMENTE!\033[m\n'
                                          'Deseja continuar removendo [S/N]')).upper().strip()[0]
                if continuar == 'N':
                    if not adicionar_tarefa:
                        print('\033[31mLISTA VAZIA\033[m')
                        time.sleep(1)
                        break
                    else:
                        break
    elif opcao == 4:
        while True:
            if not adicionar_tarefa:
                print('\033[31mLISTA VAZIA\033[m')
                time.sleep(1)
                break
            else:
                adicionar_tarefa = []
                break
    elif opcao == 5:
        print('\033[35m__' * 20)
        print('Obrigado por usar o nosso gerenciador <3')
        print('__' * 20)
        break