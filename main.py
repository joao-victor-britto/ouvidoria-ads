from functions import *

manifesto = 1

manifestacoes = [

]

while manifesto != 6:
    print("\n1) Lista de manifestos \n2) Criar manifesto \n3) Exibir quantidade de manifestos \n4) Pesquisar manifesto por codigo \n5) Excluir manifesto por codigo \n6) Sair")
    manifesto = int(input("\nQual opção deseja escolher? "))

    if manifesto == 1:
        lista(manifestacoes)

    elif manifesto == 2:
       criarManifesto(manifesto,manifestacoes)

    elif manifesto == 3:
        listagemManifesto(manifestacoes)

    elif manifesto == 4:
        pesquisarPorCodigo(manifestacoes)

    elif manifesto == 5:
        removerPorCodigo(manifestacoes)

    elif manifesto != 6:
        print("Opção Inválida")

print("\nObrigado por usar nosso sistema!")