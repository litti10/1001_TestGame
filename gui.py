from tkinter import image_names
import pygame
import math

pygame.init()

class GUI:
    def __init__(self, game_array, px_height):
        self.game_array = game_array
        self.px_height = px_height
        # screen
        self.row = 3
        self.win = pygame.display.set_mode((self.px_height,self.px_height))

        # Images
        self.o_image = pygame.transform.scale(pygame.image.load("images/o.png"), (80, 80))
        self.x_image = pygame.transform.scale(pygame.image.load("images/x.png"), (80, 80))
        self.images = []

        # font
        self.font = pygame.font.SysFont('arial', 40)

        # color
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.gray = (200,200,200)
        self.red = (255,0,0)
        self.blue = (0,0,255)

        self.x_turn = True

    def render(self):
        self.win.fill(self.white)
        self.draw_grid()

        for image in self.images:
            self.x,self.y,self.IMAGE = image
            self.win.blit(self.IMAGE, (self.x-self.IMAGE.get_width()//2, self.y-self.IMAGE.get_height()//2))

        pygame.display.update()

    def draw_grid(self):
        gap = self.px_height//self.row

        x = 0
        y = 0

        for idx in range(self.row):
            x = idx*gap
            pygame.draw.line(self.win,self.gray,(x,0),(x,self.px_height),3)
            pygame.draw.line(self.win,self.gray,(0,x),(self.px_height,x),3)

    def click(self):
        m_x, m_y = pygame.mouse.get_pos()
        
        for i in range(len(self.game_array)):
            for j in range(len(self.game_array[i])):
                x,y,char,can_play = self.game_array[i][j]
                dis = math.sqrt((x-m_x) ** 2 + (y-m_y)**2)

                if dis < self.px_height // self.row // 2 and can_play:
                    if self.x_turn:
                        self.x_turn = False
                        self.images.append((x, y, self.x_image))
                        self.game_array[i][j] = (x,y,'x',False)
                        return True
                    else:
                        self.x_turn = True
                        self.images.append((x, y, self.o_image))
                        self.game_array[i][j] = (x,y,'o',False)
                        return True

    def display_message(self, content):
        pygame.time.delay(500)
        self.win.fill(self.white)
        end_text = self.font.render(content,1,self.black)
        self.win.blit(end_text, ((self.px_height - end_text.get_width()) // 2, (self.px_height - end_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.delay(3000)
