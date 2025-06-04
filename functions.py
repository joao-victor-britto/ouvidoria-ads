def lista(manifestacoes):
    if len(manifestacoes) >= 1:
        print("\nEssa é a nossa lista de manifestos")
        for item in manifestacoes:
            print(item)
    else:
        print("Não temos manifesto ate o momento")

def criarManifesto(manifesto,manifestacoes):
    print(f"Voce selecionou a opção {manifesto}")
    nome = input("\nDigite seu nome: ")

    entrada = input("\nDigite seu manifesto: ")
    if len(entrada) < 6 or len(entrada) > 250:
        print("\nDigite algo entre 6 e 250 caracteres")
    else:
        manifestacoes.append(entrada)
        print("Seu manifesto foi registrado!")

def listagemManifesto(manifestacoes):
    for pos in range(len(manifestacoes)):
        if manifestacoes >= 1:
            print(pos + 1, "-", manifestacoes[pos])
        else:
            print("Não temos manifesto registrado ate o momento")


def pesquisarPorCodigo(manifestacoes):
    posicao = int(input("\nDigite o codigo do manifesto: "))

    if posicao >= 1 and posicao <= len(manifestacoes):
        manifestoPesquisado = manifestacoes[posicao - 1]
        print(f"O Manifesto de escolha foi: {manifestoPesquisado} ")
    else:
        print("Não existe manifesto com esse codigo, para saber o codigo escolha a opçao 3!")

def removerPorCodigo(manifestacoes):
    posicao = int(input("Digite a posição: "))
    if posicao >= 1 and posicao <= len(manifestacoes):
        manifestoRemovido = manifestacoes.pop(posicao - 1)
        print(f"Manifesto removido: {manifestoRemovido}")
    else:
        print("Não existe manifesto com esse codigo!")