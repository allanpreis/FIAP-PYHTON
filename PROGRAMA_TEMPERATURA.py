nome = input('Insira seu nome:')
print('Olá, {}.\n'.format(nome),'Informe abaixo a temperatura atual °C e o saberá quanto é em ºF')

n1 = float(input("Temperatura atual °C:"))
n2 = ((9*n1)/5)+32


print("\nSua temperatura atual em Fahrenheit é {}".format(n2), "ºF")
