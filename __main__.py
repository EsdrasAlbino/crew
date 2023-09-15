import pygame
import os #Modo 1: Tamanho da tela
# import sys #Modo 3: 
from pygame.locals import * #Modo 3:


#Modo 1 (Janela): 
# Tamanho da tela
os.environ['SDL_VIDEO_CENTERED'] = '1' #Tem que ser antes do pygame.init()

pygame.init()

#Modo 1 (janela):
info = pygame.display.Info() #Tem que ser antes do .set_mode()
screen_width,screen_height = info.current_w,info.current_h
# window_width,window_height = screen_width,screen_height-45 #Para borda e titulo (-10,-50)
# screen = pygame.display.set_mode((window_width,window_height))

#Modo 2 (Tela cheia):
# Tamanho fixo, até tamanho da tela
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

#Modo 3:
#Maximizar e minimizar tela (Não fica proporcional)
# screen = pygame.display.set_mode((1000, 500), RESIZABLE)

#Proporção da pista pista 1:1 na tela 2:1 
if screen_height*2 < screen_width:
    pista_left = screen_width//2 - screen_height//2
    pista_right = screen_width//2 - screen_height//2
    pista_top = 0
    pista_botton = screen_height
else:
    pista_left = screen_width//4
    pista_right = 3*screen_width//4
    pista_top = 0
    pista_botton = screen_width//2
    

#Nome da Janela
pygame.display.set_caption('Corrida Espacial')

#Retangulo (x, y, width, height)
player = pygame.Rect((100,100,50,50))

pista = pygame.Rect((pista_left, pista_top, pista_right - pista_left, pista_botton - pista_top))

background = pygame.image.load("crew/assets/Fundo Espacial.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

asteroide = pygame.image.load('crew/assets/Asteroide.png')
asteroide_height = (pista_right - pista_left)/10
asteroide_width = 16*asteroide_height//18

asteroide_left = pista_left - asteroide_width
asteroide_top = 0
asteroide = pygame.transform.scale(asteroide, (asteroide_width, asteroide_height))

spacecraft = pygame.image.load('crew/assets/Spacecraft.png')
spacecraft_width = (pista_right - pista_left)/5
spacecraft_height = 900*spacecraft_width//720
spacecraft = pygame.transform.scale(spacecraft,(spacecraft_width, spacecraft_height))
spacecraft_left = pista_left

propulsor = pygame.image.load('crew/assets/propulsor.png')
propulsor_height = pista_botton/ 10
propulsor_width = 17*propulsor_height//45
propulsor = pygame.transform.scale(propulsor,(propulsor_width, propulsor_height))
propulsor_left = screen_width//2

bullet = pygame.image.load('crew/assets/bullet.png')
bullet_height = pista_botton/ 15
bullet_width = 12*propulsor_height//36
bullet = pygame.transform.scale(bullet,(bullet_width, bullet_height))
bullet_left = screen_width//2 - bullet_width*2

#Obs.: Canto superior esquerdo = (0,0)

run = True
while run:

    #Recarregar papel de parede, não deixabdo rastro
    #Completar((cor))
    screen.fill((0, 0,255))
    screen.blit(background, (0, 0))

    #Pista(Para ter noção de onde vai ser o jogo em si)
    pygame.draw.rect(screen, (0, 255, 255), pista)

    # #Asteroides
    while asteroide_top + asteroide_height < screen_height:
        screen.blit(asteroide, (asteroide_left, asteroide_top))
        screen.blit(asteroide, (asteroide_left + pista_right - pista_left + asteroide_height, asteroide_top))
        asteroide_top = asteroide_top + asteroide_height
    asteroide_top = 0

    screen.blit(spacecraft, (spacecraft_left,pista_botton - spacecraft_height))
    screen.blit(propulsor, (propulsor_left, propulsor_height))
    screen.blit(bullet, (bullet_left, bullet_height))

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
    #Quando apertar no ESC fechar
    if key[pygame.K_ESCAPE] == True:
        run = False
    #Atualizar
    pygame.display.update()

pygame.quit()