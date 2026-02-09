import time

adicionar_tarefa= []
i=0

while True:
    opcoes= 1,2,3,4,5
    print('=-'*20)
    print(f'{"\033[36mGERENCIADOR DE TAREFAS\033[m":^48}')
    print('=-' * 20)
    print('\033[34m[ 1 ]\033[m Adicionar tarefa\n'
          '\033[34m[ 2 ]\033[m Lista de tarefas\n'
          '\033[34m[ 3 ]\033[m Remover tarefa\n'
          '\033[34m[ 4 ]\033[m Limpar lista\n'
          '\033[34m[ 5 ]\033[m Sair')
    opcao= int(input('Opção:'))
    while opcao not in opcoes:
        time.sleep(0.5)
        opcao = int(input('\033[31mTENTE NOVAMENTE!\033[m\n'
                          'Opção:'))

    if opcao == 1:
        while True:
            adicionar_nova_tarefa= str(input('Adicione alguma tarefa:'))
            adicionar_tarefa.append(adicionar_nova_tarefa)
            time.sleep(0.3)
            print('\033[32mTAREFA ADICIONADA <3\033[m')
            time.sleep(0.6)
            continuar= str(input('Deseja continuar adicionando tarefas? [S/N]')).upper().strip()[0]
            while continuar not in 'SN':
                continuar= str(input('\033[31mTENTE NOVAMENTE!\033[m\n'
                              'Deseja continuar adicionando tarefas? [S/N]')).upper().strip()[0]
            if continuar == 'N':
                break

    elif opcao == 2:
        if not adicionar_tarefa:
            print('\033[31mLISTA VAZIA\033[m')
            time.sleep(1)
        else:
            while True:
                print('=-'*20)
                print(f'{"\033[36mLISTA DE TAREFAS\033[m":^40}')
                print('=-'*20)
                for c in range(len(adicionar_tarefa)):
                    print(f'Tarefa {c+1}: {adicionar_tarefa[0+c].capitalize()}')
                continuar= str(input('Deseja sair? [ S ]')).upper().strip()[0]
                while continuar not in 'S':
                    continuar= str(input('\033[31mTENTE NOVAMENTE!\033[m\n'
                                  'Deseja sair? [ S ]')).upper().strip()[0]
                if continuar == 'S':
                    break


    elif opcao == 3:
        while True:
            if not adicionar_tarefa:
                print('\033[31mLISTA VAZIA\033[m')
                time.sleep(1)
                break
            else:
                print('=-' * 20)
                print(f'{"\033[36mREMOVER TAREFAS\033[m":^40}')
                print('=-' * 20)
                for c in range(len(adicionar_tarefa)):
                    print(f'[ {c} ] {adicionar_tarefa[0 + c].capitalize()}')
                remover= int(input('Qual tarefa você quer remover?'))
                print(f'\033[31mTAREFA {adicionar_tarefa[remover].upper()} REMOVIDA \033[m')
                adicionar_tarefa.pop(remover)
                continuar = str(input('Deseja sair? [ S ]')).upper().strip()[0]
                while continuar not in 'S':
                    continuar = str(input('\033[31mTENTE NOVAMENTE!\033[m\n'
                                          'Deseja sair? [ S ]')).upper().strip()[0]
                if continuar == 'S':
                    break
    elif opcao == 4:
        while True:
            if not adicionar_tarefa:
                print('\033[31mLISTA VAZIA\033[m')
                time.sleep(1)
                break
            else:
                for c in range(len(adicionar_tarefa)):
                    adicionar_tarefa.pop()
                print('\033[31mLISTA APAGADA\033[m')
                time.sleep(1)
                break
    elif opcao == 5:
        print('\033[35m__'*20)
        print('Obrigado por usar o nosso gerenciador <3')
        print('__' * 20)
        break