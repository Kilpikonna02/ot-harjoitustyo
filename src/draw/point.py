import os
from random import randint
import pygame

dirname = os.path.dirname(__file__)

class Point:
    def __init__(self, display):
        self._display = display
        self.pointx = round(randint(40,540)/20)*20
        self.pointy = round(randint(40,540)/20)*20
        self.point = pygame.image.load(
            os.path.join(dirname,".." ,"images", "point.png")
        )

    def new_coordinates(self):
        self.pointx = round(randint(40,540)/20)*20
        self.pointy = round(randint(40,540)/20)*20

    def draw_point(self):
        self._display.blit(self.point,(self.pointx,self.pointy))

    def check(self,pos_x,pos_y):
        if pos_x == self.pointx and pos_y == self.pointy:
            return True
        return False
