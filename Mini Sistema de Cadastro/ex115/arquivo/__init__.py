#Vamos ver como fazer acesso a arquivos usando o Python.
#Aqui fica as funcionalidades do Sistema criado no exercicio 115
from ex115 import titulo

def arquivoExiste(nome):
    try:#---> aqui manda tentar abir o arquivo
        a = open(nome, 'rt')#leitura de arquivo
        a.close()
    except FileNotFoundError:#----> se nao encontrar o arquivo, ele retorna falso
        return False
    else:#----> e se encontrar ele retorna verdadeiro
        return True


def criaArquivo(nome):
    try:
        a= open(nome, 'wt+')#gravação de arquivo, "+" incluindo o arquivo. 
        a.close()
    except:
        print('Houve um Erro na criação do Arquivo!')
    else:
        print(f'Arquivo {nome} Criado com sucesso!')


def lerArquivo(nome):
    try:
        a =open(nome, 'rt')# read text
    except:
        print('ERRO ao ler o arquivo!')
    else:
        titulo('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '' )# o replece subistitui(vai mudar o q for \n, por vazio)
            print(f'{dado[0]:<30}{dado[1]:>22} anos')# dado[0]- nome; dado[1]- idade
    finally:
        a.close()


def cadastrar(arq, nome= 'Desconhecido', idade=0):
    try:
        a = open(arq, 'at')# 'a'--> append no aquivo texto 
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever o dados.')
        else:
            print(f'Novo Cadastro Realizado com Sucesso!')
            a.close()
    