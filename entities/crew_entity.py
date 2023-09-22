import pygame
from pygame.locals import *
from pygame.sprite import Group
import sys
from random import randint
from entities.asteroid_entity import Asteroid
from entities.bullet_entity import Bullets
from entities.throttle_entity import Throttle
from entities.player_entity import Spaceship

class Crew(object):
    
    def __init__(self):
        self.screen = None
        self.clock = None
    
    @property
    def spaceship_group(self):
        return self.spaceship_group
    @spaceship_group.setter
    def spaceship_group(self, spaceship_group):
        self.spaceship_group = spaceship_group
    @property
    def asteroid_group(self):
        return self.asteroid_group
    @asteroid_group.setter
    def asteroid_group(self, asteroid_group):
        self.asteroid_group = asteroid_group
    @property
    def bullet_group(self):
        return self.bullet_group
    @bullet_group.setter
    def bullet_group(self, bullet_group):
        self.bullet_group = bullet_group
    @property
    def throttle_group(self):
        return self.throttle_groupz
    @throttle_group.setter
    def throttle_group(self, throttle_group):
        self.throttle_group = throttle_group

    spaceship_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    throttle_group = pygame.sprite.Group()

    def init(self, screen_size=(800, 600)):
        pygame.init()
        pygame.display.set_caption('Crew')
        self.bg = pygame.image.load('assets/Fundo Espacial.jpg')
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.fps = 60


        def draw_bg():
           #self.screen.fill((0, 0, 0))
           self.screen.blit(self.bg, (0, 0))

        #create player
        self.spaceship = Spaceship(int(screen_size[0] / 2), screen_size[1] - 100, self.bullet_group)
        self.spaceship_group.add(self.spaceship)

        #create asteroid
        self.asteroid = Asteroid(randint(0, screen_size[0]), 200, self.asteroid_group, self.bullet_group)
        self.asteroid_group.add(self.asteroid)

        #create throttle
        self.throttle = Throttle(400, 200, self.spaceship_group, self.spaceship)
        self.throttle_group.add(self.throttle)

        running = True
        while running:

            draw_bg()
            self.clock.tick(self.fps)

            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

            #update player
            self.spaceship.update()

            #update groups
            self.asteroid_group.update()
            self.bullet_group.update()
            self.throttle_group.update()

            #draw sprite groups
            self.asteroid_group.draw(self.screen)
            self.spaceship_group.draw(self.screen)
            self.bullet_group.draw(self.screen)
            self.throttle_group.draw(self.screen)
            
            pygame.display.update() 

        pygame.quit()
