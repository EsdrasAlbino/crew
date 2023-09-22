import pygame

FONT = pygame.font.Font(None, 36)
ITEM_COLOR = (255, 255, 255)


class Item:
    def __init__(self, name, position):
        self.name = name
        self.image = pygame.Surface((30, 30))
        self.image.fill(ITEM_COLOR)
        self.rect = self.image.get_rect()
        self.position = position
        self.quantity = 1
        self.quantity_total = 1

    def draw(self, surface):
        x, y = self.position
        self.rect.topleft = (x, y)
        surface.blit(self.image, self.rect)
        quantity_text = FONT.render(
            f"{self.quantity}/{self.quantity_total}", True, (255, 255, 255))
        surface.blit(quantity_text, (x + 35, y+5))
