import pygame
from settings import *
from sprites import *
from map import *
from os import path
import sys
pygame.init()

class Spil:

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
        self.player_img = pygame.image.load(path.join(assets_folder, PLAYER_IMG ))



    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        player = Player()
        all_sprites.add(player)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

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

