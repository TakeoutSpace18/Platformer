import pygame

WINDOW_TITLE = "Platformer"

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600

COLOR_BORDER_BLOCKS = False

GRASS_BLOCK = pygame.image.load("data/img/grass.png")
GRASS = pygame.image.load("data/img/grass2.png")
DIRT_BLOCK = pygame.image.load("data/img/dirt.png")
RED = pygame.image.load("data/img/red.png")


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


"""
1 - Grass block
2 - Grass
3 - Dirt block


"""



LEVEL = ["                                                                     ",
         "                                                                     ",
         "12                                                                   ",
         "3122                                                                 ",
         "3311                                                                 ",
         "333312                                                             21",
         "3333312                                                           213",
         "333333111                                                        2133",
         "3333333331                                            222       11333",
         "33333333331                22                        211111   1133333",
         "333333333333            22211                      211333331113333333",
         "333333333333         111111331                22211133333333333333333",
         "33333   333         13333333331            22111133333333333333333333",
         "333              211333333333331   2222211111333333333333333333333333",
         "33          222111333333333333331111111133333333333333333333333333333",
         "331111111111111333333333333333333333333333333333333333333333333333333"]