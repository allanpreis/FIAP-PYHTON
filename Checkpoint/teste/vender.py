import main

def vender_produto():
    codigo = int(input("Código do produto: "))
    for alterar in main.estoque:
        if main.estoque[0] == codigo:
            print("\nCódigo:", f"{main.estoque[0]}", "Descrição:", f"{main.estoque[1]}", "Quantidade:", f"{main.estoque[2]}\n")
            quant_prod = int(input("Quanto deseja vender: "))
            while quant_prod <= 0:
                print(
                    "\033[31mImpossível vender uma quantia menor ou igual a zero\033[m")  # ==> Vendendo somente o primeiro item da lista
                quant_prod = int(input("Quanto deseja vender: "))

            main.estoque[2] = main.estoque[2] - quant_prod
            print("\nCódigo:", f"{main.estoque[0]}", "Descrição:", f"{main.estoque[1]}", "Quantidade:", f"{main.estoque[2]}\n")
            break
        else:
            print("\033[31mProduto não cadastrado\033[m")
            break