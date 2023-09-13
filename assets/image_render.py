from pygame import *
from os.path import abspath, dirname

BASE_PATH = abspath(dirname(__file__))
print(f"BASE_PATH:{BASE_PATH}",)
IMAGE_PATH = BASE_PATH+'\\'

IMG_NAMES = ['ship', 'mystery',
             'enemy1_1', 'enemy1_2',
             'enemy2_1', 'enemy2_2',
             'enemy3_1', 'enemy3_2',
             'explosionblue', 'explosiongreen', 'explosionpurple',
             'laser', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}
