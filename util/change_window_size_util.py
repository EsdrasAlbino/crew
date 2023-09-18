import pygame

def change_size_window(screen, window_width, spacecraft_left, propellant_left, bullet_left, comet_left):
    window_width_before = window_width
    
    window_width, window_height = screen.get_size()

    proportion = window_width/window_width_before

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
    asteroid = pygame.transform.scale(asteroid, (asteroid_width, asteroid_height))

    spacecraft = pygame.image.load('assets/nave completa.png')
    spacecraft_width = (track_right - track_left)/5
    spacecraft_height = 31*spacecraft_width//45
    spacecraft = pygame.transform.scale(spacecraft,(spacecraft_width, spacecraft_height))
    spacecraft_left = spacecraft_left*proportion

    propellant = pygame.image.load('assets/propulsor.png')
    propellant_height = track_botton/ 10
    propellant_width = 320*propellant_height//580
    propellant = pygame.transform.scale(propellant,(propellant_width, propellant_height))
    propellant_left = propellant_left*proportion

    bullet = pygame.image.load('assets/bullet.png')
    bullet_height = track_botton/ 20
    bullet_width = 14*bullet_height//26
    bullet = pygame.transform.scale(bullet,(bullet_width, bullet_height))
    bullet_left = bullet_left*proportion

    comet = pygame.image.load('assets/comet.png')
    comet_height = track_botton//10
    comet_width = comet_height
    comet = pygame.transform.scale(comet,(comet_width, comet_height))
    comet = pygame.transform.rotozoom(comet, 45, 1)
    comet_left = comet_left*proportion

    return window_width, window_height, track_right, track_left, track_botton, track_top, background, asteroid, asteroid_width, asteroid_height, asteroid_left, spacecraft, spacecraft_width, spacecraft_height, spacecraft_left, propellant, propellant_height, propellant_width, propellant_left, bullet, bullet_height, bullet_width, bullet_left, comet, comet_height, comet_width, comet_left, track
