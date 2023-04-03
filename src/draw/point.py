from random import randint
import pygame

class Point:
    def __init__(self, display):
        self._display = display
        self.pointx = round(randint(40,540)/20)*20
        self.pointy = round(randint(40,540)/20)*20

    def new_coordinates(self):
        self.pointx = round(randint(40,540)/20)*20
        self.pointy = round(randint(40,540)/20)*20

    def draw_point(self):
        pygame.draw.rect(self._display,(255,0,0), [self.pointx,self.pointy,20,20])

    def check(self,pos_x,pos_y):
        if pos_x == self.pointx and pos_y == self.pointy:
            return True
        return False
