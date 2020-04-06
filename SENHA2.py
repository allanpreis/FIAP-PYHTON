nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Coloque abaixo sua senha para entrar\n')

n1 = str(input('Senha: '))
if (n1 == 'FIAP1TDS'):
    print('\nAcesso permitido')
else:
    print('\nVocê não tem acesso ao sistema')
