from entities.player_entity import Player
from entities.throttle_entity import Throttle
from entities.bullet_entity import Bullets
from entities.asteroid_entity import Asteroid
from random import randint
from entities.initial_screen_entity import StartScreen
import pygame

from pygame.locals import *
from pygame.sprite import Group
from util.change_window_size_util import update_window

GAME_TITLE = "Crew"


class Crew(object):

    def __init__(self):
        self.screen = None
        self.screen_size = None
        self.clock = None
        self.current_screen = None

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

    def init(self):
        pygame.init()
        pygame.display.set_caption('Crew')

        info = pygame.display.Info()  # Tem que ser antes do .set_mode()
        self.screen_dimensions = (info.current_w, info.current_h)

        self.screen = pygame.display.set_mode(
            (self.screen_dimensions[0] / 2, self.screen_dimensions[1] / 2),
            pygame.RESIZABLE,
        )
        self.window_dimensions = self.screen.get_size()
        is_fullscreen = False

        self.clock = pygame.time.Clock()
        self.fps = 60

        def draw_bg():
            self.screen.fill((0, 0, 0))

        # create player
        self.spaceship = Player(
            int(self.screen_dimensions[0] / 2), self.screen_dimensions[1] - 100, self.bullet_group)
        self.spaceship_group.add(self.spaceship)

        # create asteroid
        self.asteroid = Asteroid(
            randint(0, self.screen_dimensions[0]), 100, self.asteroid_group, self.bullet_group)
        self.asteroid_group.add(self.asteroid)

        # create throttle
        self.throttle = Throttle(
            400, 200, self.spaceship_group, self.spaceship)
        self.throttle_group.add(self.throttle)
        self.current_screen = StartScreen(self.window_dimensions)

        running = True
        while running:

            draw_bg()
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    if not is_fullscreen:
                        self.screen = pygame.display.set_mode(
                            (self.screen_dimensions[0],
                             self.screen_dimensions[1]),
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
                self.current_screen = self.current_screen.run(
                    self.screen, self.window_dimensions, event)
