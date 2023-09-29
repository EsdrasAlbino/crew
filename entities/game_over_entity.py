import pygame

TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FONT_SIZE = 32  # Decreased font size for credits
GAME_OVER_FONT_SIZE = 80  # Decreased font size for credits


class GameOverScreen(object):
    def __init__(self, screen_size, start_screen, game_screen):
        for item in game_screen.inventory.items:
            if item.name == 'asteroid':
                self.player_score = item.quantity
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.font_title = pygame.font.Font(None, GAME_OVER_FONT_SIZE)
        self.background = pygame.image.load("assets/background.jpg")
        self.background = pygame.transform.scale(self.background, screen_size)

        self.start_screen = start_screen
        self.game_screen = game_screen
        # Create text objects for the team members

        # Create a back button
        self._game_over = self.font_title.render("FIM DE JOGO", True, TEXT_COLOR)
        self._game_over_rect = self._game_over.get_rect(
            center=(int(screen_size[0] * 0.5), screen_size[1] * 0.4)
        )
        self._player_score = self.font.render(f"Pontuação: {self.player_score}", True, TEXT_COLOR)
        self._player_score_rect = self._player_score.get_rect(
            center=((screen_size[0] * 1.5) // 3, screen_size[1] * 0.5)
        )

        self._back_button = self.font.render("Voltar", True, TEXT_COLOR)
        self._back_button_rect = self._back_button.get_rect(
            center=(screen_size[0] // 3, screen_size[1] * 0.6)
        )
        self._play_button = self.font.render("Jogar novamente", True, TEXT_COLOR)
        self._play_button_rect = self._play_button.get_rect(
            center=((screen_size[0] * 1.75) // 3, screen_size[1] * 0.6)
        )

    def draw_borders(s, x, y, w, h, bw, c):
        pygame.draw.line(s, c, (x-bw//2+1, y), (x+w+bw//2, y), bw)
        pygame.draw.line(s, c, (x-bw//2+1, y+h), (x+w+bw//2, y+h), bw)
        pygame.draw.line(s, c, (x, y-bw//2+1), (x, y+h+bw//2), bw)
        pygame.draw.line(s, c, (x+w, y-bw//2+1), (x+w, y+h+bw//2), bw)

    def draw(self, screen, screen_size):
        self.background = pygame.transform.scale(self.background, screen_size)
        screen.blit(self.background, (0, 0))

        # Draw team member names
        self._back_button_rect = self._back_button.get_rect(
            center=(screen_size[0] // 3, screen_size[1] * 0.6)
        )
        self._game_over_rect = self._game_over.get_rect(
            center=(screen_size[0] // 2, screen_size[1] * 0.4)
        )
        self._play_button_rect = self._back_button.get_rect(
            center=((screen_size[0] * 1.75) // 3, screen_size[1] * 0.6)
        )
        self._player_score_rect = self._player_score.get_rect(
            center=((screen_size[0] * 1.5) // 3, screen_size[1] * 0.5)
        )


        screen.blit(self._player_score, self._player_score_rect)
        screen.blit(self._game_over, self._game_over_rect)
        screen.blit(self._back_button, self._back_button_rect)
        screen.blit(self._play_button, self._play_button_rect)
        pygame.display.flip()

    def run(self, screen, screen_size, event):
        if self._play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                self.game_screen.__reset__()
                return self.game_screen
        elif self._back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.start_screen
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        self.draw(screen, screen_size)
        return self
