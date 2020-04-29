nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Coloque abaixo sua senha para entrar\n')

n1 = int(input('Senha: '))
if n1 == 1214:
    print('\n\033[32mAcesso permitido\033[m')
else:
    print('\n\033[31mVocê não tem acesso ao sistema\033[m')