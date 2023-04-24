import os
import pygame

dirname = os.path.dirname(__file__)

class Score:
    """Piirtää pelaajan keräämien pisteitä lukumäärää pelin aikana näytölle.

    Attributes:
        font: Fontti jolla teksti kirjoitetaan.
        points, high_score: Kertovat mitä näytölle kirjoitetaan.
    """
    def __init__(self):
        """Luokan kontruktori, joka määrittää fontin jolla kirjoitetaan.
        """
        self.font = pygame.font.Font(
            (os.path.join(dirname,".." ,"fonts", "Retro Gaming.ttf")), 30
        )

    def draw_scrore(self,display,score):
        """Piirtää pelaajaan keräämien pisteiden määrää pelin aikana.

        Args:
            display: Näyttö, jolle piirretään.
            score: Kertoo pisteiden määrän.
        """
        points = self.font.render("Score: "+str(score), True, (255,255,255))
        display.blit(points,(10,0))

    def draw_hs(self,display,high_score):
        """Piirtää pelin aikana pelaajan saanutta huppitulosta.

        Args:
            display: Näyttö, jolle piirretään.
            hs: Kertoo ennätyspisteiden määrän.
        """
        high_score = self.font.render("High Score: "+str(high_score), True, (255,255,255))
        display.blit(high_score,(600-high_score.get_width()-10,0))
