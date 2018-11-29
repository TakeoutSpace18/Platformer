import pygame
import sys
from Constants import *

from Objects import *


class Game():

    def __init__(self, screen):
        self.screen = screen
        self.running = True

        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.objects = [Hero(self.screen)]

        self.loop()

    def loop(self):
        last_time = 0
        while self.running:

            current_time = pygame.time.get_ticks()
            dt = current_time - last_time
            last_time = current_time

            self.handle_events()
    
            if self.running:
                self.render(dt)


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
                for i in self.objects:
                    i.handle_event(event.type, event.key)

    def render(self, dt):
        self.screen.fill((200, 200, 200))

        for i in self.objects:
            i.render(dt)

        pygame.display.update()
        


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(WINDOW_TITLE)

window = Game(screen)