opcao = 0
while opcao !=5:
    print('|------------ Menu de Opções ------------|')
    print('''    [1] Gerar dígitos verificadores 
    [2] Verificar dígitos verificadores 
    [3] Estado de origem 
    [4] Sair''')
    print('-' * 42)
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        cpf = input("Digite o número do CPF sem os 2 últimos dígitos: ")