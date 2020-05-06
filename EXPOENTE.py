base = int(input("Insira o valor para base: "))
expoente = int(input("Insira o valor para ser o expoente: "))

i = 0
resp = 1
while(i<expoente):
    resp*=base
    i+=1
print("Resultado: ", resp)
