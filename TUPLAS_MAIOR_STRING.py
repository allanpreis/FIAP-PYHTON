def maior(tuplas):
    maior = 0
    posicao = 0
    lista = list(tuplas)
    for p in lista:
        if (len(p) > posicao):
            posicao = len(p)
            maior = p
    return maior

tuplas = ("Alexandre", "Allan", "Dihogo", "Fernando", "Juan")
print("tuplas = {}".format(tuplas))
print("A maior string é {}".format(maior(tuplas)))
