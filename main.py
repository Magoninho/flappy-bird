import pygame
import os
import random
from colors import *

pygame.mixer.init(44000, -16, 1, 1024)
pygame.mixer.music.load('song.ogg')
pygame.mixer.music.play(-1)

scores = [0]

# CONSTANTS
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
title = pygame.display.set_caption("PyFlappy by Magoninho")

def main():
    TARGET_FPS = 80
    # paleta de cores

    # pegando a cor
    cor = random.randint(0, len(cores) - 1)

    # stuff #
    PIPE_NUMBER = 2

    ## CLASSES ##

    class Score:
        def __init__(self):
            self.x = 10
            self.y = 10

        def draw(self):
            text = str(bird.score)
            pygame.font.init()
            font = pygame.font.SysFont('', 72)
            text = font.render(text, False, cores[cor][2])
            SCREEN.blit(text, (WIDTH/2-10, self.y))

        def draw_last_score(self):
            text = f"BEST: {bird.high_score[-1]}"
            pygame.font.init()
            font = pygame.font.SysFont('', 32)
            texto = font.render(text, False, cores[cor][2])
            SCREEN.blit(texto, (self.x, self.y))
    # THE BIRD

    class Bird:
        def __init__(self):
            self.x = WIDTH/4
            self.y = HEIGHT/2 - 20
            self.velocity = 0
            self.gravity = 1
            self.score = 0
            self.high_score = sorted(scores)
            self.jump_force = -32

        def draw_bird(self):
            self.rect = pygame.Rect(self.x, self.y, 40, 40)
            pygame.draw.rect(SCREEN, cores[cor][2], self.rect)

        def update(self):  # make the bird fall, controllers etc

            self.draw_bird()
            self.velocity += self.gravity * dt  # aceleração
            # formula do sorvetão kkkkkk
            # eu concerteza nao copiei e colei da net
            self.y += self.velocity * dt + (self.gravity * .5) * (dt * dt)

            # controles #
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.velocity = self.jump_force * dt

            if self.y < 0 or self.y > HEIGHT:
                scores.append(bird.score)
                main()  # reseta do jogo chamado a função main

            for i in range(len(canos)):  # colisões em todas os canos da lista
                if self.rect.colliderect(canos[i].rect_top) or self.rect.colliderect(canos[i].rect_bottom):
                    scores.append(bird.score)
                    main()  # reseta do jogo chamado a função main

    # obstacle

    class Obstacle:
        def __init__(self, x):
            self.x = x
            self.y = random.randint(-300, 0)

            self.space_between = 570
            self.rect_top = pygame.Rect(self.x, self.y, 80, 400)
            self.rect_bottom = pygame.Rect(
                self.x, self.y + self.space_between, 80, 400)

            self.pipe_vel = 9

        def draw(self):
            self.rect_top.x -= self.pipe_vel * dt
            self.rect_bottom.x -= self.pipe_vel * dt
            pygame.draw.rect(SCREEN, cores[cor][1], self.rect_top)
            pygame.draw.rect(SCREEN, cores[cor][1], self.rect_bottom)
            if self.rect_top.x < -80:
                self.rect_top.x = WIDTH
                self.rect_bottom.x = WIDTH
                self.rect_top.y = random.randint(-300, 0)
                self.rect_bottom.y = self.rect_top.y + 570
                bird.score += 1

    # functions
    # Limpador de tela multiplataforma Magoninho Gamer versão 1.2
    def limpa_cosole():
        os.system('cls' if os.name == 'nt' else 'clear')

    # object instances
    bird = Bird()
    obj_score = Score()

    canos = []

    x = WIDTH
    for i in range(PIPE_NUMBER):
        x += WIDTH/PIPE_NUMBER + 40
        obstacle = Obstacle(x)
        canos.append(obstacle)

    # GAME LOOP
    while True:
        clock = pygame.time.Clock()
        dt = clock.tick(240) * .001 * TARGET_FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        SCREEN.fill(cores[cor][0])
        # drawinings
        bird.draw_bird()
        bird.update()
        for cano in range(PIPE_NUMBER):
            canos[cano].draw()
        obj_score.draw()
        obj_score.draw_last_score()

        pygame.display.update()


main()

"""
Feito com carinho
pelo Magoninho :D
"""
