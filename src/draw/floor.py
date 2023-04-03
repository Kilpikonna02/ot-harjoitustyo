import pygame

class Floor:
    def __init__(self,display):
        self._display = display

    def draw(self):
        for j in range(30):
            for i in range(30):
                if j%2 == 0 or j == 0:
                    if i%2 == 0 or i == 0:
                        pygame.draw.rect(self._display,(150,255,110),[i*20,j*20,20,20])
                    else:
                        pygame.draw.rect(self._display,(130,215,95),[i*20,j*20,20,20])
                else:
                    if i%2 == 0 or i == 0:
                        pygame.draw.rect(self._display,(130,215,95),[i*20,j*20,20,20])
                    else:
                        pygame.draw.rect(self._display,(150,255,110),[i*20,j*20,20,20])



        