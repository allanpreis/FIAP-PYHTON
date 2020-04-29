nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo a operação que deseja\n')

opcao = 0
while opcao !=11:
    print('-' * 30)
    print('''    [1] Tabuada do 1 
    [2] Tabuada do 2
    [3] Tabuada do 3
    [4] Tabuada do 4
    [5] Tabuada do 5
    [6] Tabuada do 6
    [7] Tabuada do 7
    [8] Tabuada do 8
    [9] Tabuada do 9
    [10] Tabuada do 10
    [11] Sair do programa''')
    print('-' * 30)
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        multiplicador = 0
        tabuada = 1
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 2:
        multiplicador = 0
        tabuada = 2
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 3:
        multiplicador = 0
        tabuada = 3
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 4:
        multiplicador = 0
        tabuada = 4
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 5:
        multiplicador = 0
        tabuada = 5
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 6:
        multiplicador = 0
        tabuada = 6
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 7:
        multiplicador = 0
        tabuada = 7
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 8:
        multiplicador = 0
        tabuada = 8
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 9:
        multiplicador = 0
        tabuada = 9
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 10:
        multiplicador = 0
        tabuada = 10
        while (multiplicador <= 10):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        break
    elif opcao == 11:
        print('\nSaindo do programa...')

    else:
        print('\nVocê escolheu uma opção inválida!!!')

print('\nFim do programa')
