import pygame
from Constants import *

def between(a, mn, mx):
    if a >= mn and a <= mx:
        return True
    else: return False

def intersects(one, two):

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

    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        self.img = HERO
        self.x = 150
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

        self.jump_power = 0.8
        self.speed = 0.25
        self.gravity_force = 0.035

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
                if p.right <= self.left + 5 and p.right > self.left - self.width // 2:
                    self.left_blocks.append(p)
                elif p.left >= self.right - 5 and p.left < self.right + self.width // 2:
                    self.right_blocks.append(p)

        for p in platforms:
            denied = False

            for b in self.left_blocks:
                if b.x == p.x:
                    denied = True
                    break

            for b in self.right_blocks:
                if b.x == p.x:
                    denied = True
                    break 

            if between(p.left, self.left, self.right) or between(p.right, self.left, self.right):
                if p.bottom <= self.top and p.bottom > self.top - self.height // 3:
                    if not denied:
                        self.top_blocks.append(p)
                elif p.top >= self.bottom and p.top < self.bottom + self.height // 3:
                    if not denied:
                        self.bottom_blocks.append(p)


    def check_collision(self, xvel, yvel, platforms):

        if self.bottom_blocks == []:
            self.onGround = False

        if self.bottom_blocks != [] and yvel > 0:
            
            self.y = self.bottom_blocks[0].top - self.height
            self.onGround = True
            self.yvel = 0

        if self.top_blocks != [] and yvel < 0:
            
            self.y = self.top_blocks[0].bottom
            self.yvel = 0

        if self.right_blocks != [] and xvel > 0:
            
            self.x = self.right_blocks[0].left - self.width + 1

        if self.left_blocks != [] and xvel < 0:
            
            self.x = self.left_blocks[0].right


    def update(self, platforms, dt):

        if self.y > 800:
            self.y = 50

        if not self.onGround:
            self.yvel += self.gravity_force


        self.x += self.xvel * dt

        self.left = self.x
        self.right = self.x + self.width - 1

        self.select_blocks(platforms)
        self.check_collision(self.xvel, 0, platforms)

        self.y += self.yvel * dt

        self.top = self.y
        self.bottom = self.y + self.height - 1

        self.check_collision(0, self.yvel, platforms)

        if COLOR_BORDER_BLOCKS:
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