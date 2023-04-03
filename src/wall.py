import pygame

class Wall:
    def __init__(self,display,size):
        self._display = display
        self.size = size
        self._display_width,self._display_height = self._display.get_size()

    def draw(self):
        for i in range(15):
            pygame.draw.rect(self._display,(0,0,0),[i*self.size,0,self.size,self.size])
            pygame.draw.rect(self._display,(0,0,0),[i*self.size,14*self.size,self.size,self.size])
        for j in range(15):
            pygame.draw.rect(self._display,(0,0,0),[0,j*self.size,self.size,self.size])
            pygame.draw.rect(self._display,(0,0,0),[14*self.size,j*self.size,self.size,self.size])
        