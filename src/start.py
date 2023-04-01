import pygame
import os

dirname = os.path.dirname(__file__)

class Start:
    def __init__(self):
        font = pygame.font.Font(
            (os.path.join(dirname, "fonts", "04B_30__.TTF")), 80
        )
        font2 = pygame.font.Font(
            (os.path.join(dirname, "fonts", "Retro Gaming.ttf")), 30
        )
        self.title = font.render("SNAKE", True, (0,255,0))
        self.start = font2.render("Press SPACE to Start", True, (255,255,255))
        self.exit = font2.render("Press ESC to Exit", True, (255,255,255))

    def start_screen(self,display):
        x,y = display.get_size()
        self._display_width = x
        self._display_height = y
        display.fill((0,0,0))
        display.blit(self.title,(self._display_width/2-self.title.get_width()/2, self._display_height/3-self.title.get_height()/3-20))
        display.blit(self.start,(self._display_width/2-self.start.get_width()/2, self._display_height/2-10+self.exit.get_height()/2))
        display.blit(self.exit,(self._display_width/2-self.exit.get_width()/2, self._display_height/1.9+self.start.get_height()/2+20))
