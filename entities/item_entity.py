import pygame
from util.colors import WHITE

pygame.font.init()
FONT = pygame.font.Font(None, 36)


class Item:
    def __init__(self, name, quantity_item, path_image, item_dimensions):
        self.name = name
        self.item_dimensions = item_dimensions
        self.image = pygame.image.load(path_image)
        self.image = pygame.transform.scale(self.image, (self.item_dimensions))
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.quantity = quantity_item
        self.quantity_total = 20

    def draw(self, surface, position):
        self.rect.topleft = position
        FONT = pygame.font.Font(None, int(self.item_dimensions[1]))
        surface.blit(self.image, self.rect)
        if self.name == "bullet":
            quantity_text = FONT.render(
                f"{self.quantity}/{self.quantity_total}", True, WHITE
            )
        elif self.name == "propellant":
            quantity_text = FONT.render(f"{self.quantity}s", True, WHITE)
        else:
            quantity_text = FONT.render(f"{self.quantity}", True, WHITE)

        surface.blit(
            quantity_text,
            (position[0] + self.item_dimensions[0]*3/2, position[1] + self.item_dimensions[1]/3),
        )
