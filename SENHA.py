nome = input('Insira seu nome: ')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Coloque abaixo sua senha para entrar\n')

n1 = int(input('Senha: '))
if n1 == 1214:
    print('\nAcesso permitido')
else:
    print('\nVocê não tem acesso ao sistema')