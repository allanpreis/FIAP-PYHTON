nome = input('Insira seu nome:')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo dois números inteiros, para saber qual o maior entre eles\n')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    maior = n1
else:
    maior = n2

print('\nO maior número é {}'.format(maior))