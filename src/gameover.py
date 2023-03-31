import pygame
import os

dirname = os.path.dirname(__file__)

class Gameover:
    def __init__(self, display):
        self._display = display
        font = pygame.font.Font(
            (os.path.join(dirname, "fonts", "upheavtt.ttf")), 90
        )
        font2 = pygame.font.Font(
            (os.path.join(dirname, "fonts", "Retro Gaming.ttf")), 30
        )
        self.font3 = pygame.font.Font(
            (os.path.join(dirname, "fonts", "Retro Gaming.ttf")), 40
        )
        self.game_over = font.render("GAME OVER", True, (255,0,0))
        self.restart = font2.render("Press R to Restart", True, (255,255,255))
        self.quit = font2.render("Press Q to Quit", True, (255,255,255))
        x,y = self._display.get_size()
        self._display_width = x
        self._display_height = y
    
    def game_over_screen(self,score):
        endscore = self.font3.render("Score: "+str(score), True, (255,255,255))
        self._display.fill((0,0,0))
        self._display.blit(self.game_over,(self._display_width/2-self.game_over.get_width()/2, self._display_height/3-self.game_over.get_height()/3-20))
        self._display.blit(self.restart,(self._display_width/2-self.restart.get_width()/2, self._display_height/1.9+self.restart.get_height()/2+20))
        self._display.blit(self.quit,(self._display_width/2-self.quit.get_width()/2, self._display_height/2-10+self.quit.get_height()/2))
        self._display.blit(endscore,(self._display_width/2-endscore.get_width()/2, self._display_height/2.75+endscore.get_height()/2))



    
