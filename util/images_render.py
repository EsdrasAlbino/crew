from pygame import *

IMG_NAMES = ['player',
             'laser', ]
IMAGE_PATH = "C:\Users\esdra\Documents\ip_crew\crew\images/"

IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}
