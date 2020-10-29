import pygame, sys
from bird import *
from consts import *
from cano import *


## display settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))

## condition to play+
started = False
pygame.font.init()
font = pygame.font.SysFont("Arial", 32)
text = font.render("Press up arrow to start", False, consts.BLACK)


## instanciar objetos
player = Bird(screen, started)

canos = []
x = consts.WIDTH - 100
for i in range(2):
    cano = Cano(screen, x)
    x += consts.WIDTH/2 + 40
    canos.append(cano)
    canos[i].x += i 
    print(canos[i].y)

## game loop
while True:
    clock = pygame.time.Clock()
    clock.tick(60)

    for event in pygame.event.get():
        ## clicar no x
        if event.type == pygame.QUIT:
            pygame.quit()

        ## apertar esc
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            

    screen.fill(CYAN)
    # player.draw_dino()
    player.update(started)
    if not player.started:
        screen.blit(text, (consts.WIDTH / 6, consts.HEIGHT / 1.5))

    for x in range(2):
        teste = canos[x].draw(player.started, player)

    
    ## display update
    pygame.display.update()
