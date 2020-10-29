import pygame, consts, random
from bird import *

class Cano:
    def __init__(self, screen, x):
        self.screen = screen
        self.x = x
        self.y = random.randint(-300, 0)
        self.pipe_vel = 3.1
    
    def draw(self, started, bird):
        
        self.pipes = [pygame.draw.rect(self.screen, consts.GREEN, (self.x, self.y, 80, 400)), pygame.draw.rect(self.screen, consts.GREEN, (self.x, self.y + 550, 80, 400))]    

        if started:
            self.x -= self.pipe_vel
        if self.x < -80:
            self.x = consts.WIDTH
            self.y = random.randint(-300, 0)





            