import pygame
from pygame.locals import *
from pygame.sprite import Group
import random


clock = pygame.time.Clock()
fps = 60

screen_width =  600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

#define colours
red = (255, 0, 0)
green = (0, 255, 0)


def draw_bg():
    screen.fill((0,0,0))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        #self.image.fill((255, 0, 0))
        self.image = pygame.image.load('assets/Nave completa.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks() #Verify when the bullet was created
        self.cooldown = 500 #set cooldown for the bullets

    def update(self):
        #set movement speed
        speed = 8


        #get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += speed

        time_now = pygame.time.get_ticks()

        if key[pygame.K_SPACE] and time_now - self.last_shot > self.cooldown and self.alive():
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now
        



class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 10))
        self.image.fill((150, 200, 255))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #set movement speed
        speed = 5

        self.rect.y -= speed

        if self.rect.bottom < 0:
            self.kill()   

        
        


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        #self.image.fill((150, 200, 0))
        self.image = pygame.image.load('assets/comet-3.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #set movement speed
        speed = 3
        
        self.rect.y += speed

        if self.rect.top > screen_height:
            self.kill()
        
        if pygame.sprite.spritecollide(self, spaceship_group, True):
            self.kill()
        if pygame.sprite.spritecollide(self, bullet_group, True):
            self.kill()

class Throttle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((25, 50))
        #self.image.fill((150, 255, 250))
        self.image = pygame.image.load('assets/Propulsor-2.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #set movement speed
        speed = 3
        
        self.rect.y += speed

        if self.rect.top > screen_height:
            self.kill()
        
        if pygame.sprite.spritecollide(self, spaceship_group, False):
            self.kill()
            spaceship.cooldown /= 4




spaceship_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
throttle_group = pygame.sprite.Group()

#create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100)
spaceship_group.add(spaceship)

#create asteroid

asteroid = Asteroid(random.randint(0, screen_width), 100)
asteroid_group.add(asteroid)

#create throttle
throttle = Throttle(400, 200)
throttle_group.add(throttle)


run = True
while run:
    clock.tick(fps)
    

    draw_bg()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update player
    spaceship.update()

    #update groups
    asteroid_group.update()
    bullet_group.update()
    throttle_group.update()

    #draw sprite groups
    asteroid_group.draw(screen)
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    throttle_group.draw(screen)
    

    pygame.display.update() 

pygame.quit()