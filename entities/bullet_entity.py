import pygame
from entities.entity import Entity

BULLET_WIDTH = 5
BULLET_HEIGHT = 10
blue = (150, 200, 255)


class Bullet(Entity):
    def __init__(self, velocity, initial_position):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, BULLET_WIDTH, BULLET_HEIGHT, initial_position)
        self.image.fill(blue)
        self.center = initial_position

    def update(self):
        future_position = self.get_future_position((0, -1))

        if future_position[1] < -1:
            self.kill()
        else:
            self.position = future_position
