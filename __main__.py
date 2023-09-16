import pygame
import os #Tamanho da tela
from pygame.locals import * 


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

def change_size_window(screen):
    window_width, window_height = screen.get_size()

    #Proporção da pista pista 1:1 na tela 2:1 
    if window_height*2 < window_width:
        pista_left = window_width//2 - window_height//2
        pista_right = pista_left + window_height
        pista_top = 0
        pista_botton = window_height
    else:
        pista_left = window_width//4
        pista_right = 3*window_width//4
        pista_top = 0
        pista_botton = window_width//2
        
    pista = pygame.Rect((pista_left, pista_top, pista_right - pista_left, pista_botton - pista_top))

    background = pygame.image.load('crew/assets/Fundo Espacial.jpg')
    background = pygame.transform.scale(background, (window_width, window_height))

    asteroide = pygame.image.load('crew/assets/asteroid.png')
    asteroide_height = (pista_right - pista_left)/10
    asteroide_width = asteroide_height

    asteroide_left = pista_left - asteroide_width
    asteroide_top = 0
    asteroide = pygame.transform.scale(asteroide, (asteroide_width, asteroide_height))

    spacecraft = pygame.image.load('crew/assets/nave completa.png')
    spacecraft_width = (pista_right - pista_left)/5
    spacecraft_height = 31*spacecraft_width//45
    spacecraft = pygame.transform.scale(spacecraft,(spacecraft_width, spacecraft_height))
    spacecraft_left = pista_left

    propulsor = pygame.image.load('crew/assets/propulsor.png')
    propulsor_height = pista_botton/ 10
    propulsor_width = 320*propulsor_height//580
    propulsor = pygame.transform.scale(propulsor,(propulsor_width, propulsor_height))
    propulsor_left = window_width//2

    bullet = pygame.image.load('crew/assets/bullet.png')
    bullet_height = pista_botton/ 20
    bullet_width = 14*bullet_height//26
    bullet = pygame.transform.scale(bullet,(bullet_width, bullet_height))
    bullet_left = window_width//2 - bullet_width*2

    comet = pygame.image.load('crew/assets/comet.png')
    comet_height = pista_botton//10
    comet_width = comet_height
    comet = pygame.transform.scale(comet,(comet_width, comet_height))
    comet = pygame.transform.rotozoom(comet, 45, 1)
    comet_left = window_width//2 - comet_width*3

    return window_width, window_height, pista_right, pista_left, pista_botton, pista_top, background, asteroide, asteroide_width, asteroide_height, asteroide_left, asteroide_top, spacecraft, spacecraft_width, spacecraft_height, spacecraft_left, propulsor, propulsor_height, propulsor_width, propulsor_left, bullet, bullet_height, bullet_width, bullet_left, comet, comet_height, comet_width, comet_left, pista

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
                screen = pygame.display.set_mode((1000, 500), RESIZABLE)
                fullscreen = False
    
    #Quando apertar no ESC fechar
    if key[pygame.K_ESCAPE] == True:
        run = False


    #Atualizar
    pygame.display.update()

pygame.quit()