import pygame

class Snake:
    def __init__(self,display):
        self._display = display

    def draw_snake(self, color, snakebody, s_list):
        for i in s_list:
            pygame.draw.rect(self._display,color,[i[0],i[1],snakebody,snakebody])
