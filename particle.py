'''
Created on 24/8/2014

@author: Alberto
'''

import pygame as py
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Particle(object):

    def __init__(self, x, y, vx, vy):
        self.size = 4
        self.rect = py.Rect(x, y, self.size, self.size)
        self.gravity = 1
        self.dead = False
        self.vy = vy
        self.vx = vx

    def Update(self):
        if not self.dead:
            self.vy += self.gravity
            self.rect.move_ip(self.vx, self.vy)
            self.CheckBounds()

    def Render(self, screen):
        if not self.dead:
            py.draw.rect(screen, (255, 0, 0), self.rect)

    def CheckBounds(self):
        if (self.rect.left < 0 or self.rect.right > SCREEN_WIDTH or self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT):
            self.dead = True