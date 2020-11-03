import pygame
from teste_collision import *


class Player:

    def __init__(self, screen, x, y, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = size
        self.vel = 0.2
        self.changable_color = (255, 255, 0)
        self.player_rect = pygame.Rect(self.x, self.y, self.size, self.size)
    def player_move(self):

        keys = pygame.key.get_pressed()  # get the keys pressed

        self.x += self.vx
        self.y += self.vy

        self.vx, self.vy = 0, 0

        """
        Tudo precisa ser um IF, só assim o sistema de 8 direções vai funcionar.
        Eu também fiz um sistema de física realista revolution ultimate pra mover o personagens com vetores e força
        """
        if keys[pygame.K_UP]:  # UP
            self.vy = -self.vel
        if keys[pygame.K_DOWN]:  # DOWN
            self.vy = self.vel
        if keys[pygame.K_LEFT]:  # LEFT
            self.vx = -self.vel
        if keys[pygame.K_RIGHT]:  # RIGHT
            self.vx = self.vel
        """
        Aplicação do teorema de pitágoras para fazer a velocidade da diagonal ser a mesma
        """
        if self.vx != 0 and self.vy != 0:
            self.vx /= 1.414  # raiz de 2
            self.vy /= 1.414  # raiz de 2

    def draw_player(self):
        self.player_rect = pygame.Rect(self.x, self.y, self.size, self.size)

        pygame.draw.rect(self.screen, self.changable_color, self.player_rect)

        self.player_move()  # calling the player movement function

        ## COLLISIONS ##

        # will always make the color be yellow
        self.changable_color = (255, 255, 0)
        
        for obstacle in range(len(obstacles)):
            if self.player_rect.colliderect(obstacles[obstacle]):
                self.changable_color = (255, 0, 0)
