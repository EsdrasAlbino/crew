import sys
from entities.ammo_entity import Ammo

from entities.player_entity import Player
from entities.throttle_entity import Throttle
from entities.bullet_entity import Bullet
from entities.asteroid_entity import Asteroid, ASTEROID_WIDTH
from random import randint
from entities.item_entity import Item
from entities.inventory_entity import Inventory
from entities.life_entity import Life

from pygame.locals import *
from pygame.sprite import Group
import pygame
from util.change_window_size_util import change_window_size
from util.update_coords import update_coords
from entities.game_over_entity import GameOverScreen


class Game(object):
    def __init__(self, window_dimensions, start_screen):
        self.start_screen = start_screen
        self.soundtrack = pygame.mixer.Sound("assets/theme.mp3")
        self.soundtrack.play(-1, 0, 1000)
        self.window_dimensions = window_dimensions
        if self.window_dimensions[1] * 2 < self.window_dimensions[0]:
            self.track_left_coord = (
                self.window_dimensions[0] // 2 - self.window_dimensions[1] // 2
            )
            self.track_right_coord = self.track_left_coord + self.window_dimensions[1]
            self.track_bottom_coord = self.window_dimensions[1]
        else:
            self.track_left_coord = self.window_dimensions[0] // 4
            self.track_right_coord = 3 * self.window_dimensions[0] // 4
            self.track_bottom_coord = self.window_dimensions[0] // 2

        self.track_coords = (
            self.track_left_coord,
            0,
            self.track_right_coord,
            self.track_bottom_coord,
        )  # left, top, right, bottom

        self.player_coords = (
            (self.track_coords[2] - self.track_coords[0]) // 2,
            self.track_coords[3]
            - (31 * ((self.track_coords[2] - self.track_coords[0]) / 5) // 45),
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

        self.ammo_coords = (
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

        # create life
        self.lives = [Life((10, 30)), Life((50, 30)), Life((90, 30))]

        self.player_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.ammo_group = pygame.sprite.Group()
        self.throttle_group = pygame.sprite.Group()
        self.livesGroup = pygame.sprite.Group()

        self.player = Player(
            10,
            (
                self.window_dimensions[0] // 2,
                self.window_dimensions[1],
            ),
            self.bullet_group,
            (self.track_left_coord, self.track_right_coord - ASTEROID_WIDTH / 1.5),
        )
        self.player_group.add(self.player)

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.is_fullscreen = False

    def __reset__(self):
        self.track_coords = (
            self.track_left_coord,
            0,
            self.track_right_coord,
            self.track_bottom_coord,
        )  # left, top, right, bottom

        self.player_coords = (
            (self.track_coords[2] - self.track_coords[0]) // 2,
            self.track_coords[3]
            - (31 * ((self.track_coords[2] - self.track_coords[0]) / 5) // 45),
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

        self.ammo_coords = (
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
        # create life
        self.lives = [Life((10, 30)), Life((50, 30)), Life((90, 30))]

        self.player_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.ammo_group = pygame.sprite.Group()
        self.throttle_group = pygame.sprite.Group()
        self.livesGroup = pygame.sprite.Group()

        self.player = Player(
            10,
            (
                self.window_dimensions[0] // 2,
                self.window_dimensions[1],
            ),
            self.bullet_group,
            (self.track_left_coord, self.track_right_coord),
        )
        self.player_group.add(self.player)
        self.soundtrack.play(-1, 0, 1000)

    def __update_coords(self):
        self.player.position = (self.player.position[0], self.player_coords[1])

    # def check_collisions(self):

    def run(self, screen, screen_size, event):
        if self.player.life <= 0:
            self.soundtrack.stop()
            return GameOverScreen(screen_size, self.start_screen, self)

        self.livesGroup.empty()

        for i in range(self.player.life):
            self.livesGroup.add(self.lives[i])

        self.screen = screen
        (
            self.window_dimensions,
            self.track_coords,
            background,
            asteroid,
            asteroid_dimensions,
            asteroid_left_coord,
            player_dimensions,
            player_new_coords,
            propellant_dimensions,
            propellant_new_coords,
            bullet_dimensions,
            bullet_new_coords,
            comet_dimensions,
            comet_new_coords,
        ) = change_window_size(
            self.screen,
            self.track_coords,
            self.player_coords,
            self.propellant_coords,
            self.bullet_coords,
            self.comet_coords,
        )

        self.asteroid_coords = (
            asteroid_left_coord,
            None,
            None,
            None,
        )  # left, top, right, bottom

        self.player_coords = update_coords(self.player_coords, player_new_coords)
        self.propellant_coords = update_coords(
            self.propellant_coords, propellant_new_coords
        )
        self.bullet_coords = update_coords(self.bullet_coords, bullet_new_coords)
        self.comet_coords = update_coords(self.comet_coords, comet_new_coords)

        self.__update_coords()
        self.player.boundaries = (
            self.track_left_coord,
            self.track_right_coord - asteroid_dimensions[0],
        )
        self.screen.blit(background, (0, 0))

        self.asteroid_coords = update_coords(
            self.asteroid_coords, (None, 0, None, None)
        )

        self.screen.fill((0, 0, 0))
        self.clock.tick(self.fps)
        self.screen.blit(background, (0, 0))

        # create inventory
        self.inventory = Inventory()

        # item1 = Item("asteroid", 1)
        bullet_item = Item("bullet", self.player.bullet_quantity, "assets/bullet.png")
        propellant_item = Item(
            "propellant", self.player.propellant_condition, "assets/propellant.png"
        )
        asteroid_item = Item(
            "asteroid", self.player.asteroid_destroy, "assets/asteroid.png"
        )
        for item in [bullet_item, propellant_item, asteroid_item]:
            self.inventory.add_item(item)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            if not self.is_fullscreen:
                infoObject = pygame.display.Info()
                self.screen = pygame.display.set_mode(
                    (infoObject.current_w, infoObject.current_h),
                    pygame.FULLSCREEN,
                )
                self.is_fullscreen = True
            else:
                self.screen = pygame.display.set_mode(
                    (
                        self.window_dimensions[0] // 2,
                        self.window_dimensions[1] // 2,
                    ),
                    pygame.RESIZABLE,
                )
                self.is_fullscreen = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return self
        if self.asteroid_group.__len__() < 2:
            seed = randint(0, 200)
            if seed > 40 and seed < 45:
                enemy = Asteroid(
                    5,
                    (
                        randint(
                            self.track_left_coord,
                            self.track_right_coord - int(ASTEROID_WIDTH / 1.5),
                        ),
                        0,
                    ),
                    self.player_group,
                    self.bullet_group,
                    self.window_dimensions,
                    self.track_bottom_coord,
                )
                self.asteroid_group.add(enemy)

        for _asteroid in self.asteroid_group.sprites():
            _asteroid.width = comet_dimensions[0]
            _asteroid.height = comet_dimensions[1]
        for _player in self.player_group.sprites():
            _player.width = player_dimensions[0]
            _player.height = player_dimensions[1]
        for _ammo in self.ammo_group.sprites():
            _ammo.width = bullet_dimensions[0]
            _ammo.height = bullet_dimensions[1]
        for _throttle in self.throttle_group.sprites():
            _throttle.width = propellant_dimensions[0]
            _throttle.height = propellant_dimensions[1]
        for _bullet in self.bullet_group.sprites():
            _bullet.width = (self.track_right_coord - self.track_left_coord) / 100
            _bullet.height = (self.track_right_coord - self.track_left_coord) / 50

        if self.throttle_group.__len__() < 1:
            seed = randint(0, 200)
            if seed == 50:
                throttle = Throttle(
                    3,
                    (
                        randint(
                            self.track_left_coord,
                            self.track_right_coord - int(ASTEROID_WIDTH / 1.5),
                        ),
                        0,
                    ),
                    self.player_group,
                    self.player,
                    self.window_dimensions,
                    self.track_bottom_coord,
                )
                self.throttle_group.add(throttle)

        if self.ammo_group.__len__() < 1:
            seed = randint(0, 200)
            if 25 < seed < 30:
                ammo = Ammo(
                    3,
                    (
                        randint(
                            self.track_left_coord,
                            self.track_right_coord - int(ASTEROID_WIDTH / 1.5),
                        ),
                        0,
                    ),
                    self.player_group,
                    self.player,
                    self.window_dimensions,
                    self.track_bottom_coord,
                )
                self.ammo_group.add(ammo)

        # update player
        self.player.update()

        # update groups
        self.asteroid_group.update()
        self.bullet_group.update()
        self.ammo_group.update()
        self.throttle_group.update()
        self.livesGroup.update(self.screen)

        # draw sprite groups
        self.asteroid_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.ammo_group.draw(self.screen)
        self.throttle_group.draw(self.screen)
        self.livesGroup.draw(self.screen)

        self.inventory.draw(self.screen)

        while self.asteroid_coords[1] < self.window_dimensions[1]:
            self.screen.blit(
                asteroid, (self.asteroid_coords[0], self.asteroid_coords[1])
            )
            self.screen.blit(
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
                (
                    None,
                    self.asteroid_coords[1] + asteroid_dimensions[1],
                    None,
                    None,
                ),
            )

        if self.window_dimensions[1] * 2 < self.window_dimensions[0]:
            self.track_left_coord = (
                self.window_dimensions[0] // 2 - self.window_dimensions[1] // 2
            )
            self.track_right_coord = self.track_left_coord + self.window_dimensions[1]
            self.track_bottom_coord = self.window_dimensions[1]
        else:
            self.track_left_coord = self.window_dimensions[0] // 4
            self.track_right_coord = 3 * self.window_dimensions[0] // 4
            self.track_bottom_coord = self.window_dimensions[0] // 2

        pygame.display.update()

        return self
