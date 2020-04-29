cont = 0
soma = 0
while(cont<5):
    idade = int(input("Insira sua idade: "))
    if(idade >= 0 and idade <= 122):
        cont = cont + 1
        soma = soma + idade
    else:
        print("\033[31mIdade digitada inválida, tente novamente\033[m")
media = idade / cont
print("\nA média simples das idades é ", media)
