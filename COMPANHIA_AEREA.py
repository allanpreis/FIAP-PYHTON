nome = input('Insira seu nome:')
print('Bem-vindo, {}.\n'.format(nome), end='')
print('Informe abaixo o hemisfério de destino e se deseja somente ida ou ida e volta para cotação de valores:\n')

print('Atenção usuário, por questões de saúde contra o vírus COVID-19 estamos apenas funcionando para os hemisférios norte, noredeste e centro-oeste.\n')

destino = input("Você deseja comprar uma passagem de ida? [S/N] ").upper()
print('Escolha para onde deseja viajar:\n 1 --> Norte\n 2 --> Nordeste\n 3 --> Centro-Oeste\n')
local = input("Digite o seu destino: ")
if(destino == "N"):
    if(local == "1"):
        print("O preço da passagem de ida e volta para o Norte é R$",400)
    elif(local == "2"):
        print("O preço da passagem de ida e volta para o Nordeste é R$",628)
    elif(local == "3"):
        print("O preço da passagem de ida e volta para o Centro-Oeste é R$",1100)
elif(destino == "S"):
    if(local == "1"):
        print("O valor somente de ida para o Norte é de R$",228)
    elif(local == "2"):
        print("O valor somente de ida para o Nordeste é de R$",338)
    elif(local == "3"):
        print("O Valor somente de ida para o Centro-Oeste é de R$",628)


