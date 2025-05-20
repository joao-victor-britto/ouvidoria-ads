opcao = 1

manifestacoes = [

]

while opcao != 6:
    print("\n1) Listar manifesto 2) Criar manifesto 3) Exibir quantidade de manifestos 4) Pesquisar manifesto por codigo 5) Excluir manifesto por codigo 6)Sair")
    opcao = int(input("Qual opção deseja escolher? "))
    if opcao == 1:
        if len(manifestacoes) >= 1:
            print("\nEssa é a nossa lista de manifestos")
            for item in manifestacoes:
                print(item)
        else:
            print("Não temos manifesto ate o momento")
    elif opcao == 2:
        entrada = input("\nDigite seu manifesto: ")
        if len(entrada) <= 1:
            print("\nSeu manifesto tem 1 ou menos caracteres")
        else:
            manifestacoes.append(entrada)
            print("Seu manifesto foi registrado!")

    elif opcao == 3:
        for pos in range(len(manifestacoes)):
            print(pos + 1, "-", manifestacoes[pos])

    elif opcao == 4:
        posicao = int(input("\nDigite sua posicao: "))
        if posicao >= 1 and posicao <= len(manifestacoes):
            manifestoPesquisado = manifestacoes[posicao - 1]
            print(f"O Manifesto de escolha foi: {manifestoPesquisado} ")
        else:
            print("Não existe manifesto nessa posição!")

    elif opcao == 5:
        posicao = int(input("Digite a posição: "))
        if posicao >= 1 and posicao <= len(manifestacoes):
            manifestacoes.pop(posicao - 1)
            print("Manifesto removido com sucesso!")
        else:
            print("Não existe manifesto nessa posição!")

    elif opcao != 6:
        print("Opção Inválida")

print("\nObrigado por usar nosso sistema!")