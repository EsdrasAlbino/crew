import pygame
from util.colors import WHITE
pygame.font.init()
FONT = pygame.font.Font(None, 36)


class Item:
    def __init__(self, name):
        self.name = name
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.quantity = 1
        self.quantity_total = 1

    def draw(self, surface, x, y):
        self.rect.topleft = (x, y)
        variation_position = 35

        surface.blit(self.image, self.rect)
        quantity_text = FONT.render(
            f"{self.quantity}/{self.quantity_total}", True, (255, 255, 255))

        surface.blit(
            quantity_text, (x + variation_position, y + variation_position))
