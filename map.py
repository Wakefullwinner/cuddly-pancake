import pygame
from settings import *

def collide_rect(one, two):


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as m:
            for line in m:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE