'''
Created on 23/8/2014

@author: Alberto
'''

import pygame as py
from settings import SCREEN_HEIGHT


class Apple(object):

    def __init__(self, img, x, y):
        self.img = img
        self.rect = py.Rect(x, y, self.img.get_width(), self.img.get_height())

        self.gravity = 1
        self.vy = 0
        self.canFall = False
        self.grown = False
        self.timer = 0
        self.delay = 1000

        self.timer_2 = 0
        self.removeDelay = 2000
        self.rotten = False

        self.firstFloor = False
        self.taken = False
        self.secondFloor = False

    def Render(self, screen):
        screen.blit(self.img, self.rect)

    def Update(self):
        self.ApplyGravity()
        self.Timer()
        self.DeleteTimer()
        self.Move()
        self.CheckFirstFloor()
        self.CheckSecondFloor()

    def CheckFirstFloor(self):
        if self.rect.bottom > SCREEN_HEIGHT / 2 - 3 * 5 and not self.taken:
            self.rect.bottom = SCREEN_HEIGHT / 2 - 3 * 5
            self.firstFloor = True
            self.canFall = False

    def CheckSecondFloor(self):
        if self.rect.bottom > SCREEN_HEIGHT - 3 * 5:
            self.rect.bottom = SCREEN_HEIGHT - 3 * 5
            self.secondFloor = True
            self.canFall = False

    def Timer(self):
        if py.time.get_ticks() - self.timer > self.delay and not self.grown:
            self.grown = True
            self.canFall = True

    def DeleteTimer(self):
        if self.firstFloor or self.secondFloor:
            if py.time.get_ticks() - self.timer_2 > self.removeDelay:
                self.rotten = True
        else:
            self.timer_2 = py.time.get_ticks()

    def Move(self):
        self.rect.move_ip(0, self.vy)

    def ApplyGravity(self):
        if self.canFall:
            self.vy += self.gravity
        else:
            self.vy = 0

    def Take(self):
        self.canFall = True
        self.taken = True
        self.firstFloor = False