nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}'.format(nome), end='')
print('\nInforme abaixo o preço unitário do produto, o pais de origem, o meio transporte e se a carga é perigosa para envio, para que possa ter seu preço final')

preco = float(input('\nPreço Unitário: R$'))
pais = 0
while pais !=3:
    print('-' * 30)
    print('''        [1] Brasil 🇧🇷
        [2] México 🇲🇽
        [3] Outros 🗺''')
    print('-' * 30)
    pais = int(input('Qual o País de Origem? '))
    if pais == 1:
        transporte = 0
        while transporte !=3:
            print('-' * 30)
            print('''        [T] Terrestre 🚛
        [F] Fluvial ⛴
        [A] Aéreo ✈''')
            print('-' * 30)
            transporte = (input('Qual o Meio de Transporte? '))
            if transporte == 'T':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5/100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20/100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digita incorreto, por favor informe [S/N] com letras maiúsculas')
            elif transporte == 'F':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 21.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digitado está incorreto, por favor informe [S/N] com letras maiúsculas')
            elif transporte == 'A':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 21.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 21.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 21.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 21.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digitado está incorreto, por favor informe [S/N] com letras maiúsculas')
    elif pais == 2:
        transporte = 0
        while transporte != 3:
            print('-' * 30)
            print('''        [T] Terrestre 🚛
        [F] Fluvial ⛴
        [A] Aéreo ✈''')
            print('-' * 30)
            transporte = (input('Qual o Meio de Transporte? '))
            if transporte == 'T':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 27.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 27.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 25.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 25.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digita incorreto, por favor informe [S/N] com letras maiúsculas')
            elif transporte == 'F':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 27.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 27.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 25.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 25.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digitado está incorreto, por favor informe [S/N] com letras maiúsculas')
            elif transporte == 'A':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 27.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 27.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 25.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 25.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digitado está incorreto, por favor informe [S/N] com letras maiúsculas')
    elif pais == 3:
        transporte = 0
        while transporte != 3:
            print('-' * 30)
            print('''        [T] Terrestre 🚛
        [F] Fluvial ⛴
        [A] Aéreo ✈''')
            print('-' * 30)
            pais = (input('Qual o Meio de Transporte? '))
            if transporte == 'T':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 50.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 50.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 40.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 40.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digita incorreto, por favor informe [S/N] com letras maiúsculas')
            elif transporte == 'F':
                carga = input('\nA carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 50.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 50.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 40.00 + 0
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 40.00 + 0
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digitado está incorreto, por favor informe [S/N] com letras maiúsculas')
            elif transporte == 'A':
                carga = input('A carga é perigosa? [S/N] ')
                if (carga == 'S'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 50.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 50.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                elif (carga == 'N'):
                    if (preco <= 100.00):
                        imposto = preco * 5 / 100
                        pf = preco + imposto + 40.00 + (preco / 2)
                        print('\nO preço final é R${:.2f}'.format(pf))
                    else:
                        imposto = preco * 20 / 100
                        pf = preco + imposto + 40.00 + (preco / 2)
                        print('\nO preço final é R${:2f}'.format(pf))
                else:
                    print('\nValor digitado está incorreto, por favor informe [S/N] com letras maiúsculas')
