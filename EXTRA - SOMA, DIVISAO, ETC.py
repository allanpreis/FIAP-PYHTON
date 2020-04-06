print('Informe abaixo os dois valores que deseja fazer a soma, multiplicação, divisão inteiro e resto da divisão')

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
soma = n1+n2
multi = n1*n2
divint = n1//n2
divrest = n1%n2

print('A soma dos valores é: {}\nA mulplicação dos valores é: {}\nSua divisão inteira é: {}\nO resto da divisão é: {}'.format(soma, multi, divint, divrest))