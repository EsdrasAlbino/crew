import pygame

from entities.entity import Entity

THROTTLE_WIDTH = 20
THROTTLE_HEIGHT = 50

class Throttle(Entity):
    def __init__(
        self, velocity, initial_position, player_group, player, screen_dimensions
    ):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, THROTTLE_WIDTH, THROTTLE_HEIGHT, initial_position)
        self.image.fill((150, 255, 250))
        self.center = initial_position
        self.__player_group = player_group
        self.__player = player
        self.screen_dimensions = screen_dimensions


    def update(self):
        future_position = self.get_future_position((0, 1))
        if future_position[1] > self.screen_dimensions[1]:
            self.kill()

        self.position = future_position

        if pygame.sprite.spritecollide(self, self.__player_group, False):
            self.kill()
            self.new_cooldown = self.__player.cooldown / 4
            self.__player.cooldown = self.new_cooldown
