import pygame

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50


class Player(pygame.sprite.Sprite):
    def __init__(self, velocity):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.velocity = velocity

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self._pos_y
        self.rect.width = PLAYER_WIDTH
        self.rect.height = PLAYER_HEIGHT

    def move(self, x, y):
        self.pos_x += x * self.velocity
        self._pos_y += y * self.velocity
        self.update()
