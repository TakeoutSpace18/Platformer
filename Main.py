import pygame
import sys
from Constants import *


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.running = True

        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        
        self.loop()

    def loop(self):
        while self.running:
            self.handle_events()
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



    def render(self):
        self.screen.fill((200, 200, 200))

        self.screen.blit(IMG, (self.width - 600, self.height - 600))

        pygame.display.update()
        


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(WINDOW_TITLE)

window = Game(screen)