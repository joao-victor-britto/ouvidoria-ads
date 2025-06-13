from operacoesbd import *
from ouvidoria import *

conexao = criarConexao("localhost", "root", "12345", "ouvidoria")

manifesto = 1

while manifesto != 6:
    print("\n1) Lista de manifestos \n2) Criar manifesto \n3) Exibir quantidade de manifestos \n4) Pesquisar manifesto por codigo \n5) Excluir manifesto por codigo \n6) Sair")
    manifesto = int(input("\nQual opção deseja escolher? "))

    if manifesto == 1:
        listarManifesto(conexao)

    elif manifesto == 2:
        criarManifesto(conexao)

    elif manifesto == 3:
        listarQuantidade(conexao)

    elif manifesto == 4:
        manifestoPeloCodigo(conexao)

    elif manifesto == 5:
        excluirManifestoPeloCodigo(conexao)

    elif manifesto != 6:
        print("Opção Inválida")

encerrarConexao(conexao)

print("\nObrigado por usar nosso sistema!")