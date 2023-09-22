import pygame
from util.change_window_size_util import change_window_size
from util.update_coords import update_coords
from pygame.locals import *
from pygame.sprite import Group
import sys
from random import randint
from entities.asteroid_entity import Asteroid
from entities.bullet_entity import Bullets
from entities.throttle_entity import Throttle
from entities.player_entity import Spaceship

GAME_TITLE = "Crew"

class Crew(object):
    def __init__(self):
        self.screen = None
        self.clock = None

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
        return self.throttle_group
    @throttle_group.setter
    def throttle_group(self, throttle_group):
        self.throttle_group = throttle_group

    spaceship_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    throttle_group = pygame.sprite.Group()

    def init(self, screen_size=(800, 600)):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.fps = 60

        self.bg = pygame.image.load('assets/Fundo Espacial.jpg')

        self.screen = pygame.display.set_mode(screen_size)

        def draw_bg():
            self.screen.blit(self.bg, (0,0))

        #create player
        self.spaceship = Spaceship(int(screen_size[0] / 2), screen_size[1] - 100, self.bullet_group)
        self.spaceship_group.add(self.spaceship)

        #create asteroid
        self.asteroid = Asteroid(randint(0, screen_size[0]), 200, self.asteroid_group, self.bullet_group)
        self.asteroid_group.add(self.asteroid)

        #create throttle
        self.throttle = Throttle(400, 200, self.spaceship_group, self.spaceship)
        self.throttle_group.add(self.throttle)

        info = pygame.display.Info()  # Tem que ser antes do .set_mode()
        self.screen_dimensions = (info.current_w, info.current_h)

        self.screen = pygame.display.set_mode(
            (self.screen_dimensions[0] / 2, self.screen_dimensions[1] / 2),
            pygame.RESIZABLE,
        )
        self.window_dimensions = self.screen.get_size()
        is_fullscreen = False

        pygame.display.set_caption(GAME_TITLE)

        if self.window_dimensions[1] * 2 < self.window_dimensions[0]:
            track_left_coord = (
                self.window_dimensions[0] // 2 - self.window_dimensions[1] // 2
            )
            track_right_coord = track_left_coord + self.window_dimensions[1]
            track_bottom_coord = self.window_dimensions[1]
        else:
            track_left_coord = self.window_dimensions[0] // 4
            track_right_coord = 3 * self.window_dimensions[0] // 4
            track_bottom_coord = self.window_dimensions[0] // 2

        track_coords = (
            track_left_coord,
            0,
            track_right_coord,
            track_bottom_coord,
        )  # left, top, right, bottom

        player_coords = (
            (track_coords[2] - track_coords[0]) // 2,
            track_coords[1] - (track_coords[2] - track_coords[0]) / 5,
            None,
            None,
        )  # left, top, right, bottom

        propellant_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        bullet_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        comet_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        is_running = True
        while is_running:
            draw_bg()
            self.clock.tick(self.fps)

            #update player
            self.spaceship.update()

            #update groups
            self.asteroid_group.update()
            self.bullet_group.update()
            self.throttle_group.update()

            #draw sprite groups
            self.asteroid_group.draw(self.screen)
            self.spaceship_group.draw(self.screen)
            self.bullet_group.draw(self.screen)
            self.throttle_group.draw(self.screen)

            (   self.window_dimensions,
                track_coords,
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
                self.screen,
                track_coords,
                player_coords,
                propellant_coords,
                bullet_coords,
                comet_coords,
            )

            player_coords = update_coords(player_coords, player_new_coords)
            propellant_coords = update_coords(propellant_coords, propellant_new_coords)
            bullet_coords = update_coords(bullet_coords, bullet_new_coords)
            comet_coords = update_coords(comet_coords, comet_new_coords)

            asteroid_coords = (
                asteroid_left_coord,
                None,
                None,
                None,
            )  # left, top, right, bottom

            self.screen.blit(background, (0, 0))
            self.screen.blit(player, (player_coords[0], player_coords[1]))

            asteroid_coords = update_coords(asteroid_coords, (None, 0, None, None))
            while asteroid_coords[1] < self.window_dimensions[1]:
                self.screen.blit(asteroid, (asteroid_coords[0], asteroid_coords[1]))
                self.screen.blit(
                    asteroid,
                    (
                        asteroid_coords[0]
                        + track_coords[2]
                        - track_coords[0]
                        + asteroid_dimensions[1],
                        asteroid_coords[1],
                    ),
                )
                asteroid_coords = update_coords(
                    asteroid_coords,
                    (None, asteroid_coords[1] + asteroid_dimensions[1], None, None),
                )


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    if not is_fullscreen:
                        self.screen = pygame.display.set_mode(
                            (self.screen_dimensions[0], self.screen_dimensions[1]),
                            pygame.FULLSCREEN,
                        )
                        is_fullscreen = True
                    else:
                        self.screen = pygame.display.set_mode(
                            (
                                self.screen_dimensions[0] // 2,
                                self.screen_dimensions[1] // 2,
                            ),
                            pygame.RESIZABLE,
                        )
                        is_fullscreen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    is_running = False

            pygame.display.update()
        pygame.quit()
