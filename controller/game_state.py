import pygame
import sys
from random import choice
from entities.text_entity import Text
from entities.bullet_entity import Bullet
from paths import FONT_PATH, IMAGE_PATH
from util.colors import GREEN, WHITE


SCREEN = pygame.display.set_mode((800, 600))
FONT = FONT_PATH + 'space.ttf'
IMG_NAMES = ['player',
             'laser', ]

IMAGES = {name: pygame.image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES}


class Life(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = IMAGES['player']
        self.image = pygame.transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

#    def update(self, *args):
#        pygame.game.screen.blit(self.image, self.rect)


class Crew(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.caption = pygame.display.set_caption('CREW')
        self.screen = SCREEN
        self.background = pygame.image.load(
            IMAGE_PATH + 'background.jpg').convert()
        self.startGame = False
        self.mainScreen = True
        self.gameOver = False

        self.titleText = Text(FONT, 50, 'CREW', WHITE, 350, 155)
        self.titleText2 = Text(FONT, 25, 'Press any key to continue', WHITE,
                               201, 225)
        self.gameOverText = Text(FONT, 50, 'Game Over', WHITE, 250, 270)
        self.nextRoundText = Text(FONT, 50, 'Next Round', WHITE, 240, 270)
        self.scoreText = Text(FONT, 20, 'Score', WHITE, 5, 5)
        self.livesText = Text(FONT, 20, 'Lives ', WHITE, 640, 5)

        self.life1 = Life(715, 3)
        self.life2 = Life(742, 3)
        self.life3 = Life(769, 3)
        self.livesGroup = pygame.sprite.Group(
            self.life1, self.life2, self.life3)

    def reset(self, score):
        # self.player = Player()
        # self.playerGroup = sprite.Group(self.player)
        self.bullets = pygame.sprite.Group()

        # self.make_enemies()

        # Call all sprits -> To call more sprits, add here
        self.allSprites = pygame.sprite.Group(self.livesGroup)
        self.keys = pygame.key.get_pressed()

        self.timer = pygame.time.get_ticks()
        self.noteTimer = pygame.time.get_ticks()
        self.playerTimer = pygame.time.get_ticks()
        self.score = score
        self.makeNewPlayer = False
        self.playerAlive = True

    @staticmethod
    def should_exit(evt):
        # type: (pygame.event.EventType) -> bool
        return evt.type == pygame.QUIT or (evt.type == pygame.KEYUP and evt.key == pygame.K_ESCAPE)

    def check_input(self):
        self.keys = pygame.key.get_pressed()
        for e in pygame.event.get():
            if self.should_exit(e):
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if len(self.bullets) == 0 and self.playerAlive:
                        if self.score < 1000:
                            bullet = Bullet(self.player.rect.x + 23,
                                            self.player.rect.y + 5, -1,
                                            15, 'laser', 'center')
                            self.bullets.add(bullet)
                            self.allSprites.add(self.bullets)
                            # self.sounds['shoot'].play()
                        else:
                            leftbullet = Bullet(self.player.rect.x + 8,
                                                self.player.rect.y + 5, -1,
                                                15, 'laser', 'left')
                            rightbullet = Bullet(self.player.rect.x + 38,
                                                 self.player.rect.y + 5, -1,
                                                 15, 'laser', 'right')
                            self.bullets.add(leftbullet)
                            self.bullets.add(rightbullet)
                            self.allSprites.add(self.bullets)
                            self.sounds['shoot2'].play()

    def calculate_score(self, row):
        scores = {0: 30,
                  1: 20,
                  2: 20,
                  3: 10,
                  4: 10,
                  5: choice([50, 100, 150, 300])
                  }

        score = scores[row]
        self.score += score
        return score

#    def create_new_player(self, createPlayer, currentTime):
#        if createPlayer and (currentTime - self.playerTimer > 900):
#            self.player = Player()
#            self.allSprites.add(self.player)
#            self.playerGroup.add(self.player)
#            self.makeNewPlayer = False
#            self.playerAlive = True

    def create_game_over(self, currentTime):
        self.screen.blit(self.background, (0, 0))
        passed = currentTime - self.timer
        if passed < 750:
            self.gameOverText.draw(self.screen)
        elif 750 < passed < 1500:
            self.screen.blit(self.background, (0, 0))
        elif 1500 < passed < 2250:
            self.gameOverText.draw(self.screen)
        elif 2250 < passed < 2750:
            self.screen.blit(self.background, (0, 0))
        elif passed > 3000:
            self.mainScreen = True

        for e in pygame.event.get():
            if self.should_exit(e):
                sys.exit()

    def main(self):
        while True:
            if self.mainScreen:
                self.screen.blit(self.background, (0, 0))
                self.titleText.draw(self.screen)
                self.titleText2.draw(self.screen)
                for e in pygame.event.get():
                    if self.should_exit(e):
                        sys.exit()
                    if e.type == pygame.KEYUP:
                        self.livesGroup.add(self.life1, self.life2, self.life3)
                        self.reset(0)
                        self.startGame = True
                        self.mainScreen = False

            elif self.startGame:
                currentTime = pygame.time.get_ticks()
                self.screen.blit(self.background, (0, 0))
                self.scoreText2 = Text(FONT, 20, str(self.score), GREEN,
                                       85, 5)
                self.scoreText.draw(self.screen)
                self.scoreText2.draw(self.screen)
                self.livesText.draw(self.screen)
                self.check_input()
                # self.enemies.update(currentTime)
                self.allSprites.update(self.keys, currentTime)
                # self.check_collisions()
                # self.create_new_player(self.makeNewPlayer, currentTime)
                # self.make_enemies_shoot()

            elif self.gameOver:
                currentTime = pygame.time.get_ticks()
                # Reset starting position
                self.create_game_over(currentTime)

            pygame.display.update()
            self.clock.tick(60)
