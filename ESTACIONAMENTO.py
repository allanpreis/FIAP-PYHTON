from time import sleep
nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo qual o seu veículo e quanto tempo ficou estacionado, para saber quanto deve pagar\n')

opcao = 0
while opcao !=3:
    print('-' * 36)
    print('''        [1] Moto 🏍
        [2] Carro 🚗
        [3] Sair do programa''')
    print('-' * 36)
    opcao = int(input('Qual o seu veículo? '))
    if opcao == 1:
        print("\nAtenção usuário por favor informe o tempo de permanência do veiculo em minutos")
        t1 = int(input('\nQuanto tempo sua moto ficou estacionado? '))
        if t1 <= 15:
            print('\nPor esse período de tempo o valor é grátis')
        elif t1 >= 16 and t1 <= 180:
            print('\nVocê irá pagar R$17,00 pelo tempo estacionado')
        elif t1 > 180:
            t2 = (t1 - 180) * 0.10
            t3 = 17 + t2
            print('\nVocê irá pagar R${:.2f} pelo tempo estacionado'.format(t3))

    elif opcao == 2:
        print('\nAtenção usuário por favor informe o tempo de permanência do veiculo em minutos')
        t1 = int(input('\nQuanto tempo seu carro ficou estacionado? '))
        if t1 <= 15:
            print('\nPor esse período de tempo o valor é grátis')
        elif t1 >=16 and t1 <= 180:
            print('\nVocê irá pagar R$20 pelo tempo estacionado')
        elif t1 > 180:
            t2 = (t1 - 180) * 0.15
            t3 = 20 + t2
            print('\nVocê irá pagar R${:.2f} pelo tempo estacionado'.format(t3))


    elif opcao == 3:
        print('\nSaindo do programa...')
    else:
        print('\nVocê escolheu uma opção inválida!!!')
    sleep(2)
print('=' * 80)
print(' ESTACIONAMENTO SEMPRE BEM-VINDO AGRADECE POR USAR NOSSOS SERVIÇO, VOLTE SEMPRE ')
print('=' * 80)