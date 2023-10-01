import pygame

class Life(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (100,3100/45))
        self.rect = self.image.get_rect(topleft=position)
        self.player_life = 0

    def update(self, screen):
        self.screen = screen
        self.screen_widht = self.screen.get_width()
        self.image = pygame.transform.scale(self.image, (self.screen_widht/25, 31*self.screen_widht/(25*45)))
        screen.blit(self.image, self.rect)
