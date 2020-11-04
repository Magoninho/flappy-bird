import pygame, consts, math

class Bird:
    def __init__(self, screen, started):
        self.screen = screen
        self.started = started
        self.x = 80
        self.y = consts.HEIGHT/2 - 40
        self.xspeed = 5
        self.yspeed = 2
        self.GRAVITY = 1
        self.JUMP_FORCE = -9
        self.bird_rect = pygame.Rect((self.x, self.y, 40, 40))
        self.bird = None

    def jump(self):
        
        self.yspeed = self.JUMP_FORCE

    # def check_collision(self, cano):
    #     if self.bird_rect.colliderect(cano):
    #         print("kldafgj")

    def draw_dino(self):
        self.bird_rect = pygame.Rect((self.x, self.y, 40, 40))
        pygame.draw.rect(self.screen, consts.YELLOW, self.bird_rect)

    def update(self, started):
        self.draw_dino()
        ## Keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.started = True
            self.jump()

        ###########
        
        if self.started:
            self.y += self.yspeed
            self.yspeed += self.GRAVITY  # aceleraçao

        if self.y > consts.HEIGHT - 40 or self.y < 0:
            self.y = consts.HEIGHT / 2 - 40
            self.started = False
        ###########
        #colisions#
        ###########
        # if self.bird_rect.colliderect():
        #     print("fgjh")
        