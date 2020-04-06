nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}.\n'.format(nome), end='')
print('Informe abaixo um número inteiro para que o programa possa lhe dizer se esse número é ímpar ou par\n')

n1 = int(input('Número: '))
resultado = n1 % 2
if resultado == 0:
    print('\nO número {} é PAR!'.format(n1))
else:
    print('\nO número {} é ÍMPAR!'.format(n1))
