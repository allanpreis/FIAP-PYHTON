n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
contador = 0
n1 = n1 + 1
while n1 <= n2:
    if (n1 % 2 == 1) :
        contador = contador + 1
    n1 = n1 + 1
print("\nExiste {} número(s) ímpar(es)".format(contador))
