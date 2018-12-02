from Constants import *
import pygame

class Block():

    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.img = image
        self.type = FIRM

        self.x = x
        self.y = y

        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def render(self):
        self.screen.blit(self.img, (self.x, self.y))


class Grass_block(Block):
    def __init__(self, screen, x, y):
        Block.__init__(self, screen, x, y, GRASS_BLOCK)

class Grass(Block):
    def __init__(self, screen, x, y):
        Block.__init__(self, screen, x, y, GRASS)
        self.type = GHOST

class Dirt_block(Block):
    def __init__(self, screen, x, y):
        Block.__init__(self, screen, x, y, DIRT_BLOCK)