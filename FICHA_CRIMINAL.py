pergunta1 = ("\nTelefonou para a vítima? [S/N] ")
pergunta2 = ("Esteve no local do crime? [S/N] ")
pergunta3 = ("Mora perto da vítima? [S/N] ")
pergunta4 = ("Devia para a vítima? [S/N] ")
pergunta5 = ("Já trabalhou com a vítima? [S/N]")

perguntas = (pergunta1,pergunta2,pergunta3,pergunta4,pergunta5)

resposta = 0

def interrogatorio():
    contador = 0
    while (contador < 6):
        perguntas = input(perguntas[contador]).upper()
        while (perguntas != "S" and perguntas != "N"):
            print("Responda apenas 'S' para sim ou 'N' para não")
            perguntas = input(perguntas[contador]).upper()
        resposta.append(perguntas)
        contador+=1

    return resposta.contador('S')














