'''
Created on 23/8/2014

@author: Alberto
'''

from random import randrange

import pygame as py


class ApplesSpawner(object):

    def __init__(self, img, x, y, applesManager):
        self.img = img

        self.rect = py.Rect(x, y, self.img.get_width(), self.img.get_height())

        self.timer = 0
        self.delay = randrange(5000, 8000)
        self.applesManager = applesManager

    def Update(self):
        self.Timer()

    def Render(self, screen):
        screen.blit(self.img, self.rect)

    def Timer(self):
        if py.time.get_ticks() - self.timer > self.delay:
            self.timer = py.time.get_ticks()
            self.Grow()

    def Grow(self):
        self.applesManager.GrowApple(self)
