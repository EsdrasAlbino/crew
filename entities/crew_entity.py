import pygame
from util.change_window_size_util import change_size_window


class Crew(object):
    def __init__(self):
        self.screen = None
        self.clock = None

    def init(self):
        pygame.init()

        info = pygame.display.Info() #Tem que ser antes do .set_mode()
        self.screen_width, self.screen_height = info.current_w,info.current_h

        self.screen = pygame.display.set_mode((self.screen_width/2, self.screen_height/2), pygame.RESIZABLE)
        self.window_width, self.window_height = self.screen.get_size()
        self.fullscreen = False

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Crew')

        if self.window_height*2 < self.window_width:
            track_left = self.window_width//2 - self.window_height//2
            track_right = track_left + self.window_height
            track_top = 0
            track_botton = self.window_height
        else:
            track_left = self.window_width//4
            track_right = 3*self.window_width//4
            track_top = 0
            track_botton = self.window_width//2
            
        track = pygame.Rect((track_left, track_top, track_right - track_left, track_botton - track_top))

        background = pygame.image.load('assets/Fundo Espacial.jpg')
        background = pygame.transform.scale(background, (self.window_width, self.window_height))

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
        propellant_left = self.window_width//2

        bullet = pygame.image.load('assets/bullet.png')
        bullet_height = track_botton/ 20
        bullet_width = 14*bullet_height//26
        bullet = pygame.transform.scale(bullet,(bullet_width, bullet_height))
        bullet_left = self.window_width//2 - bullet_width*2

        comet = pygame.image.load('assets/comet.png')
        comet_height = track_botton//10
        comet_width = comet_height
        comet = pygame.transform.scale(comet,(comet_width, comet_height))
        comet = pygame.transform.rotozoom(comet, 45, 1)
        comet_left = self.window_width//2 - comet_width*3

        running = True
        while running:
            self.window_width, self.window_height, track_right, track_left, track_botton, track_top, background, asteroid, asteroid_width, asteroid_height, asteroid_left, spacecraft, spacecraft_width, spacecraft_height, spacecraft_left, propellant, propellant_height, propellant_width, propellant_left, bullet, bullet_height, bullet_width, bullet_left, comet, comet_height, comet_width, comet_left, track = change_size_window(self.screen, self.window_width, spacecraft_left, propellant_left, bullet_left, comet_left)

            self.screen.blit(background, (0, 0))

            while asteroid_top < self.window_height:
                self.screen.blit(asteroid, (asteroid_left, asteroid_top))
                self.screen.blit(asteroid, (asteroid_left + track_right - track_left + asteroid_height, asteroid_top))
                asteroid_top = asteroid_top + asteroid_height
            asteroid_top = 0

            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    if not self.fullscreen:
                        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
                        self.fullscreen = True
                    else:
                        self.screen = pygame.display.set_mode((self.screen_width//2, self.screen_height//2), pygame.RESIZABLE)
                        self.fullscreen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            pygame.display.update()
        pygame.quit()
