import pygame
from util.colors import WHITE, BLACK
from entities.credits_screen_entity import CreditsScreen

from entities.game_entity import Game

TEXT_COLOR = WHITE
BACKGROUND_COLOR = BLACK
FONT_SIZE = 48


class StartScreen(object):
    def __init__(self, screen_size, screen_dimensions):
        title_font = pygame.font.Font(None, FONT_SIZE * 2)
        font = pygame.font.Font(None, FONT_SIZE)
        self.background = pygame.image.load("assets/background.jpg")
        self.background = pygame.transform.scale(self.background, screen_size)
        self.screen_dimensions =screen_dimensions

        # Create text objects
        self._game_name = title_font.render("CREW", True, TEXT_COLOR)
        self._play_button = font.render("Jogar", True, TEXT_COLOR)
        self._credits_button = font.render("Créditos", True, TEXT_COLOR)

        # Rectangles for buttons
        self._play_button_rect = self._play_button.get_rect(
            center=(screen_size[0] // 2, screen_size[1] // 2)
        )
        self._credits_button_rect = self._credits_button.get_rect(
            center=(screen_size[0] // 2, screen_size[1] // 2 + 100)
        )

    def draw(self, screen, screen_size):
        screen.fill(BACKGROUND_COLOR)
        self.background = pygame.transform.scale(self.background, screen_size)
        screen.blit(self.background, (0, 0))

        # Draw text and buttons
        screen.blit(
            self._game_name,
            self._game_name.get_rect(center=(screen_size[0] // 2, screen_size[1] // 4)),
        )
        screen.blit(self._play_button, self._play_button_rect)
        screen.blit(self._credits_button, self._credits_button_rect)
        pygame.display.flip()

    def run(self, screen, screen_size, event):
        is_visible = True
        if self._play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_visible = False
                game = Game(screen_size, self.screen_dimensions)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                return game
        elif self._credits_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_visible = False
                credits_screen = CreditsScreen(screen_size, self)
                return credits_screen
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        if is_visible:
            self._play_button_rect = self._play_button.get_rect(
                center=(screen_size[0] // 2, screen_size[1] // 2)
            )
            self._credits_button_rect = self._credits_button.get_rect(
                center=(screen_size[0] // 2, screen_size[1] // 2 + 100)
            )

            self.draw(screen, screen_size)
        return self
