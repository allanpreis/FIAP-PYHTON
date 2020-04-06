nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo o valor do produto para saber o valor de venda\n')

n1 = float(input('Valor do Produto: R$'))
if n1 < 20:
    n2 = n1 * 30 /100
    n3 = n1 + n2
    print('\nO valor de venda será R${}'.format(n3))
else:
    n2 = n1 * 45 / 100
    n3 = n1 + n2
    print('\nO valor de venda será R${}'.format(n3))
