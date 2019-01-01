from Constants import *
import pygame

class Block():

    def __init__(self, camera, x, y, image):
        self.camera = camera
        self.img = image
        self.type = FIRM

        self.x = x
        self.y = y

        self.top = self.y
        self.bottom = self.y + BLOCK_HEIGHT - 1
        self.left = self.x
        self.right = self.x + BLOCK_WIDTH - 1

        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def render(self):
        self.camera.apply(self)


class Grass_block(Block):
    def __init__(self, screen, x, y):
        Block.__init__(self, screen, x, y, GRASS_BLOCK)
        self.default_img = GRASS_BLOCK

class Grass(Block):
    def __init__(self, screen, x, y):
        Block.__init__(self, screen, x, y, GRASS)
        self.type = GHOST
        self.default_img = GRASS

class Dirt_block(Block):
    def __init__(self, screen, x, y):
        Block.__init__(self, screen, x, y, DIRT_BLOCK)
        self.default_img = DIRT_BLOCK