'''
Created on 24/8/2014

@author: Alberto
'''

import pygame as py


class ScoreSystem(object):

    def __init__(self):
        self.font = py.font.Font("resources/fonts/font.ttf", 15)
        self.score = 0
        self.label = self.font.render("Score: ", 1, (255, 255, 255))

    def Update(self):
        self.label = self.font.render("Score: "+str(self.score), 1, (255, 255, 255))

    def Render(self, screen):
        screen.blit(self.label, (20, 20))