import os
from entities.crew_entity import Crew

os.environ['SDL_VIDEO_CENTERED'] = '1'

if __name__ == '__main__':
    game = Crew()
    game.init()
