nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}.\n'.format(nome), end='')
print('Informe abaixo dois número inteiros e o programa lhe dirá se esses números são iguais ou diferentes\n')

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
if n1 == n2:
    print('\nOs dois números são iguais')
elif n1 != n2:
    print('\nOs dois números são diferentes')