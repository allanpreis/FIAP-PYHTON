nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo um número para saber se ele está entre 0 e 30 ou entre 40 e 79\n')

n1 = float(input('Insira um número: '))
if n1 >= 0.0 and n1 <= 30.0:
    print('\nO número {} está compreendido entre 0 e 30'.format(n1))
elif  n1 >= 40.0 and n1 <= 79.0:
    print('\nO número {} está compreendido entre 40 e 79'.format(n1))
else:
    print('\nNúmero {} está fora dos limites'.format(n1))