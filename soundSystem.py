'''
Created on 24/8/2014

@author: Alberto
'''

import pygame as py


class SoundSystem(object):

    def __init__(self):
        self.imgs = [self.LoadImage("sound"),
                     self.LoadImage("no_sound")]

        self.sound = 0
        self.release = True

        self.rect = py.Rect(20, 50, self.imgs[self.sound].get_width(), self.imgs[self.sound].get_height())

        self.kitty_jump = self.LoadSound("jump_2")
        self.man_jump = self.LoadSound("jump_1")
        self.arrow_hit = self.LoadSound("damageArrow")
        self.bitting_apple = self.LoadSound("bittingApple")

    def LoadImage(self, src):
        return py.transform.scale2x(py.image.load("resources/graphics/"+str(src)+".png").convert_alpha())

    def LoadSound(self, src):
        return py.mixer.Sound("resources/sounds/"+str(src)+".ogg")

    def Render(self, screen):
        screen.blit(self.imgs[self.sound], self.rect)

    def Update(self):
        mouseX, mouseY = py.mouse.get_pos()
        if py.mouse.get_pressed()[0]:

            if self.rect.collidepoint(mouseX, mouseY) and self.release:
                if self.sound == 0:
                    self.sound = 1
                else:
                    self.sound = 0
                self.release = False


        if py.mouse.get_rel()[1]:
            self.release = True

    def PlaySound(self, i):
        if self.sound == 0:
            if i == 0:
                self.kitty_jump.play()
            elif i == 1:
                self.man_jump.play()
            elif i == 2:
                self.arrow_hit.play()
            elif i == 3:
                self.bitting_apple.play()
