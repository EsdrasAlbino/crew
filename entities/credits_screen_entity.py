import pygame

TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FONT_SIZE = 32  # Decreased font size for credits

class CreditsScreen(object):
    def __init__(self, screen_size, start_screen):
        self.font = pygame.font.Font(None, FONT_SIZE )
        self.start_screen = start_screen
        # Create text objects for the team members
        self.team_names = [
            "Matheus Borges",
            "Welton Felix",
            "Maria Fernanda",
            "Esdras Albino",
            "Tulio Araujo",
        ]
        self.professor_name = ["Filipe Calegario", "Sérgio Sacanni", "Ricardo Massa"]

        # Create a back button
        self._back_button = self.font.render("Back", True, TEXT_COLOR)
        self._back_button_rect = self._back_button.get_rect(center=(screen_size[0] * 0.8 , screen_size[1] * 0.9))

    def draw(self, screen, screen_size):
        screen.fill(BACKGROUND_COLOR)

        # Draw team member names
        self._back_button_rect = self._back_button.get_rect(center=(screen_size[0] * 0.8 , screen_size[1] * 0.9))
        y_position = screen_size[1] // 4
        text = self.font.render("Time de programação", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(screen_size[0] // 3, screen_size[1] * 0.1))
        screen.blit(text, text_rect)
        for name in self.team_names:
            text = self.font.render(name, True, TEXT_COLOR)
            text_rect = text.get_rect(center=(screen_size[0] // 3, y_position))
            screen.blit(text, text_rect)
            y_position += 50  # Adjust vertical spacing

        y_position = screen_size[1] // 4
        text = self.font.render("Professores responsáveis", True, TEXT_COLOR)
        text_rect = text.get_rect(center=((screen_size[0] * 2) // 3, screen_size[1] * 0.1))
        screen.blit(text, text_rect)
        for name in self.professor_name:
            text = self.font.render(name, True, TEXT_COLOR)
            text_rect = text.get_rect(center=((screen_size[0] * 2) // 3, y_position))
            screen.blit(text, text_rect)
            y_position += 50  # Adjust vertical spacing

        # Draw the back button
        screen.blit(self._back_button, self._back_button_rect)
        pygame.display.flip()

    def run(self, screen, screen_size, event):

        if self._back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.start_screen
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        self.draw(screen, screen_size)
        return self  # Stay on the credits screen
