import pygame
from settings import *
from map import *
import math

class Player(pygame.sprite.Sprite):
    # Player sprite

    def __init__(self):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.original_image = self.image


    def get_keys(self):
        self.vel = vec(0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pygame.K_s]:
           self.vel.y = PLAYER_SPEED
   #     if self.vel.x != 0 and self.vel.y != 0:
   #         self.vel *= 0.7071


    def rotate(self):
        # The vector to the target (the mouse position).
        direction = pygame.mouse.get_pos() - self.pos
        # .as_polar gives you the polar coordinates of the vector,
        # i.e. the radius (distance to the target) and the angle.
        radius, angle = direction.as_polar()
        # Rotate the image by the negative angle (y-axis in pygame is flipped).
        self.image = pygame.transform.rotate(self.original_image, -angle)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
 
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2.0
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2.0
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2.0
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2.0
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y


    def update(self):
        self.rotate()
        self.get_keys()
        self.rect = self.image.get_rect()
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center
        
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
        
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
