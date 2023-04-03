import pygame

class Snake:
    def __init__(self):
        pass

    def draw_snake(self,display, color, snakebody, s_list):
        for i in s_list:
            pygame.draw.rect(display,color,[i[0],i[1],snakebody,snakebody])
