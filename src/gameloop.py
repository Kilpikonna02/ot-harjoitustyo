import pygame
from gameover import Gameover
from start import Start
from wall import Wall
from score import Score
from death import Death
from snake import Snake
from random import randint


class GameLoop:
    def __init__(self, display):
        self._display = display
        self.snake_body_size = 20
        self.tickspeed = 20
        self.clock = pygame.time.Clock()
        x,y = self._display.get_size()
        self._display_width = x
        self._display_height = y
        self.game_start = True

    
    def startgame(self):
        while self.game_start == True:
            start = Start()
            start.start_screen(self._display)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.game()
                        self.game_start = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()


    def game(self):

        game_over = False

        self.snake_posx = (self._display_width/2)
        self.snake_posy = (self._display_height/2)

        self.snake_speed_x = 0
        self.snake_speed_y = 0

        self.points = 0

        size = self._display_width/15

        self.pointx = round(randint((size/20),(self._display_width/20)-(size/20)-(self.snake_body_size/20)))*20
        self.pointy = round(randint((size/20),(self._display_height/20)-(size/20)-(self.snake_body_size/20)))*20

        self.snakesbody = []
        self.snakelenght = 1

        game_end = Gameover()
        wall = Wall(self._display,size)
        score = Score()
        death = Death()
        snake = Snake()

        while True:

            while game_over == True:
                game_end.game_over_screen(self._display,self.points)
                

                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            quit()
                        if event.key == pygame.K_r:
                            self.game_start = True
                            self.startgame()

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.snake_speed_x = -self.snake_body_size
                            self.snake_speed_y = 0
                        if event.key == pygame.K_RIGHT:
                            self.snake_speed_x = self.snake_body_size
                            self.snake_speed_y = 0
                        if event.key == pygame.K_UP:
                            self.snake_speed_x = 0
                            self.snake_speed_y = -self.snake_body_size
                        if event.key == pygame.K_DOWN:
                            self.snake_speed_x = 0
                            self.snake_speed_y = self.snake_body_size
                    elif event.type == pygame.QUIT:
                        break
            
            if death.check_death(self.snake_posx,self.snake_posy) == True:
                game_over = True

            
            self.snake_posx += self.snake_speed_x
            self.snake_posy += self.snake_speed_y
            self._display.fill((150,255,110))
            pygame.draw.rect(self._display,(255,0,0), [self.pointx,self.pointy,self.snake_body_size,self.snake_body_size])
            snake_head = []
            snake_head.append(self.snake_posx)
            snake_head.append(self.snake_posy)
            self.snakesbody.append(snake_head)
            if len(self.snakesbody) > self.snakelenght:
                del self.snakesbody[0]
            for i in self.snakesbody[:-1]:
                if i == snake_head:
                    game_over = True
            snake.draw_snake(self._display,(0,0,0),self.snake_body_size,self.snakesbody)
            wall.draw()
            score.draw_scrore(self._display,self.points)

            pygame.display.update()

            if self.snake_posx == self.pointx and self.snake_posy == self.pointy:
                self.pointx = round(randint((size/20),(self._display_width/20)-(size/20)-(self.snake_body_size/20)))*20
                self.pointy = round(randint((size/20),(self._display_height/20)-(size/20)-(self.snake_body_size/20)))*20
                self.points += 1
                self.snakelenght += 1
            
            self.clock.tick(self.tickspeed)


   
