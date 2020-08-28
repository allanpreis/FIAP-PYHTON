nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}'.format(nome), end='')
print('\nInforme abaixo o número de horas extras e o número de horas que faltou ao trabalho')

hx = int(input('\nDigite o número de horas extras feitas: '))
hf = int(input('Digite a quantia de horas que faltou no trabalho: '))

m1 = hx * 60
m2 = hf * 60

h = m1 - (2/3*(m1-m2))
if h >2400:
    print('\nVocê receberá R$1500 de gratificação de Natal')
elif h >= 1800 and h <= 2399:
    print('\nVocê receberá R$1000 de gratificação de Natal')
elif h >= 1200 and h <=1799:
    print('\nVocê receberá R$890 de gratificação de Natal')
else:
    print('\nVocê receberá R$500 de gratificação de Natal')