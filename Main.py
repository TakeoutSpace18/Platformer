import pygame
import sys
import ctypes
from Constants import *
from Blocks import *
from Objects import *

#FULLSCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
#FULLSCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)

class Game():

    def __init__(self, screen):
        self.screen = screen
        self.camera = Camera(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.running = True

        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.blocks = self.initialize_level(LEVEL)
        self.platforms = []

        for i in self.blocks:
            if i.type == FIRM:
                self.platforms.append(i)

        self.player = Hero(self.camera, self)

        self.loop()

    def loop(self):
        last_time = 0
        while self.running:

            current_time = pygame.time.get_ticks()
            dt = current_time - last_time
            last_time = current_time

            self.handle_events()

            if COLOR_BORDER_BLOCKS:
                for block in self.platforms:
                    block.img = block.default_img

            self.player.update(self.platforms, dt)
            self.camera.update(self.player.x, self.player.y, self.width, self.height)

            if self.running:
                self.render()

            


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit

            elif event.type == pygame.VIDEORESIZE:

                self.width = event.w
                self.height = event.h

                screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.player.handle_event(event.type, event.key)

    def render(self):
        self.screen.fill((170, 252, 249))

        self.player.render()

        for i in self.blocks:
            i.render()

        self.camera.render()

        pygame.display.update()

        
    def initialize_level(self, level):
        blocks = []

        y = TOTAL_LEVEL_HEIGHT - BLOCK_HEIGHT

        for string in reversed(level):
            x = 0
            for symbol in string:
                if symbol == "1":
                    blocks.append(Grass_block(self.camera, x, y))
                elif symbol == "2":
                    pass
                    blocks.append(Grass(self.camera, x, y))
                elif symbol == "3":
                    blocks.append(Dirt_block(self.camera, x, y))
                x += BLOCK_WIDTH
            y -= BLOCK_HEIGHT

        return blocks



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(WINDOW_TITLE)

window = Game(screen)
