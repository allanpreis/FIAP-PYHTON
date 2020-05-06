print('Vamos a brincadeira.')
print('Digite um número e depois peça a um colega para que tente acerta o número')
n1 = int(input('\nInsira o número: '))
print('\nAgora chute o valor inserido pelo colega')
n2 = int(input("Chute o valor: "))
cont = 1
while(n1!=n2):
    cont += 1
    if(n2<n1):
        print('\033[31m*** CHUTOU BAIXO ***\033[m')
    elif(n2>n1):
        print('\033[31m*** CHUTOU ALTO ***\033[m')
    n2 = int(input("Chute o valor: "))
print('\n\033[32m*** ACERTOU! PARABÉNS! VOCÊ PRECISOU DE {} CHANCE(S) ***\033[m'.format(cont))

