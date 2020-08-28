import main

def excluir_produto():
    cont = 3
    senha = input("Digite sua senha: ")
    while senha != "yN1825*a" and cont > 1:
        print("\033[31mSenha incorreta, você têm mais ", cont - 1, " tentativas.\033[m")
        senha = input("Digite novamente.\nSenha: ")
        cont = cont - 1
    if senha == "yN1825*a":
        print("\033[32mAcesso permitido!\033[m")
        codigo = int(input("Código: "))
        if codigo in main.estoque:
            print("Descrição: ", main.estoque[1], "Quantidade: ", main.estoque[2])
            opcao = input("Deseja excluir o produto? [S/N] ").upper()
            if opcao == "s".upper():
                # estoque.pop(estoque.index(codigo))
                # estoque.pop(estoque.index(descricao))                                                             #==> ValueError: [] is not in list
                # estoque.pop(estoque.index(quantidade))
                print("\033[32mProduto excluido com sucesso\033[m")
            elif opcao == "n".upper():
                print("\033[31mProduto não excluido\033[m")
            else:
                print("\033[31mOpção inválida\033[m")
        else:
            print("\033[31mProduto não cadastrado\033[m")
    else:
        print("\033[31mSeu acesso foi bloqueado! Procure o administrador.\033[m")
        exit()