import pygame
from settings import *
from map import *
import math

class Player(pygame.sprite.Sprite):
    # Player sprite

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(assets_folder, "Player.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pSpeedx = 0
        self.pSpeedy = 0

    def update(self, player):
        self.pSpeedx = 0
        keystate = pygame.key.get_pressed()
        # Moves player left and right
        if keystate[pygame.K_a]:
            self.pSpeedx = -5
        if keystate[pygame.K_d]:
            self.pSpeedx = 5
        self.rect.x += self.pSpeedx
        # Moves Player up and down
        self.pSpeedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.pSpeedy = -5
        if keystate[pygame.K_s]:
            self.pSpeedy = 5
        self.rect.y += self.pSpeedy

        # Keeps Player on screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Mob(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT)
        self.mSpeedx = 0
        self.mSpeedy = 0

    def move_to_player(self, player):
        self.speed = 5
        movevect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                       player.rect.y - self.rect.y)
        movevect.normalize()
        movevect.scale_to_length(self.speed)
        self.rect.move_ip(movevect)
