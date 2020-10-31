import pygame

# CONSTANTS
## display settings
WIDTH, HEIGHT = 400, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

## COLORS
WHITE = (255, 255, 255)
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
    def __init__(self, screen, x, y, size):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = size
        
    def player_move(self):
        
        vel = 0.1

        keys = pygame.key.get_pressed()  # get the keys pressed
        
        self.x += self.vx
        self.y += self.vy

        self.vx, self.vy = 0, 0

        """
        Everything has to be an if, so the 8 directions system will work fine
        Also I made a realistic physics system for moving the character with vectors and force
        """
        if keys[pygame.K_UP]:  # UP
            self.vy = -vel
        if keys[pygame.K_DOWN]: # DOWN
            self.vy = vel
        if keys[pygame.K_LEFT]: # LEFT
            self.vx = -vel
        if keys[pygame.K_RIGHT]: # RIGHT
            self.vx = vel

        """
        Aplicação do teorema de pitágoras
        """
        if self.vx != 0 and self.vy != 0:
            self.vx /= 1.414
            self.vy /= 1.414


    def draw_player(self):
        player_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(self.screen, WHITE, player_rect)
        self.player_move()

# object instances
player = Player(SCREEN, 0, 0, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()


    # Drawinings
    SCREEN.fill(BLACK)

    player.draw_player()

    
    pygame.display.update()
