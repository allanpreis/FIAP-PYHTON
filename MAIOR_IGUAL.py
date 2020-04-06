nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}.\n'.format(nome), end='')
print('Informe abaixo dois número reais e o programa dirá se sua soma é maior que 10 ou menor igual\n')

n1 = int(input('Insira um número: '))
n2 = int(input('Insira o segundo número: '))
resultado = n1 + n2
if resultado > 10:
    print('\nNúmero maior que 10')
elif resultado <= 10 :
    print('\nNúmero menor ou igual a 10')