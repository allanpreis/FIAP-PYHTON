nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo o número da sua conta para que possa gerar seu código verificador:\n')

print('Digite somente os 3 primeiros números da conta\n')

conta = int(input("Digite o número de sua conta: "))
if conta >= 100 and conta <= 999:
    n1 = conta // 100
    n2 = (conta % 100) // 10
    n3 = conta % 10

    numeroInvertido = (n3*100) + (n2*10) + n1
    c = conta + numeroInvertido

    s1 = (c // 100) * 1
    s2 = ((c % 100) // 10) * 2
    s3 = (c % 10) * 3

    s = (s1 + s2 + s3) % 10

    print('\n Seu código verificador é {}'.format(s))
else:
    print('\n\033[31mO número de conta digitado é inválido\033[m')




