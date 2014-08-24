'''
Created on 24/8/2014

@author: Alberto
'''
from pygame.locals import K_UP, K_DOWN, K_w, K_s, K_RETURN

import pygame as py
from settings import SCREEN_WIDTH


class MenuState(object):
    def __init__(self, statesManager):
        self.font = py.font.Font("resources/fonts/font.ttf", 40)
        self.label = self.font.render("Kitty's Heart", 1, (255, 255, 255))

        self.font_2 = py.font.Font("resources/fonts/font.ttf", 20)

        self.play_label = self.font_2.render("Play", 1, (255, 255, 255))
        self.credits_label = self.font_2.render("Credits", 1, (0, 0, 0))

        self.cursor = py.image.load("resources/graphics/apple.png").convert_alpha()

        self.line_1 = self.font_2.render("Game made by Alberto <Luminnem> Lorente", 1, (0, 0, 0))
        self.line_2 = self.font_2.render("for the Ludum Dare 30 Contest", 1, (0, 0, 0))
        self.line_3 = self.font_2.render("Thanks for playing :)", 1, (0, 0, 0))

        self.lines = [self.line_1, self.line_2, self.line_3]

        self.selected = 0
        self.statesManager = statesManager


    def Update(self):
        key = py.key.get_pressed()
        if key[K_UP] or key[K_w]:
            if self.selected == 1:
                self.selected = 0
        elif key[K_DOWN] or key[K_s]:
            if self.selected == 0:
                self.selected = 1

        if key[K_RETURN] and self.selected == 0:
            self.statesManager.currentState = 1

    def Render(self, screen):
        screen.blit(self.label, (SCREEN_WIDTH / 2 - self.label.get_width() / 2, 50))

        screen.blit(self.play_label, (SCREEN_WIDTH / 2, 175))
        screen.blit(self.credits_label, (SCREEN_WIDTH / 2, 275))

        y = 0
        if self.selected == 0:
            y = 175
        elif self.selected == 1:
            y = 275

        screen.blit(self.cursor, (SCREEN_WIDTH / 2 - 10 - self.cursor.get_width(), y))

        if self.selected == 1:
            self.DrawCredits(screen)

    def DrawCredits(self, screen):
        for i, line in enumerate(self.lines):
            screen.blit(line, (30, 25 * i + 350))