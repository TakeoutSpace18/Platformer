import pygame

WINDOW_TITLE = "Platformer"

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540



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

LEVEL = ["333                                   3 ",
         "333                                   3 ",
         "333                                  3  ",
         "333                                 33  ",
         "333                                333  ",
         "333                                333  ",
         "333                             2131    ",
         "333                             133312  ",
         "333                            21333312 ",
         "11                             11333331 ",
         "3312                         2133333333 ",
         "3331                        2133333333  ",
         "33332                2      1333333333  ",
         "33331 2211        2111     1333333333   ",
         "33333211332222222113331 2213333333332222",
         "3333313333311111113333331133333333331111"]