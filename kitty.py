'''
Created on 23/8/2014

@author: Alberto
'''

from pygame.locals import K_UP, K_LEFT, K_RIGHT, K_DOWN

from lifeBar import LifeBar
import pygame as py
from settings import SCREEN_WIDTH


class Kitty(object):
    def __init__(self, groundPos):
        self.scale = 3
        self.ground = groundPos

        self.img = py.image.load("resources/graphics/kitty.png").convert_alpha()
        self.img = py.transform.scale(self.img, (self.img.get_width() * self.scale, self.img.get_height() * self.scale))
        self.flip = False
        self.rect = py.Rect(0, 0, self.img.get_width(), self.img.get_height())


        #Jumps
        self.gravity = 1
        self.onGround = False
        self.vy = 0

        self.lifeBar = LifeBar(50, 0)

    def Update(self, applesManager, systemScore, soundSystem, gameplayState):
        self.ApplyGravity()
        self.Controls(applesManager, systemScore, soundSystem)
        self.Move()

        self.CheckBounds()
        self.CheckFloor()

        self.lifeBar.Update()

        if self.lifeBar.currentLife == 0:
            gameplayState.GameOver()

    def Move(self):
        self.rect.move_ip(0, self.vy)

    def Controls(self, applesManager, systemScore, soundSystem):
        key = py.key.get_pressed()

        if key[K_UP] and self.onGround:
            self.vy = -10
            self.onGround = False
            soundSystem.PlaySound(0)

        if key[K_RIGHT]:
            self.rect.move_ip(3, 0)
            self.flip = False

        if key[K_LEFT]:
            self.rect.move_ip(-3, 0)
            self.flip = True

        if key[K_DOWN]:
            i = self.rect.collidelist(applesManager.apples)
            if i >= 0:
                if applesManager.apples[i].firstFloor:
                    systemScore.score += 1
                    applesManager.apples[i].Take()



    def ApplyGravity(self):
        if not self.onGround:
            self.vy += self.gravity
        else:
            self.vy = 0

    def Hit(self):
        self.lifeBar.currentLife -= 2

    def Health(self):
        self.lifeBar.currentLife += 2

    def CheckFloor(self):
        if self.rect.bottom > self.ground:
            self.rect.bottom = self.ground
            self.onGround = True

    def CheckBounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def Render(self, screen):
        screen.blit(py.transform.flip(self.img, self.flip, False), self.rect)
        self.lifeBar.Render(screen)

    def Reset(self):
        self.lifeBar.currentLife = self.lifeBar.maxLife