cont = 3
senha = int(input('Digite sua senha: '))
while(senha!=1214 and cont>1):
    print('Senha Incorreta. Você tem mais', cont-1,'chances')
    senha = int(input('Digite novamente: '))
    cont = cont -1
if(senha == 1214):
    print('\033[32mAcesso permitido!\033[m')
else:
    print('\033[31mSenha Bloqueada!Procure o setor responsável\033[m')