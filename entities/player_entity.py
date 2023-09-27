import pygame
from entities.bullet_entity import Bullet
from entities.entity import Entity

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

INITIAL_BULLET_VELOCITY = 5
INITIAL_COOLDOWN = 600
MIN_COOLDOWN = 200
BOOST_DURATION = 1000 * 10 * 60 * 2
INITIAL_LIFE = 3


class Player(Entity):
    def __init__(self, velocity, initial_position, bullet_group, boundaries):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(velocity, PLAYER_WIDTH, PLAYER_HEIGHT, initial_position)

        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = initial_position
        self.last_shot = pygame.time.get_ticks()  # Verify when the bullet was created
        self.bullet_group = bullet_group
        self.cooldown = INITIAL_COOLDOWN
        self.bullet_velocity = INITIAL_BULLET_VELOCITY
        self.boundaries = boundaries
        self.is_boosted = False
        self.boost_duration = BOOST_DURATION
        self.boost_start = 0
        self.life = INITIAL_LIFE
        self.bullet_quantity = 3

    def increment_bullet(self):
        self.bullet_quantity += 3

    def decrement_bullet(self):
        self.bullet_quantity -= 1

    def shoot(self, current_time):
        bullet = Bullet(self.bullet_velocity, self.center)
        self.bullet_group.add(bullet)
        self.last_shot = current_time
        self.bullet_quantity -= 1

    def decrease_cooldown(self):
        self.boost_duration = BOOST_DURATION
        self.boost_start = pygame.time.get_ticks()
        self.cooldown = MIN_COOLDOWN

    def player_damage(self):
        if self.life >= 1:
            self.life -= 1
        return self.life

    def update(self):
        # get key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            future_pos = self.get_future_position((-1, 0))
            if future_pos[0] > self.boundaries[0]:
                self.position = future_pos
        if keys[pygame.K_d]:
            future_pos = self.get_future_position((1, 0))
            if future_pos[0] < self.boundaries[1]:
                self.position = future_pos

        current_time = pygame.time.get_ticks()
        self.boost_duration -= current_time - self.boost_start

        if self.boost_duration <= 0:
            self.cooldown = INITIAL_COOLDOWN

        if self.bullet_quantity <= 0:
            self.bullet_quantity = 0

        if self.bullet_quantity >= 20:
            self.bullet_quantity = 20

        is_cooldown_over = current_time - self.last_shot > self.cooldown

        if keys[pygame.K_SPACE] and is_cooldown_over and self.alive():
            self.shoot(current_time)
