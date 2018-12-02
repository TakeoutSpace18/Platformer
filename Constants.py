import pygame

WINDOW_TITLE = "Platformer"

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540



GRASS_BLOCK = pygame.image.load("data/img/grass.png")
GRASS = pygame.image.load("data/img/grass2.png")
DIRT_BLOCK = pygame.image.load("data/img/dirt.png")


BLOCK_WIDTH = BLOCK_HEIGHT = GRASS.get_width()

HERO = pygame.image.load("data/img/hero2.png")
#HERO = pygame.transform.scale(HERO, (128, 128))

#direction
RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4 

FIRM = 5
GHOST = 6

LEVEL = ["--------22----------22----------2-------",
         "------2211--------2111---------21-------",
         "222--211332222222113331------221311-----",
         "1111113333111111133333311111111333311111"]