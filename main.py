import pygame
from settings import *
from sprites import *
from map import *
from os import path
import sys
pygame.init()

class Game:

    def init(self):
        pygame.init()
        self.screen = pygame.display.set((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_assets(self):
        game_folder = os.path.dirname(__file__)
        assets_folder = os.path.join(game_folder, "Sprites")
        self.map = Map(path.join(game_folder, 'map1.txt'))
        self.player_img = pygame.image.load(path.join(assets_folder, PLAYER_IMG )).convert_alpha()
        self.wall_img = pygame.image.load(path.join(img_folder, WALL_IMG )).convert_alpha()


    def new(self):
        #Initialize variables and setup new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data): #Enumerate gives both index and the value in a given list or in this case a text file
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        player = Player()
        all_sprites.add(player)

    def run(self):
        self.playing = True
        while self.playing:
            self.time = self.clock.tick(FPS) / 500
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        
     def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

# Game Loop

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

#UPDATE SPRITES
    all_sprites.update()

#DRAW AND RENDER SPRITES
    screen.fill(BLACK)


    pygame.display.update()
    clock.tick(60)

