import os
import pygame

dirname = os.path.dirname(__file__)

class Start:
    def __init__(self,display):
        self.display = display
        self.font = pygame.font.Font(
            (os.path.join(dirname,".." ,"fonts", "04B_30__.TTF")), 80
        )
        self.font2 = pygame.font.Font(
            (os.path.join(dirname,".." ,"fonts", "Retro Gaming.ttf")), 30
        )
        self.title = self.font.render("SNAKE", True, (0,255,0))
        self.start = self.font2.render("Press SPACE to Start", True, (255,255,255))
        self.exit = self.font2.render("Press ESC to Exit", True, (255,255,255))
        self.color = self.font2.render("C to Change Color", True, (255,255,255))
        self.black_snake = pygame.image.load(
            os.path.join(dirname,".." ,"images", "blacksnake.png")
        )
        self.blue_snake = pygame.image.load(
            os.path.join(dirname,".." ,"images", "bluesnake.png")
        )
        self.red_snake = pygame.image.load(
            os.path.join(dirname,".." ,"images", "redsnake.png")
        )
        self.yellow_snake = pygame.image.load(
            os.path.join(dirname,".." ,"images", "yellowsnake.png")
        )

    def start_screen(self,color):
        if color == 0:
            self.display.blit(self.black_snake,(0,0))
        if color == 1:
            self.display.blit(self.blue_snake,(0,0))
        if color == 2:
            self.display.blit(self.red_snake,(0,0))
        if color == 3:
            self.display.blit(self.yellow_snake,(0,0))
        self.display.blit(self.title,(300-self.title.get_width()/2, 180-self.title.get_height()/3))
        self.display.blit(self.start,(300-self.start.get_width()/2, 380+self.exit.get_height()/2))
        self.display.blit(self.color,(300-self.exit.get_width()/2, 425+self.start.get_height()/2))
        self.display.blit(self.exit,(300-self.exit.get_width()/2, 470+self.start.get_height()/2))
