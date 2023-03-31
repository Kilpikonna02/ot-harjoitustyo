import pygame

class Wall:
    def __init__(self,display,size):
        self._display = display
        self.size = size
        x,y = self._display.get_size()
        self._display_width = x
        self._display_height = y
        self.quantity_x = self._display_width/size
        self.quantity_y = self._display_height/size
    
    def draw(self):
        for i in range(int(self.quantity_x)):
            pygame.draw.rect(self._display,(0,0,0),[i*self.size,0,self.size,self.size])
            pygame.draw.rect(self._display,(0,0,0),[i*self.size,(self.quantity_y-1)*self.size,self.size,self.size])
        for j in range(int(self.quantity_x)):
            pygame.draw.rect(self._display,(0,0,0),[0,j*self.size,self.size,self.size])
            pygame.draw.rect(self._display,(0,0,0),[(self.quantity_x-1)*self.size,j*self.size,self.size,self.size])
        