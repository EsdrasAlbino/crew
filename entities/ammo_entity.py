import pygame

from entities.entity import Entity

AMMO_WIDTH = 10
AMMO_HEIGHT = 25


class Ammo(Entity):
    def __init__(
        self, velocity, initial_position, player_group, player, screen_dimensions
    ):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, AMMO_WIDTH, AMMO_HEIGHT, initial_position)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/bullet.png"),
            (AMMO_WIDTH, AMMO_HEIGHT),
        )
        self.center = initial_position
        self.__player_group = player_group
        self.__player = player
        self.screen_dimensions = screen_dimensions
        self.new_cooldown = self.__player.cooldown / 4

    def update(self):
        future_position = self.get_future_position((0, 1))
        if future_position[1] > self.screen_dimensions[1]:
            self.kill()

        self.position = future_position

        if pygame.sprite.spritecollide(self, self.__player_group, False):
            self.kill()
            # self.__player.decrease_cooldown()
