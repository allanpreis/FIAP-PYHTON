nome = input('Insira seu nome:')
print('Olá, {}.\n'.format(nome),'Informe abaixo à altura e o raio da lata de óleo para saber seu volume')

n1 = float(input("Altura: "))
n2 = float(input("Raio: "))
n3 = 3.14 * (n2 * n2) * n1

print("\nO volume da sua lata de óleo é {}".format(n3))
