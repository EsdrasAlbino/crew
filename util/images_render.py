from paths import *
from pygame import *

IMG_NAMES = ['player',
             'laser', ]


IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}
