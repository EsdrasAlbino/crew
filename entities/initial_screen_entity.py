import pygame

class StartScreen(object):
    def __init__(self, screen_size):
        self.TEXT_COLOR = (255, 255, 255)
        self.BACKGROUND_COLOR = (0, 0, 0)
        self.FONT_SIZE = 48

        font = pygame.font.Font(None, self.FONT_SIZE)

        # Create text objects
        self.game_name = font.render("Crew", True, self.TEXT_COLOR)
        self.play_button = font.render("Play", True, self.TEXT_COLOR)
        self.credits_button = font.render("Credits", True, self.TEXT_COLOR)

        # Rectangles for buttons
        self.play_button_rect = self.play_button.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))
        self.credits_button_rect = self.credits_button.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2 + 100))

    def draw(self, screen,screen_size):
        screen.fill(self.BACKGROUND_COLOR)

        # Draw text and buttons
        screen.blit(self.game_name, self.game_name.get_rect(center=(screen_size[0] // 2, screen_size[1] // 4)))
        screen.blit(self.play_button, self.play_button_rect)
        screen.blit(self.credits_button, self.credits_button_rect)
        pygame.display.flip()
    
    def run(self,screen, screen_size, event):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        still_showing = True
        if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                still_showing = False
                print("Start the game!")
        elif self.credits_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                still_showing = False
                print("Show credits!")
        if still_showing:
            self.draw(screen, screen_size)
        return self
