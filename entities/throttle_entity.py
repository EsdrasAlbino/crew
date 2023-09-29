import pygame

from entities.entity import Entity

THROTTLE_WIDTH = 20
THROTTLE_HEIGHT = 50


class Throttle(Entity):
    def __init__(
        self, velocity, initial_position, player_group, player, screen_dimensions, track_bottom_coord
    ):

        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, THROTTLE_WIDTH, THROTTLE_HEIGHT, initial_position)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/propellant.png"),
            (THROTTLE_WIDTH, THROTTLE_HEIGHT),
        )
        self.center = initial_position
        self.__player_group = player_group
        self.__player = player
        self.screen_dimensions = screen_dimensions
        self.track_bottom_coord = track_bottom_coord

    def update(self):
        future_position = self.get_future_position((0, self.track_bottom_coord/1000))
        if future_position[1] > self.screen_dimensions[1]:
            self.kill()

        self.position = future_position

        if pygame.sprite.spritecollide(self, self.__player_group, False):
            self.kill()
            self.__player.infinite_ammo()
