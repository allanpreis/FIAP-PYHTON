nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}.\n'.format(nome), end='')
print('Informe abaixo 3 números inteiros e o programa lhe dirá se está em ordem crescente\n')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))


if n1 < n2 and n2 < n3:
    print('\nOs números foram digitados em ordem crescente')
else:
    print('\nOs números não foram digitados em ordem crescente')

