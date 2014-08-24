'''
Created on 24/8/2014

@author: Alberto
'''

from random import randrange

from particle import Particle


class ParticlesManager(object):

    def __init__(self):
        self.particles = []
        self.maxParticles = 20

    def Update(self):
        for particle in self.particles:
            particle.Update()
            if particle.dead:
                self.particles.remove(particle)

    def Render(self, screen):
        for particle in self.particles:
            particle.Render(screen)


    def AddParticles(self, rect):
        for i in range(self.maxParticles):
            x = rect.centerx
            y = rect.centery
            side = randrange(0, 2)
            if side == 0:
                vx = randrange(-5, -1)
            else:
                vx = randrange(1, 5)

            vy = randrange(-10, -1)

            self.particles.append(Particle(x, y, vx, vy))
