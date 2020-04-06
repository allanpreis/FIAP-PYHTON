nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}.\n'.format(nome), end='')
print('Informe abaixo dois número inteiros e o programa lhe dirá se o primeiro número é divisível pelo segundo número\n')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
resultado = n1 % n2
if resultado == 0:
    print('\n{} é divisível por {}'.format(n1, n2))
else:
    print('\n{} não é divisível por {}'.format(n1, n2))
