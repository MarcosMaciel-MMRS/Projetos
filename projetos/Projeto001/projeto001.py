# a ideia é cirar um cronometro, q ao apertar no butao a contagem se inicia, e no outro finaliza. e depois ir deixando mais complexo.
# descobrir o pq o visual nao esta lendo a biblioteca; 
import pygame
import tkinter
pygame.init()

janela = pygame.display.set_mode((800,400))# assim eu crio uma janela e começo a criar meu app (largura, tamanho)
pygame.display.set_caption('Cronometro')


janela_aberta = True
while janela_aberta:# condição para poder fechar a janela
    button(master = None, activebackground = blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False 


pygame.quit()
