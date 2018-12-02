import pygame
from Constants import *

class Hero():

    def __init__(self, screen):
        self.screen = screen

        self.img = HERO
        self.x = 50
        self.y = 70

        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.onGround = False


        self.jump_power = 2
        self.yvel = 0
        self.xvel = 0

        self.speed = 0.3
        self.gravity_force = 0.1

    def handle_event(self, event_type, key):
        if event_type == pygame.KEYDOWN:
            if key == pygame.K_UP:
                if self.onGround:
                    self.yvel = -self.jump_power

            if key == pygame.K_RIGHT:
                self.xvel = self.speed

            if key == pygame.K_LEFT:
                self.xvel = -self.speed
        else: 
            if key == pygame.K_LEFT and self.xvel < 0:
                self.xvel = 0

            if key == pygame.K_RIGHT and self.xvel > 0:
                self.xvel = 0

                
    def check_collision(self, platforms):
        for p in platforms:

            if self.rect.colliderect(p.rect):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom 
                    self.yvel = 0                 

            

    def update(self, platforms, dt):

        if not self.onGround:
            self.yvel +=  self.gravity_force

        self.onGround = False
        self.check_collision(platforms)
        self.rect.x += self.xvel * dt
        self.rect.y += self.yvel * dt



    def render(self):

        self.screen.blit(self.img, self.rect)