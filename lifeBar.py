'''
Created on 24/8/2014

@author: Alberto
'''

import pygame as py
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class LifeBar(object):

    def __init__(self, life, i):
        self.maxLife = life

        self.img = py.image.load("resources/graphics/lifeBar.png").convert_alpha()
        scale = 4
        self.img = py.transform.scale(self.img, (self.img.get_width() * scale, self.img.get_height() * scale))
        width = self.img.get_width()
        height = self.img.get_height()

        if i == 0:
            x = SCREEN_WIDTH - width - 20
            y = 20
        elif i == 1:
            x = 20
            y = SCREEN_HEIGHT / 2 + 20

        self.rect = py.Rect(x, y, width, height)

        self.currentLife = life
        self.width = 80 * self.currentLife / self.maxLife


    def Update(self):
        self.width = 80 * self.currentLife / self.maxLife

        self.SetLimits()

    def SetLimits(self):
        if self.currentLife < 0:
            self.currentLife = 0

        if self.currentLife > self.maxLife:
            self.currentLife = self.maxLife

    def Render(self, screen):
        py.draw.rect(screen, (255, 0, 0), (self.rect.x + 4, self.rect.y + 4, self.width, 8))
        screen.blit(self.img, self.rect)
