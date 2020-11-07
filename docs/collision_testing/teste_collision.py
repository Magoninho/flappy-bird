"""
Um protótipo para testar colisões no pygame e como elas devem ser feitas no flappy bird
Apenas para motivos de aprendizado
"""

import pygame
import random

# CONSTANTS
# display settings
WIDTH, HEIGHT = 400, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


OBSTACLE_NUMBER = 10    # número de obstáculos
# mude caso necessário


# Classes

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

        self.changable_color = (255, 255, 0)  # will always make
        for obstacle in range(len(obstacles)):

            if self.player_rect.colliderect(obstacles[obstacle]):
                self.changable_color = (255, 0, 0)

# classe do obstáculo (não fiz uma herança com o player pq tive dificuldades)


class Obstacle:
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = rect  # eu peço o Rect

    def draw_obstacle(self):
        # desenha o obstáculo a partir dos Rects do array obstacles
        pygame.draw.rect(self.screen, WHITE, self.rect)


# object instances
player = Player(SCREEN, WIDTH/2-20, HEIGHT/2-20, 40)

""" Obstacles """
obstacles = []  # o array que vai receber os rects que serão usados para desenhar de fato os obstaculos

# criando os obstaculos
for i in range(OBSTACLE_NUMBER):  # cria um rect diferente para cada interação do loop
    x = random.randint(0, WIDTH)  # posição aleatoria 
    y = random.randint(0, HEIGHT)  # posição aleatoria y
    # definindo um novo rect para cada interação do loop
    obstacle_rect = pygame.Rect(x, y, 40, 40)
    # adicionando o rect na lista de obstaculos
    obstacles.append(obstacle_rect)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    # Drawinings
    SCREEN.fill(BLACK)
    player.draw_player()  # desenhando o player

    for o in range(len(obstacles)):  # desenhando os rects
        # desenhando o rect com o Rect listado no array de obstaculos
        Obstacle(SCREEN, obstacles[o]).draw_obstacle()

    pygame.display.update()
