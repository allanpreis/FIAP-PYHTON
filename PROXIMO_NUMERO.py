nome = input('Insira seu nome: ')
print('Olá {}.\n'.format(nome), end='')
print('Informe abaixo um número para o programa lhe mostrar os 10 números adiantes dele')

contador = 0
n1 = int(input('\nInsira um número: '))
while (contador <= 9):
    n1 = n1 + 1
    print(n1)
    contador = contador+1

print('Acabou')
