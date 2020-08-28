n = int(input("Insira um número: "))
n1 = 1
n2 = 1
n3 = 1
cont = 3
while(cont <= n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
print('Esse número corresponde ao valor {} da sequência de Fibonacci'.format(n3))
