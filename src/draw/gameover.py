import os
import pygame

dirname = os.path.dirname(__file__)

class Gameover:
    def __init__(self, display):
        self._display = display
        self._display_width,self._display_height = display.get_size()
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

    def game_over_screen(self,score):
        endscore = self.font3.render("Score: "+str(score), True, (255,255,255))
        self._display.fill((0,0,0))
        self._display.blit(self.g_o,(300-self.g_o.get_width()/2, 180-self.g_o.get_height()/3))
        self._display.blit(self.res,(300-self.res.get_width()/2, 290+self.exit.get_height()/2))
        self._display.blit(self.exit,(300-self.exit.get_width()/2, 335+self.res.get_height()/2))
        self._display.blit(endscore,(300-endscore.get_width()/2, 218+endscore.get_height()/2))
        pygame.display.update()
