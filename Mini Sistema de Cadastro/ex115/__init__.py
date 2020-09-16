#Parte do codigo reponsável pela interface.

def leiaInt(msg):
    while True:
        try:#----> Tente
            n = int(input(msg))
        except (TypeError, ValueError):# caso ocorra: 
            print('\033[31mPor favor, digite um número inteiro(ex: 0,1,2,3,4...) válido.\033[m')
            continue# o comando continue garante a permanencia dentro do laço infinito
        except KeyboardInterrupt:
            print('Falta de dados por parte do usuário.')
            return 0
        else:
            return n
        

def titulo(msg):
    print('-'*len(msg*3))
    print(msg.center(len(msg*3)))
    print('-'*len(msg*3))
    

def linha(msg = 42):
        return '-'* msg

def menu(lista):
    titulo('MENU PRÍNCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
