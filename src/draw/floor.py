import pygame

class Floor:
    """Luokka, joka piirtää lattian ruutu kuvion.

    Attributes:
        display: Näyttö, jolle piirretään.
    """
    def __init__(self,display):
        """Luokan konstruktori, joka määrittää näytön jolle piirretään.

        Args:
            display: Näyttö, jolle piirretään.
        """
        self._display = display

    def draw(self):
        """Piirttää ruutokuviota näytölle, jossa joka toinen ruutu on eri värinen.
        """
        for j in range(30):
            for i in range(30):
                color = (150,255,110) if (i+j)%2 == 0 else (130,215,95)
                pygame.draw.rect(self._display,color,[i*20,j*20,20,20])
