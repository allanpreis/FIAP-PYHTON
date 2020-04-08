nome = input('Insira seu nome: ')
print('Bem-vindo(a), {}'.format(nome), end='')
print('\nInforme abaixo o preço do produto, sua categoria e sua situação')

preco = float(input('\nDigite o preço do produto: R$'))
opcao = 0
while opcao !=3:
    print('-' * 25)
    print('''     [1] Limpeza
     [2] Alimentação
     [3] Vestuário''')
    print('-' * 25)
    opcao = int(input('Qual a categoria do seu produto?'))
    if opcao == 1:
        if preco <= 25.00:
            au1 = preco * 5 / 100
            imposto = preco * 8 / 100
            novoPreco = preco + au1 - imposto

            if novoPreco <= 50.00:
                print('\nO produto recebe 5% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                break
            elif novoPreco > 50 and novoPreco <= 120:
                print('\nO produto recebe 5% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                break
            else:
                print('\nO produto recebe 5% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                break
        elif preco > 25.00:
            au1 = preco * 12 / 100
            imposto = preco * 8 / 100
            novoPreco = preco + au1 - imposto

            if novoPreco <= 50.00:
                print('\nO produto recebe 12% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                break
            elif novoPreco > 50 and novoPreco <= 120:
                print('\nO produto recebe 12% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                break
            else:
                print('\nO produto recebe 12% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                break
    elif opcao == 2:
        print('\nR - produtos que necessitam de refrigeração e N - produtos que não necessitam de refrigeração')
        situacao = input('Responda [R/N]: ').upper()
        if situacao == 'R':
            if preco <= 25.00:
                au1 = preco * 8 / 100
                imposto = preco * 5 / 100
                novoPreco = preco + au1 - imposto

                if novoPreco <= 50.00:
                    print('\nO produto recebe 8% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                    break
                elif novoPreco > 50 and novoPreco <= 120:
                    print('\nO produto recebe 8% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                    break
                else:
                    print('\nO produto recebe 8% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                    break
            elif preco > 25.00:
                au1 = preco * 15 / 100
                imposto = preco * 5 / 100
                novoPreco = preco + au1 - imposto

                if novoPreco <= 50.00:
                    print('\nO produto recebe 15% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                    break
                elif novoPreco > 50 and novoPreco <= 120:
                    print('\nO produto recebe 15% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                    break
                else:
                    print('\nO produto recebe 15% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                    break
        else:
            if preco <= 25.00:
                au1 = preco * 8 / 100
                imposto = preco * 5 / 100
                novoPreco = preco + au1 - imposto

                if novoPreco <= 50.00:
                    print('\nO produto recebe 8% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                    break
                elif novoPreco > 50 and novoPreco <= 120:
                    print('\nO produto recebe 8% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                    break
                else:
                    print('\nO produto recebe 8% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                    break
            elif preco > 25.00:
                au1 = preco * 15 / 100
                imposto = preco * 5 / 100
                novoPreco = preco + au1 - imposto

                if novoPreco <= 50.00:
                    print('\nO produto recebe 15% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                    break
                elif novoPreco > 50 and novoPreco <= 120:
                    print('\nO produto recebe 15% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                    break
                else:
                    print('\nO produto recebe 15% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                    break
    elif opcao == 3:
        if preco <= 25.00:
            au1 = preco * 10 / 100
            imposto = preco * 8 / 100
            novoPreco = preco + au1 - imposto

            if novoPreco <= 50.00:
                print('\nO produto recebe 10% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                break
            elif novoPreco > 50 and novoPreco <= 120:
                print('\nO produto recebe 10% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                break
            else:
                print('\nO produto recebe 10% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                break
        elif preco > 25.00:
            au1 = preco * 18 / 100
            imposto = preco * 8 / 100
            novoPreco = preco + au1 - imposto

            if novoPreco <= 50.00:
                print('\nO produto recebe 18% de aumento com 8% de imposto e seu novo preço é R${} sendo Barato'.format(novoPreco))
                break
            elif novoPreco > 50 and novoPreco <= 120:
                print('\nO produto recebe 18% de aumento com 8% de imposto e seu novo preço é R${} sendo Normal'.format(novoPreco))
                break
            else:
                print('\nO produto recebe 18% de aumento com 8% de imposto e seu novo preço é R${} sendo Caro'.format(novoPreco))
                break



