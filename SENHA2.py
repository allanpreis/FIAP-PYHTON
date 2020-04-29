nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Coloque abaixo sua senha para entrar\n')

n1 = str(input('Senha: '))
if (n1 == 'FIAP1TDS'):
    print('\n\033[32mAcesso permitido\033[m')
else:
    print('\n\033[31mVocê não tem acesso ao sistema\033[m')
