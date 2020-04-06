nome = input('Insira seu nome:')
print('Olá, {}.\n'.format(nome),'Informe abaixo quantos votos cada candidato recebeu, os votos nulos e os brancos, para saber o percentual e o total dos resultados da eleição')

n1 = int(input("Quantia de votos do candidato A: "))
n2 = int(input("Quantia de votos do candidato B: "))
n3 = int(input("Quantia de votos do candidato C: "))
n4 = int(input("Votos em branco: "))
n5 = int(input("Votos nulos: "))
n6 = n1+n2+n3+n4+n5
n7 = ((n1*100)/n6)
n8 = ((n2*100)/n6)
n9 = ((n3*100)/n6)
n10 = ((n4*100)/n6)
n11 = ((n5*100)/n6)


print("\nNessa eleição tiveram {} eleitores, com o candidato A com {:.2f}% dos votos e o candidato B com {:.2f}%,\no candidato C com {:.2f}% sendo {:.2f}% de votos em branco e {:.2f}% votos nulos ".format(n6, n7, n8, n9, n10, n11))
