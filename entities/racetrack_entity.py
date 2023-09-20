import pygame


class RaceTrack():
    def __init__(self, acceleration, max_speed, friction, player, screen):

        self.accelaration = accelaration
        self.spaceship = spaceship
        self.max_speed = max_speed
        self.friction = friction
        self.visible_colliders = []  # Storing colliders as Rect objects
        self.speed = INITIAL_SPEED # Initial speed

        self.screen = screen

    def get_visible_colliders(self):
        return self.visible_colliders

    def update_friction(self, new_friction):
        self.friction = new_friction
        return self.friction

    def get_speed(self):
        return self.speed

    def update_visible_colliders(self, new_colliders):
        self.visible_colliders = [
            collider for collider in new_colliders if 0 < collider.y < self.screen.get_height()]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed += self.accelaration
        elif keys[pygame.K_s]:
            self.speed -= self.accelaration
        self.speed *= self.friction

        # Apply friction
        self.speed *= self.friction

        # Limit the speed to the maximum
        self.speed = min(self.speed, self.max_speed)

        # Update the colliders' position based on speed
        actual_colliders = []
        for idx, collider in enumerate(self.visible_colliders):
            collider.y += self.speed
            if 0 <= collider.y <= self.screen.get_height():
                actual_colliders.append(collider)
        self.visible_colliders = actual_colliders

    def get_colliderect(self):
        """Checks a collision between spaceship (Player) and
        given rect in visible_colliders (pygame.Rect).
        Return the rect if a collision occured. Otherwise - None."""
        for collider in self.visible_colliders:
            if self.spaceship['rect'].colliderect(collider):
                return collider

        return None
