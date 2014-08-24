'''
Created on 23/8/2014

@author: Alberto
'''

import pygame as py
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class ArrowsLauncher(object):

    def  __init__(self, arrowsManager, img, i):

        self.am = arrowsManager
        self.img = img

        self.ConfigurePosition(i)

        self.canShoot = True
        self.timer = 0
        self.delay = 1000

    def ConfigurePosition(self, i):
        floor = SCREEN_HEIGHT - 15 - self.img.get_height()
        self.i = i
        if i == 0:
            x = 0
            y = floor
        elif i == 1:
            x = 0
            y = floor - self.img.get_height() * 3

        if i == 2:
            x = SCREEN_WIDTH - self.img.get_width()
            y = floor
        elif i == 3:
            x = SCREEN_WIDTH - self.img.get_width()
            y = floor - self.img.get_height() * 3

        self.rect = py.Rect(x, y, self.img.get_width(), self.img.get_height())

    def Update(self):
        if not self.canShoot:
            self.Timer()

    def Render(self, screen):
        screen.blit(self.img, self.rect)

    def Timer(self):
        if py.time.get_ticks() - self.timer > self.delay:
            self.timer = py.time.get_ticks()
            self.canShoot = True

    def Shoot(self):
        if self.canShoot:
            self.am.AddArrow(self)
            self.canShoot = False