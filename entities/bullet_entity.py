import pygame

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 10))
        self.image.fill((150, 200, 255))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #set movement speed
        speed = 5

        self.rect.y -= speed

        if self.rect.bottom < 0:
            self.kill()   
