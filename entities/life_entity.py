import pygame
from util.images_render import IMAGES
from util.values_global import SIZE_IMAGE_ITEM


class Life(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGES['player']
        self.image = pygame.transform.scale(self.image, SIZE_IMAGE_ITEM)
        self.rect = self.image.get_rect(topleft=position)

    def update(self, *args):
        pygame.game.screen.blit(self.image, self.rect)
