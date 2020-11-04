import pygame
import os
import random

pygame.mixer.init()
pygame.mixer.music.load('song2.ogg')
pygame.mixer.music.play(-1)


def main():

    # CONSTANTS
    WIDTH, HEIGHT = 600, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    # colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    YELLOW = (245, 239, 66)
    CYAN = (66, 218, 245)

    # stuff #
    PIPE_NUMBER = 2
    score = 0
    ## CLASSES ##

    # THE BIRD

    class Bird:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.velocity = 0
            self.gravity = 1
            self.alive = True
            self.score = 0

        def draw_bird(self):
            self.rect = pygame.Rect(self.x, self.y, 40, 40)
            pygame.draw.rect(SCREEN, YELLOW, self.rect)

        def update(self):  # make the bird fall, controllers etc

            self.draw_bird()
            self.y += self.velocity
            self.velocity += self.gravity  # aceleração

            # controllers #

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.velocity = -10
            if self.y < 0 or self.y > HEIGHT:
                main()
            for i in range(len(canos)):  # colisões em todas os canos da lista
                if self.rect.colliderect(canos[i].rect_top) or self.rect.colliderect(canos[i].rect_bottom):
                    main()

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
            self.rect_top.x -= self.pipe_vel
            self.rect_bottom.x -= self.pipe_vel
            pygame.draw.rect(SCREEN, GREEN, self.rect_top)
            pygame.draw.rect(SCREEN, GREEN, self.rect_bottom)

            if self.rect_top.x < -80:
                self.rect_top.x = WIDTH
                self.rect_bottom.x = WIDTH
                self.rect_top.y = random.randint(-300, 0)
                self.rect_bottom.y = self.rect_top.y + 570
                limpa_tela()
                bird.score += 1
                print(f"Score: {bird.score}")

    # function
    # Limpador de tela multiplataforma Magoninho Gamer versão 1.2
    def limpa_tela():
        os.system('cls' if os.name == 'nt' else 'clear')
    limpa_tela()
    # object instances
    # obstacle = Obstacle()

    bird_x = WIDTH/4
    bird_y = HEIGHT/2 - 20

    bird = Bird(bird_x, bird_y)

    canos = []

    x = WIDTH
    for i in range(PIPE_NUMBER):
        x += WIDTH/PIPE_NUMBER + 40
        obstacle = Obstacle(x)
        canos.append(obstacle)

    # GAME LOOP
    while True:
        clock = pygame.time.Clock()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        SCREEN.fill(CYAN)
        # drawinings
        bird.draw_bird()
        if bird.alive:
            bird.update()
        for cano in range(PIPE_NUMBER):
            canos[cano].draw()

        pygame.display.update()


main()
