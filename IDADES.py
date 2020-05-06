n = int(input("Quantas idades seram calculadas: "))
i = 0
cont = 0
soma = quant = maior = menor = 0
somaidade = 0
maior18 = 0
menor18 = 0
contamenor =0
contamaior =0
tem18 = 0
while(i < n):
    idade = int(input("Idade: "))
    cont+= 1
    somaidade+= idade
    quant+= 1
    if(idade > 18):
        cont+=1
        maior18+=1
    if(idade < 18):
        cont+=1
        menor18+=1
    if(idade == 18):
        cont+=1
        tem18+=1
    if(quant == 1):
        maior = menor = idade
    else:
        if(idade>maior):
            maior = idade
            cont += 1
            contamaior+=1
        if(idade<menor):
            menor = idade
            cont += 1
            contamenor+=1
    i+=1
media = somaidade / cont
print("\n{} possuem 18 anos".format(tem18))
print("{} são maiores de 18 anos".format(maior18))
print("{} são menores de 18 anos".format(menor18))
print("A soma das idades é {}".format(somaidade))
print("A média das idades é {}".format(media))
print("A maior idade é {} e {} pessoas possuem essas idade".format(maior, contamaior))
print("A menor idade é {} e {} pessoas possuem essas idade".format(menor, contamenor))
