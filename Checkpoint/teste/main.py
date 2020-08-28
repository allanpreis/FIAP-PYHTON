import cadastrar
import alterar
import excluir
import comprar
import vender

menu = 0

codigo = []
descricao = []
quantidade = []
estoque = []

while menu != 7:
    print("\nMenu")
    opcao = int(input("\t1 - Cadastrar Produto\n\t2 - Alterar Produto\n\t3 - Excluir Produto"
                      "\n\t4 - Listar Estoque\n\t5 - Comprar Produto"
                      "\n\t6 - Vender Produto\n\t7 - Sair\n\nDigite a opção desejada: "))
    if opcao == 1: #Cadastrar Produto
        codigo = int(input("Código do produto: "))
        if codigo in estoque:
            print("\033[31mCódigo já cadastrado\033[m")
        else:
            descricao = input("Descrição do produto: ").upper()
            quantidade = int(input("Quantidade de estoque: "))
            estoque.append(codigo)
            estoque.append(descricao)
            while quantidade <= 0:
                print("\033[31mNão é permitido ter estoque menor ou igual a zero\033[m")
                quantidade = int(input("Quantidade de estoque: "))

            estoque.append(quantidade)

            print(estoque)

    elif opcao == 2: #Alterar Produto
        alterar.alterar_produto()

    elif opcao == 3: #Excluir Produto
        excluir.excluir_produto()

    elif opcao == 4: #Listar Estoque
        print(estoque)

    elif opcao == 5: #Comprar Produto
        comprar.comprar_produto()

    elif opcao == 6: #Vender Produto
        vender.vender_produto()

    elif opcao == 7: #Sair
        print("\nSaindo...")
        break

    else:
        print("\n\033[31mOpção Inválida! Tente Novamente\033[m")