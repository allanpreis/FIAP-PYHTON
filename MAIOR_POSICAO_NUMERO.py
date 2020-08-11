def maior (lista):
    m = 0
    for i in range(5):          #-
        if i == 0:              # |
            m = lista[i]        # |
        else:                   # |-> Ter o maior número
            if lista[i] > m:    # |
                m = lista[i]    #-

    p = lista.index(m)          # Posição na lista

    return m, p

lista = []
for i in range(5):
    lista.append(int(input("Digite um número: ")))

maior_numero, posicao = maior(lista)

print("O maior número é {} na posição {}".format(maior_numero, posicao))





