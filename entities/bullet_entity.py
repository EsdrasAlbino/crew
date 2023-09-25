import pygame
<<<<<<< HEAD
from util.images_render import IMAGES


class Bullet(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, direction, speed, filename, side):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGES[filename]
        self.rect = self.image.get_rect(topleft=(xpos, ypos))
        self.speed = speed
        self.direction = direction
        self.side = side
        self.filename = filename

    def update(self, keys, *args):
        pygame.game.screen.blit(self.image, self.rect)
        self.rect.y += self.speed * self.direction
        if self.rect.y < 15 or self.rect.y > 600:
=======
from entities.entity import Entity

BULLET_WIDTH = 5
BULLET_HEIGHT = 10
blue = (150, 200, 255)

class Bullet(Entity):
    def __init__(self, velocity, initial_position):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, BULLET_WIDTH, BULLET_HEIGHT, initial_position)
        self.image.fill(blue)
        self.center = initial_position

    def update(self):
        future_position = self.get_future_position((0, -1))

        if future_position[1] < -1:
>>>>>>> 1acf6a49a30bbacf72ea83cbaf712b2fc82695ca
            self.kill()
        else:
            self.position = future_position
