cont = 0
soma = quant = maior = menor = 0
while(cont<20):
    n1 = int(input("Insira um número: "))
    cont = cont + 1
    soma+= n1
    quant+= 1
    if(quant == 1):
        maior = menor = n1
    else:
        if(n1>maior):
            maior = n1
        if(n1<menor):
            menor = n1
print("\nO maior número é {} e o menor é {} ".format(maior, menor))