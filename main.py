'''
Created on 23/8/2014

@author: Alberto
'''

from pygame.locals import QUIT

import pygame as py
from scene import Scene
from settings import SIZE
from statesManager import StatesManager


def main():

    py.init()

    py.display.set_icon(py.image.load("resources/graphics/icon.bmp"))
    screen = py.display.set_mode(SIZE)
    py.display.set_caption("Kitty's Heart")


    exit = False
    clock = py.time.Clock()
    clear = (0, 255, 255)

    scene = Scene()
    statesManager = StatesManager(scene)

    while not exit:
        screen.fill(clear)

        for event in py.event.get():
            if event.type == QUIT:
                exit = True

        #------------------
        scene.Render(screen)
        statesManager.Update()
        statesManager.Render(screen)

        #------------------
        py.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()