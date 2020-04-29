nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo suas 3 notas e seu número de faltas para saber sua  situação final\n')

p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
p3 = float(input('Terceira nota: '))
falta = int(input('Número de faltas: '))
reprovado = 80 * (25/100)
media = (p1 + p2 + p3) / 3

if (falta > reprovado):
        print('\n\033[31m{} foi Reprovado por Falta!!!\033[m'.format(nome))
elif (media < 7.0):
        print('\n\033[31m{} foi Reprovado por Média!!!\033[m'.format(nome))
else:
    print('\n\033[32m{} foi Aprovado!!!\033[m'.format(nome))