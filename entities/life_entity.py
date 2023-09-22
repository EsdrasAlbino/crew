import pygame
from util.images_render import IMAGES


class Life(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGES['player']
        self.image = pygame.transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

#    def update(self, *args):
#        pygame.game.screen.blit(self.image, self.rect)
