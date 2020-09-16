# Desenvolvendo um projeto para o curso
# Vamos criar um menu em Python, usando modularização.
from ex115 import titulo, menu, leiaInt
from ex115.arquivo import *# assim eu importo a biblioteca toda
from time import sleep


arq = 'projetoM3.txt'

if not arquivoExiste(arq):# Se o aquivo nao existir, ele cria um arquivo com o nome.
    criaArquivo(arq)

while True: 
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair Do Sistema'])
    if resposta == 1:
        titulo('Opção 1')
        #mostra o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        titulo('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do Sistema....')
        sleep(2)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
