import pygame
from paths import IMAGE_PATH

IMG_NAMES = ['player',
             'laser', ]

IMAGES = {name: pygame.image.load(IMAGE_PATH + '{}.png'.format(name))
          for name in IMG_NAMES}
