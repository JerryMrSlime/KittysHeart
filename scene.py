'''
Created on 23/8/2014

@author: Alberto
'''

from random import randrange

from details import Detail
import pygame as py
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Scene(object):
    def __init__(self):
        self.upper_platform = py.image.load("resources/graphics/upper_platform.png").convert_alpha()
        self.upper_platform = py.transform.scale(self.upper_platform, (self.upper_platform.get_width() * 10, self.upper_platform.get_height() * 5))

        self.lower_platform = py.image.load("resources/graphics/lower_platform.png").convert_alpha()
        self.lower_platform = py.transform.scale(self.lower_platform, (self.upper_platform.get_width() * 10, self.lower_platform.get_height() * 5))

        self.lava_img = py.image.load("resources/graphics/lava.png").convert_alpha()
        self.lava_img = py.transform.scale(self.lava_img, (self.lava_img.get_width() * 2, self.lava_img.get_height() * 2))
        self.details = []

        self.upper_platformPos = SCREEN_HEIGHT / 2 - self.upper_platform.get_height()
        self.lower_platformPos = SCREEN_HEIGHT - self.lower_platform.get_height()

        self.GenerateDetails()

    def Render(self, screen):
        #HEAVEN
        py.draw.rect(screen, (135, 206, 250), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT / 2))
        screen.blit(self.upper_platform, (0, SCREEN_HEIGHT / 2 - self.upper_platform.get_height()))

        #HELL
        py.draw.rect(screen, (178, 34, 34), (0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        self.RenderDetails(screen)
        screen.blit(self.lower_platform, (0, SCREEN_HEIGHT - self.lower_platform.get_height()))

        #Middle Line
        py.draw.rect(screen, (0, 0, 0), (0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, 2))


    def RenderDetails(self, screen):
        for detail in self.details:
            detail.Render(screen)

    def GenerateDetails(self):
        #Generate Lava Details
        for i in range(20):
            x = randrange(0, SCREEN_WIDTH)
            y = randrange(SCREEN_HEIGHT / 2 + self.upper_platform.get_height(), SCREEN_HEIGHT - self.lava_img.get_height())
            self.details.append(Detail(self.lava_img, x, y))