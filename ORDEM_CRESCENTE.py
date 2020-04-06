nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo 3 números diferentes para que o programa o coloque em ordem crescente\n')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 < n2 and n1 < n3:
    print('\nA ordem ficará {},'.format(n1), end='')
    if n2 < n3:
        print(' {}, '.format(n2), end='')
        print('{} '.format(n3))
    else:
        print(' {}, '.format(n3), end='')
        print('{} '.format(n2))
elif n2 < n1 and n2 < n3:
    print('\nA ordem ficará {},'.format(n2), end='')
    if n1 < n3:
        print(' {}, '.format(n1), end='')
        print('{} '.format(n3))
    else:
        print(' {}, '.format(n3), end='')
        print('{} '.format(n1))
elif n3 < n1 and n3 < n2:
    print('\nA ordem ficará {},'.format(n3), end='')
    if n1 < n2:
        print(' {}, '.format(n1), end='')
        print('{} '.format(n2))
    else:
        print(' {}, '.format(n2), end='')
        print('{} '.format(n1))
elif n1 == n2 and n1 == n3:
    print('\nOs três números digitados são iguais')
