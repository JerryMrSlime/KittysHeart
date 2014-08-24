'''
Created on 23/8/2014

@author: Alberto
'''

import pygame as py


class Detail(object):
    def __init__(self, img, x, y):
        self.img = img
        self.rect = py.Rect(x, y, self.img.get_width(), self.img.get_height())

    def Render(self, screen):
        screen.blit(self.img, self.rect)