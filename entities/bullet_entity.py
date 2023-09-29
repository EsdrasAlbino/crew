import pygame
from entities.entity import Entity

BULLET_WIDTH = 5
BULLET_HEIGHT = 10
blue = (150, 200, 255)


class Bullet(Entity):
    def __init__(self, velocity, initial_position, direction):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, BULLET_WIDTH, BULLET_HEIGHT, initial_position)
        self.image.fill(blue)
        self.center = initial_position
        self.bullet = 3
        shot_sound = pygame.mixer.Sound("assets/shot.mp3")
        shot_sound.play()
        self.direction = (
            (direction[0] - initial_position[0], direction[1] - initial_position[1])
            if direction
            else (0, -1)
        )
        self.direction = [
            direct / ((self.direction[0] ** 2 + self.direction[1] ** 2) ** 0.5)
            for direct in self.direction
        ]
        self.direction = (self.direction[0], self.direction[1])

    def update(self):
        future_position = self.get_future_position(self.direction)

        if future_position[1] < -1:
            self.kill()
        else:
            self.position = future_position
