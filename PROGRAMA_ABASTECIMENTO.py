
nome = input('Insira seu nome:')
print('Olá, {}.\n'.format(nome),'Informe abaixo o preço do combustível e qual o valor que deseja abastacer')

n1 = float(input('Preço do Combustível: R$'))
n2 = float(input('Quanto reais deseja abastecer? R$'))
n3 = n2 / n1

print('\nVocê abastecera {:.2f}l de gasolina'.format(n3))