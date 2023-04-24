import pygame

class Snake:
    """Luokka, jonka avulla mato piirretään näytölle.

    Attributes:
        display: Näyttö, jolle piirretään.
    """

    def __init__(self,display):
        """Luokan konstruktori, joka määrittää näytön jolle piirretään.

        Args:
            display: Näyttö, jolle piirretään.
        """
        self._display = display

    def draw_snake(self, color, snakebody, s_list):
        """Piirtää matoa näytölle

        Args:
            color: Kertoo madon värin.
            snakebody: Keroo yhden madon osan koon.
            s_list: Lista jossa on madon kulkeman reitin koordinaatit.
        """
        for i in s_list:
            pygame.draw.rect(self._display,color,[i[0],i[1],snakebody,snakebody])
