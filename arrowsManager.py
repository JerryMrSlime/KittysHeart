'''
Created on 23/8/2014

@author: Alberto
'''
from random import randrange

from arrow import Arrow
from arrowsLauncher import ArrowsLauncher
import pygame as py


class ArrowsManager(object):

    def __init__(self):
        self.launchers = []
        self.arrows = []

        self.arrow_img = py.image.load("resources/graphics/arrow.png").convert_alpha()

        self.launcher_img = py.image.load("resources/graphics/arrows_launcher.png").convert_alpha()
        self.launcher_img = py.transform.scale(self.launcher_img, (self.launcher_img.get_width() * 2, self.launcher_img.get_height() * 2))

        self.AddLaunchers()

        self.timer = 0
        self.delay = 500

    def Update(self):
        self.UpdateArrows()
        self.UpdateLaunchers()
        self.Timer()

    def Render(self, screen):
        self.RenderArrows(screen)
        self.RenderLaunchers(screen)

    def UpdateArrows(self):
        for arrow in self.arrows:
            arrow.Update()
            if arrow.dead:
                self.arrows.remove(arrow)

    def RenderArrows(self, screen):
        for arrow in self.arrows:
            arrow.Render(screen)

    def UpdateLaunchers(self):
        for launcher in self.launchers:
            launcher.Update()

    def RenderLaunchers(self, screen):
        for launcher in self.launchers:
            launcher.Render(screen)

    def AddLaunchers(self):
        #LEFT LAUNCHERS
        for i in range(2):
            self.launchers.append(ArrowsLauncher(self, py.transform.flip(self.launcher_img, True, False), i))

        #RIGHT LAUNCHERS
        for i in range(2, 4):
            self.launchers.append(ArrowsLauncher(self, self.launcher_img, i))

    def AddArrow(self, launcher):
        i = launcher.i
        x, direction = 0, 0

        y = launcher.rect.centery
        if i <= 1:
            x = launcher.rect.left
        else:
            x = launcher.rect.right
            direction = 1

        self.arrows.append(Arrow(self.arrow_img, x, y, direction))

    def Timer(self):
        if py.time.get_ticks() - self.timer > self.delay:
            self.timer = py.time.get_ticks()
            self.Shoot()

    def Shoot(self):
        done = False
        while not done:
            i = randrange(0, len(self.launchers))
            launcher = self.launchers[i]
            if launcher.canShoot:
                launcher.Shoot()
                done = True