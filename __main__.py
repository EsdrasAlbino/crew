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

window_width, window_height = screen.get_size()

#Proporção da pista pista 1:1 na tela 2:1 
if window_height*2 < window_width:
    track_left = window_width//2 - window_height//2
    track_right = track_left + window_height
    track_top = 0
    track_botton = window_height
else:
    track_left = window_width//4
    track_right = 3*window_width//4
    track_top = 0
    track_botton = window_width//2
    
track = pygame.Rect((track_left, track_top, track_right - track_left, track_botton - track_top))

background = pygame.image.load('assets/Fundo Espacial.jpg')
background = pygame.transform.scale(background, (window_width, window_height))

asteroid = pygame.image.load('assets/asteroid.png')
asteroid_height = (track_right - track_left)/10
asteroid_width = asteroid_height

asteroid_left = track_left - asteroid_width
asteroid_top = 0
asteroid = pygame.transform.scale(asteroid, (asteroid_width, asteroid_height))

spacecraft = pygame.image.load('assets/nave completa.png')
spacecraft_width = (track_right - track_left)/5
spacecraft_height = 31*spacecraft_width//45
spacecraft = pygame.transform.scale(spacecraft,(spacecraft_width, spacecraft_height))
spacecraft_left = track_left

propellant = pygame.image.load('assets/propulsor.png')
propellant_height = track_botton/ 10
propellant_width = 320*propellant_height//580
propellant = pygame.transform.scale(propellant,(propellant_width, propellant_height))
propellant_left = window_width//2

bullet = pygame.image.load('assets/bullet.png')
bullet_height = track_botton/ 20
bullet_width = 14*bullet_height//26
bullet = pygame.transform.scale(bullet,(bullet_width, bullet_height))
bullet_left = window_width//2 - bullet_width*2

comet = pygame.image.load('assets/comet.png')
comet_height = track_botton//10
comet_width = comet_height
comet = pygame.transform.scale(comet,(comet_width, comet_height))
comet = pygame.transform.rotozoom(comet, 45, 1)
comet_left = window_width//2 - comet_width*3



#Obs.: Canto superior esquerdo = (0,0)

run = True
while run:
    window_width, window_height, track_right, track_left, track_botton, track_top, background, asteroid, asteroid_width, asteroid_height, asteroid_left, spacecraft, spacecraft_width, spacecraft_height, spacecraft_left, propellant, propellant_height, propellant_width, propellant_left, bullet, bullet_height, bullet_width, bullet_left, comet, comet_height, comet_width, comet_left, track = change_size_window(screen, window_width, spacecraft_left, propellant_left, bullet_left, comet_left)

    #Recarregar papel de parede, não deixando rastro
    screen.blit(background, (0, 0))

    #Pista(Para ter noção de onde vai ser o jogo em si)
    # pygame.draw.rect(screen, (0, 255, 255), pista)

    # #Asteroides
    while asteroid_top < window_height:
        screen.blit(asteroid, (asteroid_left, asteroid_top))
        screen.blit(asteroid, (asteroid_left + track_right - track_left + asteroid_height, asteroid_top))
        asteroid_top = asteroid_top + asteroid_height
    asteroid_top = 0

    screen.blit(spacecraft, (spacecraft_left, track_botton - spacecraft_height))
    screen.blit(propellant, (propellant_left, propellant_height))
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