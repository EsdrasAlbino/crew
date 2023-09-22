import pygame

class Throttle(pygame.sprite.Sprite):

    def __init__(self, x, y, spaceship_group, spaceship):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 50))
        self.image.fill((150, 255, 250))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.screen_width =  600
        self.screen_height = 800
        self.spaceship_group = spaceship_group
        self.spaceship = spaceship


    def update(self):
        #set movement speed
        speed = 3
        
        self.rect.y += speed

        if self.rect.top > self.screen_height:
            self.kill()
        
        if pygame.sprite.spritecollide(self, self.spaceship_group, False):
            self.kill()
            self.spaceship.cooldown /= 4