import pygame

# CONSTANTS
## display settings
WIDTH, HEIGHT = 300, 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

## COLORS
WHITE = (0, 0, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

###########

# Functions
def function():
    pass

# Classes
"""
dont remember to:
- create the rects
"""
class Player:
    def __init__(self):
        pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    pygame.display.update()
