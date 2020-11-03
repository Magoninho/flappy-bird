"""
Um protótipo para testar colisões no pygame e como elas devem ser feitas no flappy bird
Apenas para motivos de aprendizado
"""
import pygame
import random
from player import *
""" Obstacles """
# from teste_collision import Player

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

# classe do obstáculo (não fiz uma herança com o player pq tive dificuldades)


obstacles = []  # o array que vai receber os rects que serão usados para desenhar de fato os obstaculos


def create_obstacles():
    pass


def draw_obstacles():
    pass


def main():
    for i in range(10):  # cria um rect diferente para cada interação do loop
        x = random.randint(0, WIDTH)  # posição aleatoria x
        y = random.randint(0, HEIGHT)  # posição aleatoria y
        # definindo um novo rect para cada interação do loop
        obstacle_rect = pygame.Rect(x, y, 40, 40)
        # adicionando o rect na lista de obstaculos
        obstacles.append(obstacle_rect)

    class Obstacle:
        def __init__(self, screen, size, rect):
            self.screen = screen
            self.size = size
            self.rect = rect  # eu peço o Rect

        def draw_obstacle(self):
            # desenha o obstáculo a partir dos Rects do array obstacles
            pygame.draw.rect(self.screen, WHITE, self.rect)

    # object instances
    # criando os obstaculos
    player = Player(SCREEN, WIDTH/2-20, HEIGHT/2-20, 40)

    # game loop
    print(obstacles)
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
            Obstacle(SCREEN, 40, obstacles[o]).draw_obstacle()

        pygame.display.update()


if __name__ == "__main__":
    main()
