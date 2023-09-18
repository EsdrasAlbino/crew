import pygame
import os #Tamanho da tela
from pygame.locals import * 
from util.change_window_size_util import change_size_window

#Informação da tela toda
os.environ['SDL_VIDEO_CENTERED'] = '1' #Tem que ser antes do pygame.init()

pygame.init()

#Informação da tela toda
info = pygame.display.Info() #Tem que ser antes do .set_mode()
screen_width,screen_height = info.current_w,info.current_h

#Nome da Janela
pygame.display.set_caption('Corrida Espacial')

#Maximizar, minimizar e redimencionar janela
screen = pygame.display.set_mode((screen_width/2, screen_height/2), RESIZABLE)
fullscreen = False

#Obs.: Canto superior esquerdo = (0,0)

run = True
while run:
    window_width, window_height, pista_right, pista_left, pista_botton, pista_top, background, asteroide, asteroide_width, asteroide_height, asteroide_left, asteroide_top, spacecraft, spacecraft_width, spacecraft_height, spacecraft_left, propulsor, propulsor_height, propulsor_width, propulsor_left, bullet, bullet_height, bullet_width, bullet_left, comet, comet_height, comet_width, comet_left, pista = change_size_window(screen)

    #Recarregar papel de parede, não deixando rastro
    screen.blit(background, (0, 0))

    #Pista(Para ter noção de onde vai ser o jogo em si)
    # pygame.draw.rect(screen, (0, 255, 255), pista)

    # #Asteroides
    while asteroide_top < window_height:
        screen.blit(asteroide, (asteroide_left, asteroide_top))
        screen.blit(asteroide, (asteroide_left + pista_right - pista_left + asteroide_height, asteroide_top))
        asteroide_top = asteroide_top + asteroide_height
    asteroide_top = 0

    screen.blit(spacecraft, (spacecraft_left,pista_botton - spacecraft_height))
    screen.blit(propulsor, (propulsor_left, propulsor_height))
    screen.blit(bullet, (bullet_left, bullet_height))
    screen.blit(comet, (comet_left, comet_height))

    #Quando pressionar tecla
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        #Ação (x,y)
        spacecraft_left = spacecraft_left - 1
    elif key[pygame.K_d] == True:
        spacecraft_left = spacecraft_left + 1

    #Quando apertar no X fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Modo tela cheia
        if event.type == pygame.KEYDOWN and event.key == K_f:
            if not fullscreen:
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                fullscreen = True
            else:
                screen = pygame.display.set_mode((screen_width//2, screen_height//2), RESIZABLE)
                fullscreen = False
    
    #Quando apertar no ESC fechar
    if key[pygame.K_ESCAPE] == True:
        run = False


    #Atualizar
    pygame.display.update()

pygame.quit()