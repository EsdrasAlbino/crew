import pygame
from util.change_window_size_util import change_window_size

GAME_TITLE = 'Crew'

class Crew(object):
    def __init__(self):
        self.screen = None
        self.clock = None

    def init(self):
        pygame.init()

        info = pygame.display.Info()  # Tem que ser antes do .set_mode()
        self.screen_dimensions = (info.current_w, info.current_h)

        self.screen = pygame.display.set_mode(
            (self.screen_dimensions[0] / 2, self.screen_dimensions[1] / 2), pygame.RESIZABLE
        )
        self.window_dimensions = self.screen.get_size()
        is_fullscreen = False

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(GAME_TITLE)

        if self.window_dimensions[1] * 2 < self.window_dimensions[0]:
            track_left_coord = self.window_dimensions[0] // 2 - self.window_dimensions[1] // 2
            track_right_coord = track_left_coord + self.window_dimensions[1]
            track_bottom_coord = self.window_dimensions[1]
        else:
            track_left_coord = self.window_dimensions[0] // 4
            track_right_coord = 3 * self.window_dimensions[0] // 4
            track_bottom_coord = self.window_dimensions[0] // 2
        track_coord = (track_left_coord, 0, track_right_coord, track_bottom_coord)
        player_left_coord = (track_right_coord - track_left_coord)//2
        player_top_coord = track_bottom_coord - (track_coord[2] - track_coord[0]) / 5
        propellant_left_coord = 0
        propellant_top_coord = 0
        bullet_left_coord = 0
        bullet_top_coord = 0
        comet_left_coord = 0
        comet_top_coord = 0

        is_running = True
        while is_running:
            (   track_coord,
                background,
                asteroid,
                asteroid_dimensions,
                asteroid_left_coord,
                player,
                player_dimensions,
                player_left_coord,
                player_top_coord,
                propellant,
                propellant_dimensions,
                propellant_left_coord,
                propellant_top_coord,
                bullet,
                bullet_dimensions,
                bullet_left_coord,
                bullet_top_coord,
                comet,
                comet_dimensions,
                comet_left_coord,
                comet_top_coord
            ) = change_window_size(
                self.screen,
                track_coord,
                player_left_coord,
                player_top_coord,
                propellant_left_coord,
                propellant_top_coord,
                bullet_left_coord,
                bullet_top_coord,
                comet_left_coord,
                comet_top_coord
            )

            self.screen.blit(background, (0, 0))

            asteroid_top_coord = 0
            while asteroid_top_coord < self.window_dimensions[1]:
                self.screen.blit(asteroid, (asteroid_left_coord, asteroid_top_coord))
                self.screen.blit(
                    asteroid,
                    (
                        asteroid_left_coord + track_coord[2] - track_coord[0] + asteroid_dimensions[1],
                        asteroid_top_coord,
                    ),
                )
                asteroid_top_coord = asteroid_top_coord + asteroid_dimensions[1]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    if not is_fullscreen:
                        self.screen = pygame.display.set_mode(
                            (self.screen_dimensions[0], self.screen_dimensions[1]), pygame.FULLSCREEN
                        )
                        is_fullscreen = True
                    else:
                        self.screen = pygame.display.set_mode(
                            (self.screen_dimensions[0] // 2, self.screen_dimensions[1] // 2),
                            pygame.RESIZABLE,
                        )
                        is_fullscreen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    is_running = False

            pygame.display.update()
        pygame.quit()
