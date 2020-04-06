nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}.\n'.format(nome), end='')
print('Informe abaixo um número inteiro e ver se esse número é múltiplo de 5 e 10\n')

n1 = int(input('Insira um número: '))
if n1 % 5 == 0 and n1 % 10 == 0:
    print('{} é multiplo de 5 e 10'.format(n1))
else:
    print('{} não é multiplo de 5 e 10'.format(n1))

