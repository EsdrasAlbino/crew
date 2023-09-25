import pygame
from entities.initial_screen_entity import StartScreen

from util.change_window_size_util import update_window

GAME_TITLE = "Crew"

class Crew(object):

    def __init__(self):
        self.screen = None
        self.screen_size = None
        self.clock = None

    def init(self, screen_size=(800, 600)):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.fps = 60

        self.bg = pygame.image.load('assets/background.jpg')

        self.screen = pygame.display.set_mode(screen_size)

        def draw_bg():
            self.screen.blit(self.bg, (0,0))

        info = pygame.display.Info()  # Tem que ser antes do .set_mode()
        self.screen_dimensions = (info.current_w, info.current_h)

        self.screen = pygame.display.set_mode(
            (self.screen_dimensions[0] / 2, self.screen_dimensions[1] / 2),
            pygame.RESIZABLE,
        )
        self.window_dimensions = self.screen.get_size()
        is_fullscreen = False

        self.current_screen = StartScreen(self.window_dimensions)

        pygame.display.set_caption(GAME_TITLE)

        is_running = True
        while is_running:
            self.window_dimensions = update_window(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    if not is_fullscreen:
                        self.screen = pygame.display.set_mode(
                            (self.screen_dimensions[0],
                             self.screen_dimensions[1]),
                            pygame.FULLSCREEN,
                        )
                        is_fullscreen = True
                    else:
                        self.screen = pygame.display.set_mode(
                            (
                                self.screen_dimensions[0] // 2,
                                self.screen_dimensions[1] // 2,
                            ),
                            pygame.RESIZABLE,
                        )
                        is_fullscreen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    is_running = False
                self.current_screen = self.current_screen.run(
                    self.screen, self.window_dimensions, event)
