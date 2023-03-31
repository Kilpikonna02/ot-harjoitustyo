import pygame
import os

dirname = os.path.dirname(__file__)

class Score:
    def __init__(self, display):
        self._display = display
        self.font = pygame.font.Font(
            (os.path.join(dirname, "fonts", "Retro Gaming.ttf")), 30
        )
    
    def draw_scrore(self,score):
        points = self.font.render("Score: "+str(score), True, (255,255,255))
        self._display.blit(points,(10,0))