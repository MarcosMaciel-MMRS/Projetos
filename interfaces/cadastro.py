from PySimpleGUI import PySimpleGUI as sg


#Layout

sg.theme('Reddit')# tema escolhido da biblioteca
layout = [ # aqui fica as configurações fixas no layout
    [sg.Text('Usuário:'),sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha:  '),sg.Input(key='senha', password_char='*', size=(20,1))],# observação o password_char é o responsavel por omitir a senha.
    [sg.Checkbox('Salvar o Login: [S/N]')],
    [sg.Button('Entrar')]
]
#janelas


janela = sg.Window('Tela de Longin', layout)# aqui fica o nome da janela.


#eventos

while True:# aqui é feito a validação dos dados
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:# assim o programa fica aberto ate ser ordenado à se fechar
        break
    elif eventos == 'Entrar':# evento disparado ao apertar no botao entrar.
        if valores['usuario'] == 'xmaciex' and valores['senha']== '2604':# aqui eu trabalhei as kays 
            print('Entra, a casa é tua LADRÃO!')
        else:
            print('QUAL FOI!!! Ta vacilando? ta doidão, saí fora ladrão!')
