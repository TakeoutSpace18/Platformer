import pygame
from Constants import *
class Hero():

    def __init__(self, screen):
        self.screen = screen

        self.img = HERO
        self.x = 50
        self.y = 70

        self.moving = False
        self.direction = RIGHT

        self.speed = 0.3

    def handle_event(self, event_type, key):
        if event_type == pygame.KEYDOWN:
            self.moving = True
            if key == pygame.K_RIGHT:
                self.direction = RIGHT
            if key == pygame.K_LEFT:
                self.direction = LEFT
        else: 
            if key == pygame.K_LEFT and self.direction == LEFT:
                self.moving = False

            if key == pygame.K_RIGHT and self.direction == RIGHT:
                self.moving = False


    def render(self, dt):
        if self.moving:
            if self.direction == RIGHT:
                self.x += self.speed * dt
            elif self.direction == LEFT:
                self.x -= self.speed * dt

        self.screen.blit(self.img, (self.x, self.y))