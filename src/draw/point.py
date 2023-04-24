import os
from random import randint
import pygame

dirname = os.path.dirname(__file__)

class Point:
    """Luokka, joka luo pisteet ja määrittelee niiden sijainnin.

    Attributes:
        display: Näyttö, jolle piirretään.
        pointx, pointy: Määriteelevät pisteiden x ja y koordinaattien sijainnit.
        point: Kuva, joka toimii pisteenä.
    """
    def __init__(self, display):
        """Luokan konstruktori, joka määrittää aloitus pisteen koordinaatit.

        Args:
            display: Näyttö, jolle piirretään.
        """
        self._display = display
        self.pointx = round(randint(40,540)/20)*20
        self.pointy = round(randint(40,540)/20)*20
        self.point = pygame.image.load(
            os.path.join(dirname,".." ,"images", "point.png")
        )

    def new_coordinates(self):
        """Määrittää pisteelle uudet koordinaatit.
        """
        self.pointx = round(randint(40,540)/20)*20
        self.pointy = round(randint(40,540)/20)*20

    def draw_point(self):
        """Piirtää pisteen näytölle.
        """
        self._display.blit(self.point,(self.pointx,self.pointy))

    def check(self,pos_x,pos_y):
        """Tarkistaa osuuko madon pää pisteeseen.

        Args:
            pos_x: madon x koordinaatti.
            pos_y: madon y koordinaatti.

        Returns:
            Palauttaa True jos mato osuu pisteeseen ja muuten False.
        """
        if pos_x == self.pointx and pos_y == self.pointy:
            return True
        return False
