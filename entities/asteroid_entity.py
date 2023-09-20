import pygame
from pygame import *
from pygame.sprite import _Group
import util.collision

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((150, 200, 0))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.screen_width =  600
        self.screen_height = 800
        self.spaceship_group = util.collision.spaceship_group
        self.bullet_group = util.collision.bullet_group
        

    def update(self):
        #set movement speed
        speed = 3
        
        self.rect.y += speed

        if self.rect.top > self.screen_height:
            self.kill()
        
        if pygame.sprite.spritecollide(self, self.spaceship_group, False):
            self.kill()
        if pygame.sprite.spritecollide(self, self.bullet_group, True):
            self.kill()