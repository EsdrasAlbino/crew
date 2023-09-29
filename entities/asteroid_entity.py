import pygame
from entities.entity import Entity

ASTEROID_WIDTH = 50
ASTEROID_HEIGHT = 50


class Asteroid(Entity):
    def __init__(
        self, velocity, initial_position, player_group, bullet_group, screen_dimensions, track_bottom_coord, comet_dimensions, comet_new_coord
    ):
        ASTEROID_WIDTH, ASTEROID_HEIGHT = comet_dimensions
        
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, ASTEROID_WIDTH, ASTEROID_HEIGHT, initial_position)

        self.image = pygame.transform.scale(
                pygame.image.load(
                    "assets/comet.png"), (ASTEROID_WIDTH, ASTEROID_HEIGHT)
                )
            
        self.rect = self.image.get_rect()
        self.rect.center = initial_position

        self.__player_group = player_group
        self.__bullet_group = bullet_group
        self.__screen_dimensions = screen_dimensions
        self.track_bottom_coord = track_bottom_coord

    def update(self):
        future_position = self.get_future_position(
            (0, self.track_bottom_coord/1000))

        if future_position[1] > self.__screen_dimensions[1]:
            self.kill()

        self.position = future_position

        if pygame.sprite.spritecollide(self, self.__player_group, False):
            self.kill()
            self.__player_group.sprites()[0].player_damage()

        if pygame.sprite.spritecollide(self, self.__bullet_group, True):
            self.kill()
            self.__player_group.sprites()[0].asteroid_destroy += 1
