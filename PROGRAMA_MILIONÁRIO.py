nome = input('Insira seu nome:')
print('Olá, {}.\n'.format(nome),'Informe abaixo seu salário e o valor de suas despesas para saber em quanto tempo ficará milionário')

n1 = float(input("Salário: R$"))
n2 = float(input("Valor das despesas: R$"))
n3 = n1-n2
n4 = n3*12
n5 = 1000000/n4

print("\nVocê ficará milionário em {:.0f} anos".format(n5))
