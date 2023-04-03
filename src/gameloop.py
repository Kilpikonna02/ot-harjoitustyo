import sys
import pygame
from gameover import Gameover
from start import Start
from wall import Wall
from score import Score
from death import Death
from snake import Snake
from point import Point

class GameLoop:
    def __init__(self, display):
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
        self.snake = Snake()
        self.point = Point(self._display)

    def startgame(self):
        while self.game_start is True:
            start = Start(self._display)
            start.start_screen()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.game()
                        self.game_start = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()


    def game(self):

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
                self.game_end.game_over_screen(self.points)

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
            self._display.fill((150,255,110))
            self.point.draw_point()
            snake_body_list = []
            snake_body_list.append(self.snake_posx)
            snake_body_list.append(self.snake_posy)
            self.snakesbody.append(snake_body_list)
            if len(self.snakesbody) > self.snakelenght:
                del self.snakesbody[0]
            if snake_body_list in self.snakesbody[:-1]:
                game_over = True
            self.snake.draw_snake(self._display,(0,0,0),20,self.snakesbody)
            self.wall.draw()
            self.score.draw_scrore(self._display,self.points)

            pygame.display.update()

            if self.point.check(self.snake_posx,self.snake_posy) is True:
                self.point.new_coordinates()
                self.points += 1
                self.snakelenght += 1

            self.clock.tick(20)
