import pygame
from settings import *
from map import *


class Player(pygame.sprite.Sprite):
    # Player sprite

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(assets_folder, "Player.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        # Moves player left and right
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx
        # Moves Player up and down
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_s]:
            self.speedy = 5
        self.rect.y += self.speedy

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