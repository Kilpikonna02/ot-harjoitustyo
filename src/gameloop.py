import sys
import pygame
from death import Death
from draw.snake import Snake
from draw.gameover import Gameover
from draw.start import Start
from draw.wall import Wall
from draw.score import Score
from draw.point import Point
from draw.floor import Floor

class GameLoop:
    """Luokka, joka pyörittää koko peliä.

    Attributes:
        display: Näyttö, jolle piirretään.
        clock: Sen avulla määritetään näytön päivitys nopeus.
        display_width, display_height: Kertovat näytön leveyden ja korkeuden
        game_start: Kertoo pelin alkunäytön tilan.
        snake_lenght: Kertoo madon pituuden.
        snakebody: Lista, joka ottaa talteen madon kulkeman reitin koordinaatteja.
        points: Kertoo kerättyjen pisteiden määrän.
        snake_speed_x, snake_speed_y: Kertovat madon liikesuunnan.
        snake_posx, snake_posy: Kertovat madon sijainnin.
        game_end: Luokan Gameover määrittely.
        wall: Luokan Wall määrittely.
        score: Luokan Score määrittely.
        death: Luokan Death määrittely.
        snake: Luokan Snake määrittely.
        point: Luokan Point määrittely.
        floor: Luokan Floor määrittely.
        start: Luokan Start määrittely.
        color: Kertoo madon värin.
        file: Tiedosto jossa säilytetään ennätyspiste määrää.
        high_score: Kertoo ennätyspisteiden määrän.
        game_over: Kertoo pelin lopetus näytön tilan.

    """
    def __init__(self, display):
        """Luoka konstruktori, joka määrittelee kaikki pelin alku arvot.

        Args:
            display: Näyttö, jolle piirretään.
        """
        self._display = display
        self.clock = pygame.time.Clock()
        self._display_width,self._display_height = self._display.get_size()
        self.game_start = True
        self.snakelenght = 1
        self.snakesbody = []
        self.points = 0
        self.snake_speed_x = 0
        self.snake_speed_y = 0
        self.snake_posx = self._display_width/2
        self.snake_posy = self._display_height/2
        self.game_end = Gameover(self._display)
        self.wall = Wall(self._display,40)
        self.score = Score()
        self.death = Death()
        self.snake = Snake(self._display)
        self.point = Point(self._display)
        self.floor = Floor(self._display)
        self.color = 0
        file = open("./src/highscore.txt","r+")
        self.high_score = file.read()

    def startgame(self):
        """Piirtää pelin aloitus menun kun peli käynnistyy ja muuttaa pelin tilaa pelaajan riippuen mitä näppäimiä pelaaja painaa.
        """
        while self.game_start is True:
            start = Start(self._display)
            start.start_screen(self.color)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_c:
                        self.color += 1
                        if self.color >= 4:
                            self.color = 0
                        start.start_screen(self.color)
                    if event.key == pygame.K_SPACE:
                        self.game()
                        self.game_start = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()


    def game(self):
        """Käytössä kun peli on käynnissä tai kun pelaaja häviää pelin. Liikuttaa matoa ja käyttää suurinta osaa muista luokista.
        """

        game_over = False

        self.snake_posx = self._display_width/2
        self.snake_posy = self._display_height/2

        self.snake_speed_x = 0
        self.snake_speed_y = 0

        self.points = 0

        self.point.new_coordinates()

        self.snakesbody = []
        self.snakelenght = 1

        while True:

            while game_over is True:
                if int(self.high_score) < int(self.points):
                    file = open("./src/highscore.txt","w")
                    file.write(str(self.points))
                file = open("./src/highscore.txt","r+")
                self.high_score = file.read()
                self.game_end.game_over_screen(self.points,self.high_score)

                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_r:
                            self.game_start = True
                            self.startgame()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake_speed_x = -20
                        self.snake_speed_y = 0
                    if event.key == pygame.K_RIGHT:
                        self.snake_speed_x = 20
                        self.snake_speed_y = 0
                    if event.key == pygame.K_UP:
                        self.snake_speed_x = 0
                        self.snake_speed_y = -20
                    if event.key == pygame.K_DOWN:
                        self.snake_speed_x = 0
                        self.snake_speed_y = 20
                elif event.type == pygame.QUIT:
                    break

            if self.death.check_death(self.snake_posx,self.snake_posy) is True:
                game_over = True

            self.snake_posx += self.snake_speed_x
            self.snake_posy += self.snake_speed_y
            self.floor.draw()
            self.point.draw_point()
            snake_body_list = []
            snake_body_list.append(self.snake_posx)
            snake_body_list.append(self.snake_posy)
            self.snakesbody.append(snake_body_list)
            if len(self.snakesbody) > self.snakelenght:
                del self.snakesbody[0]
            if snake_body_list in self.snakesbody[:-1]:
                game_over = True
            if self.color == 0:
                self.snake.draw_snake((0,0,0),20,self.snakesbody)
            if self.color == 1:
                self.snake.draw_snake((0,18,255),20,self.snakesbody)
            if self.color == 2:
                self.snake.draw_snake((255,25,0),20,self.snakesbody)
            if self.color == 3:
                self.snake.draw_snake((255,237,0),20,self.snakesbody)
            self.wall.draw()
            self.score.draw_scrore(self._display,self.points)
            if int(self.high_score) < int(self.points):
                self.score.draw_hs(self._display,self.points)
            else:
                self.score.draw_hs(self._display,self.high_score)

            pygame.display.update()

            if self.point.check(self.snake_posx,self.snake_posy) is True:
                self.point.new_coordinates()
                self.points += 1
                self.snakelenght += 1

            self.clock.tick(20)
