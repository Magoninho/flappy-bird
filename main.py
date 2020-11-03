import pygame
import sys
from bird import *
from consts import *
from cano import *


# display settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# condition to play+
started = False
pygame.font.init()
font = pygame.font.SysFont("Arial", 32)
text = font.render("Press up arrow to start", False, consts.BLACK)


# instanciar objetos
player = Bird(screen, started)

canos = []  # canos agrupados

x = consts.WIDTH + consts.DISTANCIA_INICIAL_DO_CANO
for i in range(consts.PIPE_NUMBER):
    cano = Cano(screen, x)
    canos.append(cano)
    x += consts.WIDTH/consts.PIPE_NUMBER + 40
    print(canos)


# game loop
while True:
    clock = pygame.time.Clock()
    clock.tick(60)

    for event in pygame.event.get():
        # clicar no x
        if event.type == pygame.QUIT:
            pygame.quit()

        # apertar esc
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    screen.fill(CYAN)
    # player.draw_dino()
    player.update(started)
    if not player.started:
        screen.blit(text, (consts.WIDTH / 6, consts.HEIGHT / 1.5))

    for x in range(consts.PIPE_NUMBER):
        teste = canos[x].draw(player.started, player)

    # display update
    pygame.display.update()
