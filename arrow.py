'''
Created on 23/8/2014

@author: Alberto
'''

import pygame as py


class Arrow(object):

    def __init__(self, img, x, y, direction):
        self.img = img
        if direction == 0:
            self.img = py.transform.flip(self.img, True, False)
        self.direction = direction
        self.rect = py.Rect(int(x), int(y), self.img.get_width(), self.img.get_height())
        self.speed = 5
        self.dead = False

    def Update(self):
        if self.direction == 0:
            self.rect.move_ip(self.speed, 0)
        elif self.direction == 1:
            self.rect.move_ip(-self.speed, 0)

    def Render(self, screen):
        screen.blit(self.img, self.rect)

    def CheckBounds(self):
        if self.rect.left < 0 or self.rect.right > 480:
            self.dead = True
