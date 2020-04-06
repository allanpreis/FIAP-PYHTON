nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo suas 3 notas para assim ter sua média ponderada\n')

n1 = float(input('Trabalho de Laboratório: '))
n2 = float(input('Avaliação Semestral: '))
n3 = float(input('Exame Final: '))

p1 = ((n1*2)+(n2*3)+(n3*5))
p2 = 2+3+5
resultado = p1 / p2
if(resultado):
    if (resultado >= 8.0 or resultado <= 10.0):
        print('\nConceito A - 8.0 a 10.0')
    elif (resultado >= 7.0 or resultado <= 7.9):
            print('\nConceito B - 7.0 a 7.9')
    elif (resultado >= 6.0 or resultado <= 6.9):
            print('\nConeito C - 6.0 a 6.9')
    elif (resultado >= 5.0 or resultado <= 5.9):
            print('\nConceito D - 5.0 a 5.9')
else:
    if (resultado >= 0.0 or resultado <=4.9):
         print('\nConceito E - 0.0 a 4.9')


print('\nSua nota será {:.1f}'.format(resultado))