import pygame
from abc import ABC, abstractmethod
from typing import Tuple


class Entity(ABC, pygame.sprite.Sprite):
    @abstractmethod
    def __init__(self, velocity, width, height, position):
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.velocity = velocity
        self.__width = width
        self.__height = height
        self.__position = position

    def __entity_update(self):
        self.rect.x = self.__position[0]
        self.rect.y = self.__position[1]
        self.rect.width = self.__width
        self.rect.height = self.__height

    def get_future_position(self, steps: Tuple[float, float]):
        x_steps = steps[0]
        y_steps = steps[1]

        future_x = self.__position[0]
        future_y = self.__position[1]

        if x_steps is not None:
            future_x = self.__position[0] + x_steps * self.velocity
        if y_steps is not None:
            future_y = self.__position[1] + y_steps * self.velocity

        return (future_x, future_y)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position: Tuple[float, float]):
        self.__position = (new_position[0], new_position[1])
        self.__entity_update()

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width: float):
        self.__width = new_width
        self.__entity_update()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height: float):
        self.__height = new_height
        self.__entity_update()

    @property
    def center(self):
        return self.rect.center

    @center.setter
    def center(self, new_center: Tuple[float, float]):
        self.rect.center = new_center

    def check_collision(self, other):
        return self.rect.colliderect(other.rect)
