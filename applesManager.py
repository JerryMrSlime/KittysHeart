'''
Created on 23/8/2014

@author: Alberto
'''
from random import  randrange

from apple import Apple
from applesSpawner import ApplesSpawner
import pygame as py
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class ApplesManager(object):

    def __init__(self):
        self.apples = []
        self.spawners = []

        self.apple_img = py.image.load("resources/graphics/apple.png").convert_alpha()
        self.spawner_img = py.image.load("resources/graphics/apples_spawner.png").convert_alpha()

        self.maxSpawners = 5
        self.GenerateSpawners()

    def Update(self):
        self.UpdateApples()
        self.UpdateSpawners()

    def GenerateSpawners(self):
        for i in range(self.maxSpawners):
            x = randrange(30, SCREEN_WIDTH - self.spawner_img.get_width())
            y = randrange(0, SCREEN_HEIGHT / 4)
            self.spawners.append(ApplesSpawner(self.spawner_img, x, y, self))

    def UpdateApples(self):
        for apple in self.apples:
            apple.Update()
            if apple.rotten:
                self.apples.remove(apple)

    def UpdateSpawners(self):
        for spawner in self.spawners:
            spawner.Update()

    def Render(self, screen):
        self.RenderSpawners(screen)
        self.RenderApples(screen)

    def RenderApples(self, screen):
        for apple in self.apples:
            apple.Render(screen)

    def RenderSpawners(self, screen):
        for spawner in self.spawners:
            spawner.Render(screen)

    def GrowApple(self, spawner):
        x = spawner.rect.centerx - self.apple_img.get_width() / 2
        y = spawner.rect.centery - 5
        self.apples.append(Apple(self.apple_img, x, y))