from operacoesbd import *

def listarManifesto(conexao):

    consulta = 'select * from manifesto'
    manifestos = listarBancoDados(conexao, consulta)

    if len(manifestos) == 0:
        print("Não existem Manifestos registrados a serem exibidos")
    else:
        print("Lista de Manifestaçoes")
        for item  in manifestos:
            print('Codigo do manifesto: ',item[0], '\nManifesto:', item[2], '\nAutor:', item[1])



def criarManifesto(conexao):

    nome = input("Digite como deseja ser indetificado em nosso sistema: ")
    manifesto = input("Digite seu manifesto: ")

    consulta = 'insert into manifesto (nome,manifesto) values (%s,%s)'
    dados = [nome, manifesto]

    gerarNovoManifesto = insertNoBancoDados(conexao,consulta,dados)
    print("Manifesto cadastro com sucesso, O codigo do seu manifesto é: ", gerarNovoManifesto)


def listarQuantidade(conexao):
    consulta = 'select count(*) from manifesto'
    manifestos = listarBancoDados(conexao, consulta)
    quantidadeManifestos = manifestos[0][0]

    # Verifica a quantidade de manifesto para estar ortograficamente correto
    if quantidadeManifestos >= 2:
        print("Atualmente temos", quantidadeManifestos, "manifestos.")
    else:
        print("Atualmente temos", quantidadeManifestos, "manifesto.")
        


def manifestoPeloCodigo(conexao):
    codigoManifesto = int(input("Digite o código do manifesto a ser pesquisado: "))
    consulta = 'select * from manifesto where codigo = %s'
    dados = [codigoManifesto]
    manifestos = listarBancoDados(conexao, consulta, dados)


    if len(manifestos) == 0:
        print("Não existe manifesto com o código informado.")
    else:
        print("Codigo: ", manifestos[0][0], "\nAutor do manifesto:", manifestos[0][1], "\nManifesto: ", manifestos[0][2])


def excluirManifestoPeloCodigo(conexao):
    codigoManifesto = int(input("Digite o código do manifesto que deseja excluir"))
    consulta = 'delete from manifesto codigo = %s'
    dados = [codigoManifesto]
    manifestos = excluirBancoDados(conexao, consulta, dados)
    print(manifestos)
