import os
import pygame

dirname = os.path.dirname(__file__)

class Gameover:
    """Luokka, joka piirtää pelin lopetus näytön.

    Attributes:
        display: Näyttö, jolle piirretään.
        font1, font2, font3: Eri fontit teksteille
        g_o, res, exit, end_score, high_score: Kertovat mitä näytölle kirjoitetaan.
    """
    def __init__(self, display):
        """Luokan konstruktori, joka luo uuden lopetus näytön.

        Args:
            display: Näyttö, jolle piirretään.
        """
        self._display = display
        font = pygame.font.Font(
            (os.path.join(dirname,".." ,"fonts", "upheavtt.ttf")), 90
        )
        font2 = pygame.font.Font(
            (os.path.join(dirname,".." ,"fonts", "Retro Gaming.ttf")), 30
        )
        self.font3 = pygame.font.Font(
            (os.path.join(dirname,".." ,"fonts", "Retro Gaming.ttf")), 40
        )
        self.g_o = font.render("GAME OVER", True, (255,0,0))
        self.res = font2.render("Press R to Restart", True, (255,255,255))
        self.exit = font2.render("Press ESC to Exit", True, (255,255,255))

    def game_over_screen(self,score,high_score):
        """Piirtää lopetus näytön pelin loputtua.

        Args:
            score: Kertoo piste määrän jonka pelaaja sai kerättyä pelin aikana.
            hs: Kertoo suurimman piste ennätyksen, jonka pelaaja on saanut.
        """
        end_score = self.font3.render("Score: "+str(score), True, (255,255,255))
        high_score = self.font3.render("High Score: "+str(high_score), True, (255,255,255))
        self._display.fill((0,0,0))
        self._display.blit(self.g_o,(300-self.g_o.get_width()/2, 160-self.g_o.get_height()/3))
        self._display.blit(self.res,(300-self.res.get_width()/2, 330+self.exit.get_height()/2))
        self._display.blit(self.exit,(300-self.exit.get_width()/2, 375+self.res.get_height()/2))
        self._display.blit(end_score,(300-end_score.get_width()/2, 260+end_score.get_height()/2))
        self._display.blit(high_score,(300-high_score.get_width()/2, 205+high_score.get_height()/2))
        pygame.display.update()
