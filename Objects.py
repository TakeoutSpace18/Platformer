import pygame
from Constants import *

def between(a, mn, mx):
    if a >= mn and a <= mx:
        return True
    else: return False

def intersects(one, two): #returns (LEFT/RIGHT, UP/DOWN)

    if one.bottom <= two.bottom and one.bottom > two.top and one.right > two.left and one.right <= two.right:
        return (RIGHT, DOWN)    
    elif one.bottom <= two.bottom and one.bottom > two.top and one.left >= two.left and one.left < two.right:
        return (LEFT, DOWN)
    elif one.top < two.bottom and one.top >= two.top and one.left >= two.left and one.left < two.right:
        return (LEFT, UP)
    elif one.top < two.bottom and one.top >= two.top and one.right > two.left and one.right <= two.right:
        return (RIGHT, UP)
    else: return False

class Hero():

    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        self.img = HERO
        self.x = 50
        self.y = 70

        self.height = self.img.get_height()
        self.width = self.img.get_width()

        self.top = self.y
        self.bottom = self.y + self.height - 1
        self.left = self.x
        self.right = self.x + self.width - 1

        self.bottom_blocks = []
        self.top_blocks = []
        self.right_blocks = []
        self.left_blocks = []

        self.onGround = False

        self.yvel = 0
        self.xvel = 0

        self.jump_power = 0.5
        self.speed = 0.3
        self.gravity_force = 0.007

    def handle_event(self, event_type, key):
        if event_type == pygame.KEYDOWN:
            if key == pygame.K_RIGHT:
                self.xvel = self.speed
            elif key == pygame.K_LEFT:
                self.xvel = -self.speed
            elif key == pygame.K_UP:
                if self.onGround:
                    self.onGround = False
                    self.yvel = -self.jump_power

        elif event_type == pygame.KEYUP:
            if key == pygame.K_RIGHT and self.xvel > 0:
                self.xvel = 0
            elif key == pygame.K_LEFT and self.xvel < 0:
                self.xvel = 0

    def select_blocks(self, platforms):
        self.bottom_blocks = []
        self.top_blocks = []
        self.right_blocks = []
        self.left_blocks = []

        for p in platforms:

            if between(p.top, self.top, self.bottom) or between(p.bottom, self.top, self.bottom):
                if p.right < self.left:
                    self.left_blocks.append(p)
                elif p.left > self.right:
                    self.right_blocks.append(p)

            if between(p.left, self.left, self.right) or between(p.right, self.left, self.right):
                if p.bottom < self.top:
                    self.top_blocks.append(p)
                elif p.top > self.bottom:
                    self.bottom_blocks.append(p)

    def check_collision(self, xvel, yvel, platforms):

        for p in platforms:
            if intersects(self, p):

                if yvel < 0 and intersects(self, p)[1 == UP]:
                    self.y = p.bottom

                if yvel > 0 and intersects(self, p)[1] == DOWN:
                    self.y = p.top - self.height
                    self.onGround = True
                    self.yvel = 0
                    
                if xvel > 0 and intersects(self, p)[0] == RIGHT:
                    self.x = p.left - self.width

                if xvel < 0 and intersects(self, p)[0] == LEFT:
                    self.x = p.right           

    def update(self, platforms, dt):

        if self.y > 800:
            self.y = 50

        if not self.onGround:
            self.yvel += self.gravity_force


        self.x += self.xvel * dt

        self.left = self.x
        self.right = self.x + self.width - 1

        self.check_collision(self.xvel, 0, platforms)

        self.y += self.yvel * dt

        self.top = self.y
        self.bottom = self.y + self.height - 1

        self.check_collision(0, self.yvel, platforms)

        self.select_blocks(platforms)


        for block in self.bottom_blocks:
            block.img = RED

        for block in self.right_blocks:
            block.img = RED

        for block in self.left_blocks:
            block.img = RED

        for block in self.top_blocks:
            block.img = RED
        

    def render(self):
        self.screen.blit(self.img, (self.x, self.y))