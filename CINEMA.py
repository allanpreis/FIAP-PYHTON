cont = 0
soma = 0
while(cont<2):
    idade = int(input("Insira sua idade: "))
    if(idade >= 0 and idade <= 122):
        print("Qual sua nota em relação ao filme?")
        print('-' * 30)
        print('''Notas:        
        [A] Ótimo 😆
        [B] Bom 🙂
        [C] Regular 😐
        [D] Ruim 😠
        [E] Péssimo 😤''')
        print('-' * 30)

        opiniao = str(input("Nota: ")).upper()
        if (opiniao == "A"):
            soma+= opiniao
        elif(opiniao == "B"):
            opiniao == 1
            soma += opiniao
        elif (opiniao == "C"):
            opiniao == 1
            soma += opiniao
        elif (opiniao == "D"):
            opiniao == 1
            soma += opiniao
        elif (opiniao == "E"):
            opiniao == 1
            soma += opiniao
        else:
            print("\n\033[31mResposta inválida\033[m\n")
        cont+=1
        soma+=idade
    else:
        print("\033[31mIdade digitada inválida, tente novamente\033[m")
        break

media = idade / cont

print("Tivemos {} respota A e a medida de é {}".format(opiniao, media))