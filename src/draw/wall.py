import pygame

class Wall:
    """Luokka, joka piirtää pelin reinoille seinät.

    Attributes:
        display: Näyttö, jolle piirretään.
        size: Kertoo yhden seinän osan koon.
    """

    def __init__(self,display,size):
        """Luokan konstruktori, joka määrittää näytön, jolle seinä piirretään ja seinän osien koon.

        Args:
            display: Näyttö, jolle piirretään.
            size: Kertoo yhden seinän osan koon
        """
        self._display = display
        self.size = size

    def draw(self):
        """Piirtää seinät ympäröimään näyttöä pelin aikana.
        """
        for i in range(15):
            pygame.draw.rect(self._display,(0,0,0),[i*self.size,0,self.size,self.size])
            pygame.draw.rect(self._display,(0,0,0),[i*self.size,14*self.size,self.size,self.size])
        for j in range(15):
            pygame.draw.rect(self._display,(0,0,0),[0,j*self.size,self.size,self.size])
            pygame.draw.rect(self._display,(0,0,0),[14*self.size,j*self.size,self.size,self.size])
        