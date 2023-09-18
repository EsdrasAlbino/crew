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

    @property
    def position_y_obj1(self):
        return self.position_y_obj1
    
    @position_y_obj1.setter
    def position_y_obj1(self, position_y_obj1):
        self.position_y_obj1 = position_y_obj1
    
    @property
    def position_x_obj2(self):
        return self.position_x_obj2
    
    @position_x_obj2.setter
    def position_x_obj2(self, position_x_obj2):
        self.position_x_obj2 = position_x_obj2

    @property
    def position_y_obj2(self):
        return self.position_y_obj2    
        
    @position_y_obj2.setter
    def position_y_obj2(self, position_y_obj2):
        self.position_y_obj2 = position_y_obj2


    #Check for collision

    def check_for_collision(self):
        if self.position_x_obj1 == self.position_x_obj2 and self.position_y_obj1 == self.position_y_obj2:
            return True
        else:
            return False