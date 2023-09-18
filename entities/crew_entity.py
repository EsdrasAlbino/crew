import pygame
import sys


class Crew(object):
    def __init__(self):
        self.screen = None
        self.clock = None

    def init(self, screen_size=(800, 600)):
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Crew')

        running = True
        while running:

            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
