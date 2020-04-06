nome = input('Insira seu nome:')
print('Olá, {}. \n'.format(nome),'Insira abaixo os três valores desejados para que possam ser somados e em seguida retornar o quadrado da sua soma')

n1 = int(input('Valor 1:'))
n2 = int(input('Valor 2:'))
n3 = int(input('Valor 3:'))
n4 = n1+n2+n3

print('O quadrado da soma dos valores é: {}'.format(n4**2))
