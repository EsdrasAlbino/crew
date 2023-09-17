import pygame
from pygame import *
import entities
from entities import *



class Colision:
    def __init__(self, position_x_obj1, position_y_obj1, position_x_obj2, position_y_obj2):
        self.position_x_obj1 = position_x_obj1
        self.position_y_obj1 = position_y_obj1
        self.position_x_obj2 = position_x_obj2
        self.position_y_obj2 = position_y_obj2

    @property
    def position_x_obj1(self):
        return self.position_x_obj1
    
    @position_x_obj1.setter
    def position_x_obj1(self, position_x_obj1):
        self.position_x_obj1 = position_x_obj1
    
        


