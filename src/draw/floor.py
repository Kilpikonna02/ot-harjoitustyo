import pygame

class Floor:
    def __init__(self,display):
        self._display = display

    def draw(self):
        for j in range(30):
            for i in range(30):
                color = (150,255,110) if (i+j)%2 == 0 else (130,215,95)
                pygame.draw.rect(self._display,color,[i*20,j*20,20,20])
