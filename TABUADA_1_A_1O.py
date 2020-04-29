tab = 1

while(tab<=10):
    cont = 0
    while(cont<=10):
        calc = int(tab*cont)
        print(tab, "X", cont, "=", calc)
        cont+=1
    tab = tab + 1
    print('-' * 14)