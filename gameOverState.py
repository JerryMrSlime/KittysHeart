'''
Created on 24/8/2014

@author: Alberto
'''

from pygame.locals import K_UP, K_DOWN, K_w, K_s, K_RETURN

import pygame as py
from settings import SCREEN_WIDTH


class GameOverState():
    def __init__(self, statesManager):
        self.font = py.font.Font("resources/fonts/font.ttf", 40)

        self.bigLabel = self.font.render("Your final score:", 1, (255, 255, 255))
        self.score = 0
        self.score_label = self.font.render(str(self.score), 1, (255, 255, 255))

        self.cursor = py.image.load("resources/graphics/apple.png").convert_alpha()
        self.font_2 = py.font.Font("resources/fonts/font.ttf", 20)

        self.playAgain = self.font_2.render("Play Again", 1, (0, 0, 0))
        self.selected = 0
        self.labels = [ self.playAgain]

        self.statesManager = statesManager

    def Update(self):
        self.Controls()
        self.score_label = self.font.render(str(self.score), 1, (255, 255, 255))

    def Controls(self):
        key = py.key.get_pressed()

        if key[K_RETURN]:
            if self.selected == 0:
                self.statesManager.currentState = 1
                self.statesManager.PlayAgain()

    def Render(self, screen):
        screen.blit(self.bigLabel, (SCREEN_WIDTH / 2 - self.bigLabel.get_width() / 2, 50))
        screen.blit(self.score_label, (SCREEN_WIDTH / 2 - self.score_label.get_width() / 2, 150))

        for i, label in enumerate(self.labels):
            screen.blit(label, (SCREEN_WIDTH / 2, 300 + i * 30))


        if self.selected == 0:
            y = 300
        elif self.selected == 1:
            y = 330

        screen.blit(self.cursor, (SCREEN_WIDTH / 2 - self.cursor.get_width() - 10, y))