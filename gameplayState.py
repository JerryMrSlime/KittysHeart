'''
Created on 24/8/2014

@author: Alberto
'''

from applesManager import ApplesManager
from arrowsManager import ArrowsManager
from kitty import Kitty
from particlesManager import ParticlesManager
from player import Player
from scoreSystem import ScoreSystem
from soundSystem import SoundSystem


class GameplayState(object):
    def __init__(self, scene, statesManager):
        self.player = Player(scene.lower_platformPos)
        self.kitty = Kitty(scene.upper_platformPos)
        self.arrowsManager = ArrowsManager()
        self.applesManager = ApplesManager()
        self.particlesManager = ParticlesManager()
        self.scoreSystem = ScoreSystem()
        self.soundSystem = SoundSystem()
        self.statesManager = statesManager

    def Update(self):
        self.player.Update(self.applesManager, self.arrowsManager, self.particlesManager, self.kitty, self.scoreSystem, self.soundSystem, self)
        self.kitty.Update(self.applesManager, self.scoreSystem, self.soundSystem, self)
        self.arrowsManager.Update()
        self.applesManager.Update()
        self.particlesManager.Update()
        self.scoreSystem.Update()
        self.soundSystem.Update()

    def Render(self, screen):
        self.player.Render(screen)
        self.kitty.Render(screen)
        self.arrowsManager.Render(screen)
        self.applesManager.Render(screen)
        self.particlesManager.Render(screen)
        self.scoreSystem.Render(screen)
        self.soundSystem.Render(screen)

    def GameOver(self):
        self.statesManager.GoToGameOver(self.scoreSystem.score)
        self.scoreSystem.score = 0

    def PlayAgain(self):
        self.player.Reset()
        self.kitty.Reset()
