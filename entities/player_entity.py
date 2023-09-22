from typing import Tuple
import pygame
from entities.bullet_entity import Bullets
'''
from entities.entity import Entity

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50


class Player(Entity):
    def __init__(self, velocity):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, PLAYER_WIDTH, PLAYER_HEIGHT, (0, 0))
        '''


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/Nave completa.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks()  # Verify when the bullet was created
        self.cooldown = 500  # set cooldown for the bullets
        self.bullet_group = bullet_group

    def update(self):
        # set movement speed
        speed = 8

        # get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_d] and self.rect.right < 800:
            self.rect.x += speed

        time_now = pygame.time.get_ticks()

        if key[pygame.K_SPACE] and time_now - self.last_shot > self.cooldown and self.alive():
            bullet = Bullets(self.rect.centerx, self.rect.top)
            self.bullet_group.add(bullet)
            self.last_shot = time_now
