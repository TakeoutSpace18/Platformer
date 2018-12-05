import pygame
from Constants import *

def intersects(one, two): # First rectangle (x, y, width, height) Second rectangle (x, y, width, height)

    if one.bottom <= two.bottom and one.bottom > two.top and one.right > two.left and one.right <= two.right:
        return True
    elif one.bottom <= two.bottom and one.bottom > two.top and one.left >= two.left and one.left < two.right:
        return True
    elif one.top < two.bottom and one.top >= two.top and one.left >= two.left and one.left < two.right:
        return True
    elif one.top < two.bottom and one.top >= two.top and one.right > two.left and one.right <= two.right:
        return True
    else: return False

class Hero():

    def __init__(self, screen):
        self.screen = screen

        self.img = HERO
        self.x = 50
        self.y = 70

        self.height = self.img.get_height()
        self.width = self.img.get_width()

        self.top = self.y
        self.bottom = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width

        self.onGround = False

        self.yvel = 0
        self.xvel = 0

        self.jump_power = 0.7
        self.speed = 0.3
        self.gravity_force = 0.001

    def handle_event(self, event_type, key):
        if event_type == pygame.KEYDOWN:
            if key == pygame.K_RIGHT:
                self.xvel = self.speed
            elif key == pygame.K_LEFT:
                self.xvel = -self.speed
            elif key == pygame.K_UP:
                if self.onGround:
                    self.yvel = -self.jump_power

        elif event_type == pygame.KEYUP:
            if key == pygame.K_RIGHT and self.xvel > 0:
                self.xvel = 0
            elif key == pygame.K_LEFT and self.xvel < 0:
                self.xvel = 0

    def check_collision(self, xvel, yvel, platforms):
        for p in platforms:
            if intersects(self, p):
                if yvel > 0:
                    self.y = p.top - self.height
                    self.onGround = True
                    self.yvel = 0
                    

                if xvel > 0:
                    self.x = p.left - self.width

                if xvel < 0:
                    self.x = p.right
                break

    def update(self, platforms, dt):

        if self.y > 800:
            self.y = 50

        if not self.onGround:
            self.yvel += self.gravity_force

        self.onGround = False

        self.x += self.xvel * dt
        self.check_collision(self.xvel, 0, platforms)

        self.y += self.yvel * dt
        self.check_collision(0, self.yvel, platforms)
        

        
        
        self.top = self.y
        self.bottom = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width
        print(self.onGround)

    def render(self):
        self.screen.blit(self.img, (self.x, self.y))