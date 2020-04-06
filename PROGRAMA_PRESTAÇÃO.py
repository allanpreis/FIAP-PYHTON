nome = input('Insira seu nome:')
print('Olá, {}.\n'.format(nome),'Informe abaixo o valor do seu boleto, o percentual de juros e os dias de atraso para que possa saber quanto será o novo valor de seu boleto')

n1 = float(input("Valor do Boleto: R$"))
n2 = float(input("Percentual de Juros: "))
n3 = int(input("Dias de atraso: "))
n4 = n1+(n1*(n2/100))*n3

print("\nO novo valor a ser pago será R${}".format(n4))
