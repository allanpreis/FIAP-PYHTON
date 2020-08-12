lista = ("Memória HyperX, 8GB", 340.80, "SSD Kingston 480GB", 470.47, "Logitech G604", 549.89)
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>7.2f}')
print('-'*40)
total = lista[1] + lista[3] + lista[5]
print(f'{"Total":.<30}', f'R${total:>7.2f}')