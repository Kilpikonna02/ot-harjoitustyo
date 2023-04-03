import os
import pygame

dirname = os.path.dirname(__file__)

class Start:
    def __init__(self,display):
        self.display = display
        self.font = pygame.font.Font(
            (os.path.join(dirname, "fonts", "04B_30__.TTF")), 80
        )
        self.font2 = pygame.font.Font(
            (os.path.join(dirname, "fonts", "Retro Gaming.ttf")), 30
        )
        self.title = self.font.render("SNAKE", True, (0,255,0))
        self.start = self.font2.render("Press SPACE to Start", True, (255,255,255))
        self.exit = self.font2.render("Press ESC to Exit", True, (255,255,255))

    def start_screen(self):
        self.display.fill((0,0,0))
        self.display.blit(self.title,(300-self.title.get_width()/2, 180-self.title.get_height()/3))
        self.display.blit(self.start,(300-self.start.get_width()/2, 290+self.exit.get_height()/2))
        self.display.blit(self.exit,(300-self.exit.get_width()/2, 335+self.start.get_height()/2))
