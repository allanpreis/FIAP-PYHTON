def media(tuplas):
    lista = list(tuplas)
    media = sum(lista) / len(tuplas)
    return media

from random import randint
tuplas = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))

print("tuplas = {}".format(tuplas))
print("A média é {}".format(media(tuplas)))