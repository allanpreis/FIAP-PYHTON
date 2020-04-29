nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo 3 valores para saber que tipo de triângulo esses valores formam\n')

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\nEsses valores formam um triângulo ', end='')
    if n1 == n2 == n3:
        print('equilátero!')
    elif n1 != n2 != n3 != n1:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('\n\033[31mOs valores inseridos não formam um triângulo!\033[m')

