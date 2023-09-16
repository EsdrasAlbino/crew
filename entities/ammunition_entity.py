import pygame
from pygame import *
from pygame.sprite import _Group

class Ammunition(pygame.sprite.Sprite):
    def __init__(self, *groups: _Group, position_x, position_y):
        super().__init__(*groups)
        self.postion_x = position_x
        self.position_y = position_y

    @property
    def position_x(self):
        return self.position_x
    
    @position_x.setter
    def position_x(self, position_x):
        self.position_x = position_x

    @property
    def position_y(self):
        return self.position_y
    
    @position_y.setter
    def position_y(self, position_y):
        self.position_y = position_y