n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))
soma = 0

if(n1>n2):
    aux = n1
    n1 = n2
    n2 = aux
while(n1<n2):
    n1+=1
    if(n1!=n2):
        soma+= n1
        print(n1)
print("A soma dos números existentte entre os números digitados é ", soma)
