from entities.player_entity import Player
from entities.throttle_entity import Throttle
from entities.bullet_entity import Bullets
from entities.asteroid_entity import Asteroid
from random import randint

from pygame.locals import *
from pygame.sprite import Group
import pygame
from util.change_window_size_util import change_window_size
from util.update_coords import update_coords


class Game(object):
    def __init__(self, window_dimensions):
        if window_dimensions[1] * 2 < window_dimensions[0]:
            self.track_left_coord = (
                window_dimensions[0] // 2 - window_dimensions[1] // 2
            )
            self.track_right_coord = self.track_left_coord + \
                window_dimensions[1]
            self.track_bottom_coord = window_dimensions[1]
        else:
            self.track_left_coord = window_dimensions[0] // 4
            self.track_right_coord = 3 * window_dimensions[0] // 4
            self.track_bottom_coord = window_dimensions[0] // 2

        self.track_coords = (
            self.track_left_coord,
            0,
            self.track_right_coord,
            self.track_bottom_coord,
        )  # left, top, right, bottom

        self.player_coords = (
            (self.track_coords[2] - self.track_coords[0]) // 2,
            self.track_coords[3] -
            (31 * ((self.track_coords[2] - self.track_coords[0]) / 5) // 45),
            None,
            None,
        )  # left, top, right, bottom

        self.propellant_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        self.bullet_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        self.comet_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

    @property
    def spaceship_group(self):
        return self.spaceship_group

    @spaceship_group.setter
    def spaceship_group(self, spaceship_group):
        self.spaceship_group = spaceship_group

    @property
    def asteroid_group(self):
        return self.asteroid_group

    @asteroid_group.setter
    def asteroid_group(self, asteroid_group):
        self.asteroid_group = asteroid_group

    @property
    def bullet_group(self):
        return self.bullet_group

    @bullet_group.setter
    def bullet_group(self, bullet_group):
        self.bullet_group = bullet_group

    @property
    def throttle_group(self):
        return self.throttle_groupz

    @throttle_group.setter
    def throttle_group(self, throttle_group):
        self.throttle_group = throttle_group

    spaceship_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    throttle_group = pygame.sprite.Group()

    def run(self, screen, window_dimensions, event):
        (window_dimensions,
         self.track_coords,
         background,
         asteroid,
         asteroid_dimensions,
         asteroid_left_coord,
         player,
         player_dimensions,
         player_new_coords,
         propellant,
         propellant_dimensions,
         propellant_new_coords,
         bullet,
         bullet_dimensions,
         bullet_new_coords,
         comet,
         comet_dimensions,
         comet_new_coords,
         ) = change_window_size(
            screen,
            self.track_coords,
            self.player_coords,
            self.propellant_coords,
            self.bullet_coords,
            self.comet_coords,
        )

        self.player_coords = (
            (self.track_coords[2] - self.track_coords[0]) // 2,
            self.track_coords[3] - player_dimensions[1],
            None,
            None,
        )  # left, top, right, bottom

        self.asteroid_coords = (
            asteroid_left_coord,
            None,
            None,
            None,
        )  # left, top, right, bottom

        self.player_coords = update_coords(
            self.player_coords, player_new_coords)
        self.propellant_coords = update_coords(
            self.propellant_coords, propellant_new_coords)
        self.bullet_coords = update_coords(
            self.bullet_coords, bullet_new_coords)
        self.comet_coords = update_coords(self.comet_coords, comet_new_coords)

        screen.blit(background, (0, 0))
        screen.blit(player, (self.player_coords[0], self.player_coords[1]))

        self.asteroid_coords = update_coords(
            self.asteroid_coords, (None, 0, None, None))
        while self.asteroid_coords[1] < window_dimensions[1]:
            screen.blit(
                asteroid, (self.asteroid_coords[0], self.asteroid_coords[1]))
            screen.blit(
                asteroid,
                (
                    self.asteroid_coords[0]
                    + self.track_coords[2]
                    - self.track_coords[0]
                    + asteroid_dimensions[1],
                    self.asteroid_coords[1],
                ),
            )
            self.asteroid_coords = update_coords(
                self.asteroid_coords,
                (None, self.asteroid_coords[1] +
                 asteroid_dimensions[1], None, None),
            )

        if window_dimensions[1] * 2 < window_dimensions[0]:
            self.track_left_coord = (
                window_dimensions[0] // 2 - window_dimensions[1] // 2
            )
            self.track_right_coord = self.track_left_coord + \
                window_dimensions[1]
            self.track_bottom_coord = window_dimensions[1]
        else:
            self.track_left_coord = window_dimensions[0] // 4
            self.track_right_coord = 3 * window_dimensions[0] // 4
            self.track_bottom_coord = window_dimensions[0] // 2
        pygame.display.flip()

        self.clock = pygame.time.Clock()
        self.fps = 60

        def draw_bg(screen):
            screen.fill((0, 0, 0))

        # create player
        self.spaceship = Player(
            int(window_dimensions[0] / 2), window_dimensions[1] - 100, self.bullet_group)
        self.spaceship_group.add(self.spaceship)

        # create asteroid
        self.asteroid = Asteroid(
            randint(0, window_dimensions[0]), 200, self.asteroid_group, self.bullet_group)
        self.asteroid_group.add(self.asteroid)

        # create throttle
        self.throttle = Throttle(
            400, 200, self.spaceship_group, self.spaceship)
        self.throttle_group.add(self.throttle)

        draw_bg(screen)
        self.clock.tick(self.fps)

        return self
