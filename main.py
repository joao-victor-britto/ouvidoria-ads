manifesto = 1

manifestacoes = [

]

while manifesto != 6:
    print("\n1) Lista de manifestos \n2) Criar manifesto \n3) Exibir quantidade de manifestos \n4) Pesquisar manifesto por codigo \n5) Excluir manifesto por codigo \n6) Sair")
    manifesto = int(input("\nQual opção deseja escolher? "))

    if manifesto == 1:
        if len(manifestacoes) >= 1:
            print("\nEssa é a nossa lista de manifestos")
            for item in manifestacoes:
                print(item)
        else:
            print("Não temos manifesto ate o momento")

    elif manifesto == 2:
        entrada = input("\nDigite seu manifesto: ")
        if 5 >= len(entrada) > 250:
            print("\nDigite algo entre 6 e 250 caracteres")
        else:
            manifestacoes.append(entrada)
            print("Seu manifesto foi registrado!")

    elif manifesto == 3:
        for pos in range(len(manifestacoes)):
            print(pos + 1, "-", manifestacoes[pos])

    elif manifesto == 4:
        posicao = int(input("\nDigite sua posicao: "))
        if posicao >= 1 and posicao <= len(manifestacoes):
            manifestoPesquisado = manifestacoes[posicao - 1]
            print(f"O Manifesto de escolha foi: {manifestoPesquisado} ")
        else:
            print("Não existe manifesto nessa posição!")

    elif manifesto == 5:
        posicao = int(input("Digite a posição: "))
        if posicao >= 1 and posicao <= len(manifestacoes):
            manifestoRemovido = manifestacoes.pop(posicao - 1)
            print(f"Manifesto removido: {manifestoRemovido}")
        else:
            print("Não existe manifesto nessa posição!")

    elif manifesto != 6:
        print("Opção Inválida")

print("\nObrigado por usar nosso sistema!")