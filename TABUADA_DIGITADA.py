resp = "S"
while (resp == "S"):
    tabuada = int(input('Insira qual tabuada deseja: '))
    multiplicador = 0
    while (multiplicador <= 10):
        if (tabuada >= 0):
            print('{} x {} = {}'.format(tabuada, multiplicador, tabuada * multiplicador))
            multiplicador += 1
        else:
            print("\n\033[31mNúmero digitado inválido!!!\033[m")
            break
    resp = str(input("\nDeseja fazer outra tabuada? [S/N] ")).upper()

