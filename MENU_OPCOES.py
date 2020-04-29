nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo a operação que deseja\n')

opcao = 0
while opcao !=3:
    print('-' * 30)
    print('''    [1] Somar dois números 
    [2] Raiz quadrada
    [3] Sair do programa''')
    print('-' * 30)
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        n1 = float(input('\nPrimeiro número: '))
        n2 = float(input('Segundo número: '))
        n3 = n1 + n2
        print('\n{} + {} = {}'.format(n1, n2, n3))
        break
    elif opcao == 2:
        n1 = int(input('\nInsira um número: '))
        print('A raiz quadrada de {} é {}'.format(n1 , n1**2))
        break
    elif opcao == 3:
        print('\nSaindo do programa...')

    else:
        print('\n\033[31mVocê escolheu uma opção inválida!!!\033[m')
print('\nFim do programa')

