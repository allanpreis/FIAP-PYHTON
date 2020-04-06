nome = input('Insira seu nome: ')
print('Olá, {}. \n'.format(nome), 'Insira abaixo a cotação atual do dolar e sua quantia em real, assim poderá saber quanto dolares você pode adquirir\n')

n1 = float(input('Cotação atual do Dolar : '))
n2 = float(input('Quanto você tem na carteira R$'))

print('\nVocê pode adquirir um total de US${}'.format(n1*n2))