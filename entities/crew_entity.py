import pygame
import sys
from entities.initial_screen_entity import StartScreen


class Crew(object):
    def __init__(self):
        self.screen = None
        self.screen_size = None
        self.clock = None
        self.current_screen = None

    def init(self, screen_size=(800, 600)):
        pygame.init()

        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.current_screen = StartScreen(screen_size)

        pygame.display.set_caption('Crew')

        running = True
        while running:

            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                self.current_screen = self.current_screen.run(self.screen, self.screen_size, event)
