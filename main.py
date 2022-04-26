import pygame

TILE_WIDTH = 64
TILE_HEIGHT = 64

WIN_WIDTH = 350
WIN_HEIGHT = 350

WIN = pygame.display.setmode(())

clock = pygame.time.Clock()

run = True
while run:
    clock.tick()
    for event in pygame.event.get():
        if event == pygame.quit:
            run = False