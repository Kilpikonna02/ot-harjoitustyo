import os
import pygame

dirname = os.path.dirname(__file__)

class Score:
    def __init__(self):
        self.font = pygame.font.Font(
            (os.path.join(dirname, "fonts", "Retro Gaming.ttf")), 30
        )

    def draw_scrore(self,display,score):
        points = self.font.render("Score: "+str(score), True, (255,255,255))
        display.blit(points,(10,0))
