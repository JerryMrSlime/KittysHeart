'''
Created on 24/8/2014

@author: Alberto
'''

from gameOverState import GameOverState
from gameplayState import GameplayState
from menuState import MenuState


class StatesManager(object,):
    def __init__(self, scene):
        self.states = [MenuState(self), GameplayState(scene, self), GameOverState(self)]
        self.currentState = 0

    def Update(self):
        self.states[self.currentState].Update()

    def Render(self, screen):
        self.states[self.currentState].Render(screen)

    def GoToGameOver(self, score):
        self.currentState = 2
        self.states[self.currentState].score = score

    def PlayAgain(self):
        self.states[self.currentState].PlayAgain()