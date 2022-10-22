import pygame

pygame.init()

class GUI:
    def __init__(self):
        # screen
        self.width = 300
        self.row = 3
        win = pygame.display.set_mode((self.width,self.width))

        # Images
        self.o_image = pygame.transform.scale(pygame.image.load("images/o.png"), (80, 80))
        self.x_image = pygame.transform.scale(pygame.image.load("images/x.png"), (80, 80))

        # font
        self.font = pygame.font.Sysfont('arial', 40)

        # color
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.gray = (200,200,200)
        self.red = (255,0,0)
        self.blue = (0,0,255)
