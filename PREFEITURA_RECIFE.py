nome = input("Insira seu nome: ")
print("Olá, {}.\n".format(nome), end='')
print("Informe abaixo o valor de seu salário bruto e o valor de sua prestação, para que saiba se o empréstimo possa ser feito.\n")

n1 = float(input("Salário bruto: R$"))

if n1 <= 0:
    print("Salário inválido, por favor informe um salário novamente!")

else:
    print("Informe abaixo o valor de sua prestação:")
    n2 = float(input("Valor da prestação: R$"))

    if n2 <=0:
     print("Valor da prestação inválida, por favor informe novamente!")
    else:
        minimo = n1 * 30 / 100
        if n2 <= minimo:
         print("Empréstimo aprovado!")
        else:
         print("Empréstimo negado!")

print('\nPrograma encerrado')
