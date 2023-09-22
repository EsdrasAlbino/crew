<<<<<<< HEAD
from entities.crew_entity import Crew

=======
import os
from entities.crew_entity import Crew

os.environ['SDL_VIDEO_CENTERED'] = '1'

>>>>>>> 942759cc5f04e787dc38098aef25173ca4dbdcbe
if __name__ == '__main__':
    game = Crew()
    game.init()
