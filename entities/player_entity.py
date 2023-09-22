from typing import Tuple
import pygame

from entities.entity import Entity

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50


class Player(Entity):
    def __init__(self, velocity):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, PLAYER_WIDTH, PLAYER_HEIGHT, (0, 0))
