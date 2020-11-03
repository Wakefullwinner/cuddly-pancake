import pygame
pygame.init()


import pygame

pygame.init()


finished = False
clock = pygame.time.Clock()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


    pygame.display.update()
    clock.tick(60)

