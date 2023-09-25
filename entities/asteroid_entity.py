import pygame
from entities.entity import Entity

ASTEROID_WIDTH = 50
ASTEROID_HEIGHT = 50


class Asteroid(Entity):
    def __init__(
        self, velocity, initial_position, player_group, bullet_group, screen_dimensions
    ):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, ASTEROID_WIDTH, ASTEROID_HEIGHT, initial_position)

        self.image.fill((150, 200, 0))
        self.center = initial_position

        self.__player_group = player_group
        self.__bullet_group = bullet_group
        self.__screen_dimensions = screen_dimensions

    def update(self):
        future_position = self.get_future_position((0, 1))

        if future_position[1] > self.__screen_dimensions[1]:
            self.kill()

        self.position = future_position

        if pygame.sprite.spritecollide(self, self.__player_group, False):
            self.kill()
        if pygame.sprite.spritecollide(self, self.__bullet_group, True):
            self.kill()

