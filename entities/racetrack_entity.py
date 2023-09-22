import pygame


class RaceTrack():
    def __init__(self, acceleration, max_speed, friction, player, screen):
        self._acceleration = acceleration

        self._player = player
        self._max_speed = max_speed
        self._friction = friction
        self._visible_colliders = []  # Storing colliders as Rect objects
        self._speed = INITIAL_SPEED # Initial speed

        self._screen = screen

    @property
    def collision_rect(self):
        for collider in self.visible_colliders:
            if self.player['rect'].colliderect(collider):
                return collider
        return None

    @property
    def friction(self):
        return self._friction
    
    @friction.setter
    def friction(self, value):
        self._friction = value if value < 1 else 1

    @property
    def player(self):
        return self._player
    
    @property
    def visible_colliders(self):
        return self._visible_colliders
    
    @visible_colliders.setter
    def visible_colliders(self, value):
        self._visible_colliders = [
            collider for collider in value if 0 < collider.y < self._screen.get_height()]

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = value if value <= self._max_speed else self._max_speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed += self._acceleration
        elif keys[pygame.K_s]:
            self.speed -= self._acceleration
        self.speed *= self.friction

        # Apply friction
        self.speed *= self.friction

        self.visible_colliders = self.visible_colliders
