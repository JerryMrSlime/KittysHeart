'''
Created on 23/8/2014

@author: Alberto
'''

from pygame.locals import K_w, K_a, K_d, K_s

from lifeBar import LifeBar
import pygame as py
from settings import SCREEN_WIDTH


SCALE = 9
SPEED = 3
JUMPSPEED = 10



class Player(object):

    def __init__(self, groundPos):
        self.img = py.image.load("resources/graphics/player.png").convert_alpha()
        self.img = py.transform.scale(self.img, (self.img.get_width() * SCALE, self.img.get_height() * SCALE))

        self.rect = py.Rect(0, 0, self.img.get_width(), self.img.get_height())

        self.flip = False

        #Jumps
        self.gravity = 1
        self.onGround = False
        self.vy = 0
        self.ground = groundPos

        self.lifeBar = LifeBar(100, 1)

    def Render(self, screen):
        screen.blit(py.transform.flip(self.img, self.flip, False), self.rect)
        self.lifeBar.Render(screen)

    def Update(self, applesManager, arrowsManager, particlesManager, kitty, systemScore, soundSystem, gameplayState):
        self.ApplyGravity()
        self.Controls(applesManager, kitty, systemScore, soundSystem)
        self.Move()
        self.CheckArrows(arrowsManager, particlesManager, kitty, soundSystem)

        self.CheckFloor()
        self.CheckBounds()

        self.lifeBar.Update()

        if self.lifeBar.currentLife == 0:
            gameplayState.GameOver()

    def CheckArrows(self, arrowsManager, particlesManager, kitty, soundSystem):
        arrows = arrowsManager.arrows

        i = self.rect.collidelist(arrows)
        if i >= 0:
            arrows.pop(i)
            particlesManager.AddParticles(self.rect)
            particlesManager.AddParticles(kitty.rect)
            self.lifeBar.currentLife -= 2
            kitty.Hit()
            soundSystem.PlaySound(2)


    def ApplyGravity(self):
        if not self.onGround:
            self.vy += self.gravity
        else:
            self.vy = 0

    def Move(self):
        self.rect.move_ip(0, self.vy)

    def CheckFloor(self):
        if self.rect.bottom > self.ground:
            self.rect.bottom = self.ground
            self.onGround = True

    def CheckBounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def Controls(self, applesManager, kitty, systemScore, soundSystem):
        key = py.key.get_pressed()

        if key[K_w] and self.onGround:
            self.vy = -JUMPSPEED
            self.onGround = False
            soundSystem.PlaySound(1)

        if key[K_a]:
            self.rect.move_ip(-SPEED, 0)
            self.flip = True
        if key[K_d]:
            self.rect.move_ip(SPEED, 0)
            self.flip = False

        if key[K_s]:
            i = self.rect.collidelist(applesManager.apples)
            if i >= 0:
                applesManager.apples.pop(i)
                self.lifeBar.currentLife += 2
                kitty.Health()
                systemScore.score += 1
                soundSystem.PlaySound(3)

    def Reset(self):
        self.lifeBar.currentLife = self.lifeBar.maxLife