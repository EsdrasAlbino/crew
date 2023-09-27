import pygame
from util.colors import WHITE
from util.values_global import SIZE_IMAGE_ITEM, VARIATION_POSITION_TEXT_IN_ITEM
pygame.font.init()
FONT = pygame.font.Font(None, 36)


class Item:
    def __init__(self, name, quantity_item):
        self.name = name
        self.image = pygame.Surface(SIZE_IMAGE_ITEM)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.quantity = quantity_item
        if (name == 'bullet'):
            self.quantity_total = 20
        else:
            self.quantity_total = 3

    def draw(self, surface, position):
        self.rect.topleft = position
        variation_position = VARIATION_POSITION_TEXT_IN_ITEM

        surface.blit(self.image, self.rect)
        quantity_text = FONT.render(
            f"{self.quantity}/{self.quantity_total}", True, WHITE)

        surface.blit(
            quantity_text, (position[0] + variation_position, position[1] + variation_position))
